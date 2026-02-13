-- CREATE DATABASE IF NOT EXISTS `snacks`;

-- SHOW DATABASES;
-- USE `snacks`;
-- DROP TABLE IF EXISTS `snack_info`;
-- CREATE TABLE `snack_info`(
--     `snack_id` INT PRIMARY KEY AUTO_INCREMENT,
--     `snack_name` VARCHAR(20) UNIQUE NOT NULL,
--     `price` DECIMAL(5,1) NOT NULL,
--     `amount` INT NOT NULL,
--     `ate` CHAR(2) NOT NULL,
--     `buy_date` DATE NOT NULL,
--     `buyer` VARCHAR(20) NOT NULL
-- );
--  
-- INSERT INTO `snack_info` VALUES (1, 'Oreo' , 26, 1 , 'NO', 20220611, 'PETER');
-- INSERT INTO `snack_info` VALUES (2, 'Ritz' , 23.5, 2 , 'NO', 20220530, 'MARY');
-- INSERT INTO `snack_info` VALUES (3, 'Calbee' , 22.6, 1 , 'YS', 20220611, 'AMY');
-- INSERT INTO `snack_info` VALUES (4, 'Pringles' , 29, 1 , 'NO', 20220515, 'MARY');
-- INSERT INTO `snack_info` VALUES (5, 'Wise' , 15.4, 2 , 'YS', 20220605, 'KIN');
-- INSERT INTO `snack_info` VALUES (6, 'Lays' , 24.9, 3 , 'NO', 20220514, 'PETER');
-- INSERT INTO `snack_info` VALUES (7, 'Choco_Pie' , 26, 1 , 'YS', 20220601, 'AMY');
-- INSERT INTO `snack_info` VALUES (8, 'Ice_cream' , 26, 2 , 'NO', 20220615, 'AMY');
--  
-- CREATE USER 'CRUD'@'localhost' IDENTIFIED BY 'password';
-- CREATE USER 'Read only'@'localhost' IDENTIFIED BY 'password';
--  
-- GRANT CREATE, SELECT, UPDATE, DELETE ON *.* TO 'CRUD'@'localhost';
-- GRANT SELECT ON `snack_info`.* TO 'Read only'@'localhost';
-- REVOKE SELECT ON `snack_info`.* FROM 'Read only'@'localhost';  

-- SELECT `snack_name` FROM `snack_info`;
-- SELECT snack_name, price, amount
-- FROM snack_info
-- WHERE ATE="NO"

-- SELECT * FROM snack_info
-- ORDER BY amount DESC, snack_name ASC;

-- SELECT COUNT(snack_name) AS "ATE counter"
-- FROM snack_info
-- WHERE ATE="YS";

-- SELECT COUNT(snack_name)
-- FROM snack_info
-- WHERE ATE="YS"

-- SELECT SUM(price)
-- FROM snack_info
-- WHERE buyer="PETER";

-- SELECT AVG(price)
-- FROM snack_info
-- WHERE buyer="MARY";

-- UPDATE `snack_info` SET `price` = 26.0 WHERE `snack_name` = "Ice_cream";
-- SELECT `snack_name`, `price` FROM `snack_info`;

DELETE FROM `snack_info` WHERE `snack_name` = "Ice_cream";
SELECT `snack_name`, `price` FROM `snack_info`