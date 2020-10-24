from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, fields
from verification import verify_infection

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Infection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    locId = db.Column(db.String, nullable=False)
    attendanceStart = db.Column(db.Integer, nullable=False)
    attendanceEnd = db.Column(db.Integer, nullable=False)

    def __init__(self, locId, attendanceStart, attendanceEnd):
        self.locId = locId
        self.attendanceStart = attendanceStart
        self.attendanceEnd = attendanceEnd

class InfectionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'locId', 'attendanceStart', 'attendanceEnd')

infection_schema = InfectionSchema()
infections_schema = InfectionSchema(many=True)

@app.route('/infections', methods=['POST','GET'])
def infectionsEndpoint():
    # If GET, fetch infections for locations
    if request.method == 'GET':
        locations = request.args.getlist('locId')
        query = Infection.query.filter(Infection.locId.in_(locations)).all()
        infections = infections_schema.dump(query)
        return jsonify(infections), 200

    # If POST, add a new infection
    elif request.method == 'POST':
        infection = request.get_json()
        if not verify_infection(infection.get('code')):
            return jsonify(error='infection code invalid'), 400
        locId = infection.get('locId')
        attendanceStart = infection.get('attendanceStart')
        attendanceEnd = infection.get('attendanceEnd')
        new_infection = Infection(locId, attendanceStart, attendanceEnd)

        db.session.add(new_infection)
        db.session.commit()
        return '{}', 200

if __name__ == '__main__':
    app.run()
