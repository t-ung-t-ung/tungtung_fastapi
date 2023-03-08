use around;

DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `category` WRITE;
INSERT INTO `category` VALUES
(0, '기타'),
(1, '운동'),
(2, '게임'),
(3, '영화'),
(4, '음악'),
(5, '미술'),
(6, '음식'),
(7, '공연'),
(8, '공부'),
(9, '여행');

UNLOCK TABLES;