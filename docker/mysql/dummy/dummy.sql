-- MariaDB dump 10.19  Distrib 10.10.2-MariaDB, for osx10.17 (x86_64)
--
-- Host: 127.0.0.1    Database: around
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.22.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `banner`
--
use around;
DROP TABLE IF EXISTS `banner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `banner` (
  `id` int NOT NULL AUTO_INCREMENT,
  `image` varchar(255) NOT NULL,
  `link` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banner`
--

LOCK TABLES `banner` WRITE;
/*!40000 ALTER TABLE `banner` DISABLE KEYS */;
/*!40000 ALTER TABLE `banner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES
(1,'운동');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chat`
--

DROP TABLE IF EXISTS `chat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chat` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` int NOT NULL,
  `user_id` int NOT NULL,
  `promise_id` int NOT NULL,
  `time` datetime NOT NULL,
  `content` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `promise_id` (`promise_id`),
  CONSTRAINT `chat_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `chat_ibfk_2` FOREIGN KEY (`promise_id`) REFERENCES `promise` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat`
--

LOCK TABLES `chat` WRITE;
/*!40000 ALTER TABLE `chat` DISABLE KEYS */;
/*!40000 ALTER TABLE `chat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evaluation`
--

DROP TABLE IF EXISTS `evaluation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `evaluation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `evaluator` int NOT NULL,
  `evaluated_user` int NOT NULL,
  `promise_id` int NOT NULL,
  `content` varchar(255) NOT NULL,
  `star` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `evaluator` (`evaluator`),
  KEY `evaluated_user` (`evaluated_user`),
  KEY `promise_id` (`promise_id`),
  CONSTRAINT `evaluation_ibfk_1` FOREIGN KEY (`evaluator`) REFERENCES `user` (`id`),
  CONSTRAINT `evaluation_ibfk_2` FOREIGN KEY (`evaluated_user`) REFERENCES `user` (`id`),
  CONSTRAINT `evaluation_ibfk_3` FOREIGN KEY (`promise_id`) REFERENCES `promise` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation`
--

LOCK TABLES `evaluation` WRITE;
/*!40000 ALTER TABLE `evaluation` DISABLE KEYS */;
/*!40000 ALTER TABLE `evaluation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notification`
--

DROP TABLE IF EXISTS `notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notification` (
  `id` int NOT NULL AUTO_INCREMENT,
  `message` varchar(255) NOT NULL,
  `type` int NOT NULL,
  `status` int NOT NULL,
  `time` datetime NOT NULL,
  `user_id` int NOT NULL,
  `promise_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `promise_id` (`promise_id`),
  CONSTRAINT `notification_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `notification_ibfk_2` FOREIGN KEY (`promise_id`) REFERENCES `promise` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification`
--

LOCK TABLES `notification` WRITE;
/*!40000 ALTER TABLE `notification` DISABLE KEYS */;
INSERT INTO `notification` VALUES
(1,'메세지입니다.',1,1,'2022-12-28 13:05:38',1,NULL),
(2,'메세지입니다.',1,1,'2022-12-28 13:05:42',1,NULL);
/*!40000 ALTER TABLE `notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promise`
--

DROP TABLE IF EXISTS `promise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promise` (
  `id` int NOT NULL AUTO_INCREMENT,
  `owner` int NOT NULL,
  `category_id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `detail` varchar(255) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `address` varchar(255) NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `image` varchar(255) NOT NULL,
  `max_people` int NOT NULL,
  `status` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `owner` (`owner`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `promise_ibfk_1` FOREIGN KEY (`owner`) REFERENCES `user` (`id`),
  CONSTRAINT `promise_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promise`
--

LOCK TABLES `promise` WRITE;
/*!40000 ALTER TABLE `promise` DISABLE KEYS */;
INSERT INTO `promise` VALUES
(1,1,1,'이 약속은 내가 차지한다','크리스마스',33.3,33.3,'광진구','2022-12-23 11:34:06','2022-12-23 11:34:06','somethign',2,1),
(3,1,1,'우아아아아아아','이것저것',48.3,38.2,'서울','2022-12-16 13:00:00','2022-12-16 15:00:00','image',8,-1),
(4,1,1,'test','test',111,111,'test','2022-12-29 14:25:57','2022-12-29 14:25:57','test',4,0),
(5,3,1,'마라샹궈 먹으러 갈 사람~!','마라샹궈가 먹고 싶다...',37.5602,127.041,'맨즈필드','2023-02-10 18:39:50','2023-02-10 20:00:00','마라샹궈.jpg',4,0),
(6,3,1,'마라샹궈 먹자','배고파',37.5602,127.041,'맨즈필드','2023-02-10 18:43:50','2023-02-10 20:00:00','마라샹궈.jpg',4,0),
(7,3,1,'중국어 공부할 사람','뒤에서 누가 중국어를 쓰고 있어',37.5602,127.041,'맨즈필드','2023-02-10 18:43:50','2023-02-10 20:00:00','중국어.jpg',4,0),
(8,3,1,'중국어 공부할 사람','뒤에서 누가 중국어를 쓰고 있어',37.5602,127.041,'맨즈필드','2023-02-10 18:43:50','2023-02-10 20:00:00','중국어.jpg',4,0),
(9,3,1,'코딩합시다','안드로이드 개발 중',37.5602,127.041,'맨즈필드','2023-02-10 18:43:50','2023-02-10 20:00:00','안드로이드.jpg',2,1),
(10,3,1,'이제 아이디어가 없어','건우야 디자인 빨리하자',37.5602,127.041,'맨즈필드','2023-02-10 18:43:50','2023-02-10 20:00:00','윤건우.jpg',10,1),
(11,3,1,'테니스','테니스 치고 싶다.',37.5602,127.041,'맨즈필드','2023-02-10 18:43:50','2023-02-10 20:00:00','테니스.jpg',4,1),
(12,3,1,'약과','약과 맛있다',37.5602,127.041,'맨즈필드','2023-02-10 18:43:50','2023-02-10 20:00:00','약과.jpg',15,1);
/*!40000 ALTER TABLE `promise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kakao_id` int NOT NULL,
  `nickname` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `age` int NOT NULL,
  `gender` int NOT NULL,
  `introduction` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `kakao_id` (`kakao_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES
(1,1,'황진하','imageurl',27,0,'진하입니다.'),
(2,12345,'jiwon','jiwon.image',23,1,'hello'),
(3,123,'202','image',25,1,'hihi');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userpromise`
--

DROP TABLE IF EXISTS `userpromise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userpromise` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `promise_id` int NOT NULL,
  `is_auth` tinyint(1) NOT NULL,
  `status` int NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `promise_id` (`promise_id`),
  CONSTRAINT `userpromise_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `userpromise_ibfk_2` FOREIGN KEY (`promise_id`) REFERENCES `promise` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userpromise`
--

LOCK TABLES `userpromise` WRITE;
/*!40000 ALTER TABLE `userpromise` DISABLE KEYS */;
INSERT INTO `userpromise` VALUES
(1,2,3,0,1,'2022-12-29 10:00:00','2022-12-29 13:00:00'),
(2,1,1,0,2,'2022-12-29 23:06:11','2022-12-29 23:06:11');
/*!40000 ALTER TABLE `userpromise` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-10 19:04:50
