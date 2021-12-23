-- Creating database call hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creating user hbnbn_test and set password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';
-- Giving all permissions to the database hbnbn_test_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';
-- Giving permission SELECT to the database performance_schema
GRANT SELECT ON performance_schema.*
TO 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';
-- Refresh all priviliges
FLUSH PRIVILEGES;
