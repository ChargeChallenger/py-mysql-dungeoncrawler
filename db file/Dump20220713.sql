CREATE DATABASE  IF NOT EXISTS `dungeon` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dungeon`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: dungeon
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bosses`
--

DROP TABLE IF EXISTS `bosses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bosses` (
  `id_boss` int NOT NULL AUTO_INCREMENT,
  `boss_name` varchar(25) DEFAULT NULL,
  `boss_body` int DEFAULT NULL,
  `boss_dexterity` int DEFAULT NULL,
  `id_weapon` int DEFAULT NULL,
  `is_dead` enum('yes','no') DEFAULT NULL,
  PRIMARY KEY (`id_boss`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bosses`
--

LOCK TABLES `bosses` WRITE;
/*!40000 ALTER TABLE `bosses` DISABLE KEYS */;
INSERT INTO `bosses` VALUES (1,'Босс',15,15,3,'yes'),(2,'Николай',9,8,4,'yes'),(3,'убица',7,10,9,'no');
/*!40000 ALTER TABLE `bosses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enemies`
--

DROP TABLE IF EXISTS `enemies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enemies` (
  `id_enemy` int NOT NULL AUTO_INCREMENT,
  `enemy_name` varchar(25) DEFAULT NULL,
  `enemy_body` int DEFAULT NULL,
  `enemy_dexterity` int DEFAULT NULL,
  `id_weapon` int DEFAULT NULL,
  `floor_number` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_enemy`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enemies`
--

LOCK TABLES `enemies` WRITE;
/*!40000 ALTER TABLE `enemies` DISABLE KEYS */;
INSERT INTO `enemies` VALUES (1,'Скелет',5,5,1,'1'),(2,'Скелет',7,7,2,'2'),(3,'Скелет',10,10,3,'3'),(4,'Виталий',1,1,5,'1'),(5,'Гном',1,1,6,'1'),(6,'Джедай',8,7,7,'3'),(7,'Мелкий',1,1,8,'1');
/*!40000 ALTER TABLE `enemies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weapons`
--

DROP TABLE IF EXISTS `weapons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `weapons` (
  `id_weapon` int NOT NULL AUTO_INCREMENT,
  `weapon_type` varchar(25) DEFAULT NULL,
  `weapon_name` varchar(25) DEFAULT NULL,
  `weapon_damage` int DEFAULT NULL,
  `weapon_speed` int DEFAULT NULL,
  `weapon_floor` int DEFAULT NULL,
  PRIMARY KEY (`id_weapon`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weapons`
--

LOCK TABLES `weapons` WRITE;
/*!40000 ALTER TABLE `weapons` DISABLE KEYS */;
INSERT INTO `weapons` VALUES (1,'Меч','Остроконечный',2,4,1),(2,'Кинжал','Перо под ребро',1,6,2),(3,'Топор','Сокрушитель',3,2,3),(4,'Меч','Хоба',9,8,3),(5,'Топор','Сломанное ребро',3,2,1),(6,'Кинжал','',1,6,1),(7,'Кинжал','Перо под ребро',2,6,3),(8,'Кинжал','Тык',1,6,1),(9,'Кинжал','кинжалище',8,6,3);
/*!40000 ALTER TABLE `weapons` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-13 22:17:26
