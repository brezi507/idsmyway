-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: ids_database
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ids_alerts`
--

DROP TABLE IF EXISTS `ids_alerts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ids_alerts` (
  `alert_id` int(11) NOT NULL AUTO_INCREMENT,
  `alert_name` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `severity` varchar(255) NOT NULL,
  `criticality` varchar(255) NOT NULL,
  `reporter_module` varchar(64) NOT NULL,
  `alert_details` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`alert_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ids_alerts`
--

LOCK TABLES `ids_alerts` WRITE;
/*!40000 ALTER TABLE `ids_alerts` DISABLE KEYS */;
/*!40000 ALTER TABLE `ids_alerts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ids_audit`
--

DROP TABLE IF EXISTS `ids_audit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ids_audit` (
  `audit_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) NOT NULL,
  `logon_status` varchar(255) NOT NULL,
  `audit_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `audit_xapikey` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`audit_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ids_audit`
--

LOCK TABLES `ids_audit` WRITE;
/*!40000 ALTER TABLE `ids_audit` DISABLE KEYS */;
INSERT INTO `ids_audit` VALUES (1,'catalin','succes','2018-03-27 20:40:01','47b9c056-af67-406d-b690-a2840de63779'),(2,'catalin','succes','2018-03-27 20:40:03','47b9c056-af67-406d-b690-a2840de63779'),(3,'anonim','failed','2018-03-27 20:40:25',NULL),(4,'anonim','failed','2018-03-27 20:40:54','47b9c056-af67-'),(5,'catalin','succes','2018-03-27 20:41:04','47b9c056-af67-406d-b690-a2840de63779');
/*!40000 ALTER TABLE `ids_audit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ids_roles`
--

DROP TABLE IF EXISTS `ids_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ids_roles` (
  `role_id` int(11) NOT NULL AUTO_INCREMENT,
  `role_name` varchar(255) NOT NULL,
  `user_role` varchar(64) NOT NULL,
  `details` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ids_roles`
--

LOCK TABLES `ids_roles` WRITE;
/*!40000 ALTER TABLE `ids_roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `ids_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ids_users`
--

DROP TABLE IF EXISTS `ids_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ids_users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) NOT NULL,
  `user_key` varchar(255) NOT NULL,
  `user_role` varchar(64) NOT NULL,
  `user_details` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ids_users`
--

LOCK TABLES `ids_users` WRITE;
/*!40000 ALTER TABLE `ids_users` DISABLE KEYS */;
/*!40000 ALTER TABLE `ids_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modules_inventory`
--

DROP TABLE IF EXISTS `modules_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `modules_inventory` (
  `module_id` int(11) NOT NULL AUTO_INCREMENT,
  `module_name` varchar(255) NOT NULL,
  `owner` varchar(255) NOT NULL,
  `type` varchar(64) NOT NULL,
  `status` varchar(64) DEFAULT NULL,
  `deployed` date NOT NULL,
  `started` date DEFAULT NULL,
  `last_seen` date DEFAULT NULL,
  `details` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`module_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modules_inventory`
--

LOCK TABLES `modules_inventory` WRITE;
/*!40000 ALTER TABLE `modules_inventory` DISABLE KEYS */;
/*!40000 ALTER TABLE `modules_inventory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-27 23:52:43
