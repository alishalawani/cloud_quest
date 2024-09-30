-- settings.sql
CREATE DATABASE nimbo;
CREATE USER nimbouser WITH PASSWORD 'nimbo';
GRANT ALL PRIVILEGES ON DATABASE nimbo TO nimbouser;