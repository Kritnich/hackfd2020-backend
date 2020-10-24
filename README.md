# hackfd2020-backend
Backend component of our HackFD 2020 contribution

# Requirements
- flask
- flask-sqlalchemy
- flask-marshmallow
- sqlalchemy
- marshmallow

# Usage
1. Install python3 and requirements
2. Run `python3` and execute this in the interpeter to initialize the DB at /tmp/test.db
```
from app import db
db.create_all()
```
3. Run `python3 app.py` to start the server

# Requests
Send a GET request with a list of location IDs to retrieve active infections at that location

```GET /infections?locId=<LocationID>&locId=<LocationID>```

Send a POST request with a location ID, start time, end time (both as Unix timestamps) and a code to verify the infection (currently only `iminfected` is valid)
```POST /infections
{
"locId": aad9878ef,
"attendanceStart": 1603559368,
"attendanceEnd": 1603584000,
"code": "iminfected"
}
```
