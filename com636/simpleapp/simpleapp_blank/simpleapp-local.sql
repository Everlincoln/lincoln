drop schema if exists simpleapp;
create schema simpleapp;
use simpleapp;

CREATE TABLE `people` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `room` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO people VALUES(123,"Lee","L168");
INSERT INTO people VALUES(822,"Mike","L022");
INSERT INTO people VALUES(719,"Pen","L003"); 

