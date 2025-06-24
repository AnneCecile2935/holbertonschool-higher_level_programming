-- create user if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- with all privilege on data bases
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'local_host';
-- apply the changes
FLUSH PRIVILEGES;
