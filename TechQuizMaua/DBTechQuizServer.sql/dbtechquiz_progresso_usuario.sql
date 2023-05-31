-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: mysql246.umbler.com    Database: dbtechquiz
-- ------------------------------------------------------
-- Server version	5.7.40

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
-- Table structure for table `progresso_usuario`
--

DROP TABLE IF EXISTS `progresso_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `progresso_usuario` (
  `idProgresso` int(11) NOT NULL AUTO_INCREMENT,
  `idJogo` int(11) NOT NULL,
  `idUser` int(11) NOT NULL,
  `progresso` decimal(5,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`idProgresso`),
  KEY `progresso_usuario_ibfk_1` (`idJogo`),
  KEY `progresso_usuario_ibfk_2` (`idUser`),
  CONSTRAINT `progresso_usuario_ibfk_1` FOREIGN KEY (`idJogo`) REFERENCES `jogo` (`idJogo`) ON DELETE CASCADE,
  CONSTRAINT `progresso_usuario_ibfk_2` FOREIGN KEY (`idUser`) REFERENCES `usuario` (`idUser`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `progresso_usuario`
--

LOCK TABLES `progresso_usuario` WRITE;
/*!40000 ALTER TABLE `progresso_usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `progresso_usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-31  0:30:15
