{ pkgs ? import <nixpkgs> {} }:
with pkgs;

let
  myPythonPackages = ps: with ps; [
    flask
    flask_sqlalchemy
    flask_marshmallow
    sqlalchemy
    marshmallow
  ];
in mkShell {
  buildInputs = [
    (python3.withPackages myPythonPackages)
  ];
}
