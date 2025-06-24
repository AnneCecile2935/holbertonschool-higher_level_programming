-- create DATA BASE
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Créer l'utilisateur s'il n'existe pas déjà
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Donner uniquement le droit SELECT à cet utilisateur
GRANT SELECT ON hbtn_0d_2 *TO 'user_0d_2'@'localhost';

-- Appliquer les changements
FLUSH PRIVILEGES;

