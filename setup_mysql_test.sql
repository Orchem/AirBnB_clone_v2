-- create database hbnb_dev_db
-- create user hbnb_dev on mysql server and set password to hbnb_dev_pwd
-- set privileges for hbnb_dev
-- script does not fail if user exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
		IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

