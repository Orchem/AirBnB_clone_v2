-- create database hbnb_dev_db
-- create user hbnb_dev on mysql server and set password to hbnb_dev_pwd
-- set privileges for hbnb_dev
-- script does not fail if user exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
		IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
