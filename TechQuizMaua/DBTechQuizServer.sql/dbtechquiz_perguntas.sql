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
-- Table structure for table `perguntas`
--

DROP TABLE IF EXISTS `perguntas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `perguntas` (
  `idPergunta` int(11) NOT NULL AUTO_INCREMENT,
  `idJogo` int(11) NOT NULL,
  `Pergunta` varchar(500) NOT NULL,
  PRIMARY KEY (`idPergunta`),
  KEY `perguntas_ibfk_1` (`idJogo`),
  CONSTRAINT `perguntas_ibfk_1` FOREIGN KEY (`idJogo`) REFERENCES `jogo` (`idJogo`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perguntas`
--

LOCK TABLES `perguntas` WRITE;
/*!40000 ALTER TABLE `perguntas` DISABLE KEYS */;
INSERT INTO `perguntas` VALUES (1,1,'Qual é a sintaxe correta para declarar uma lista em Python?'),(2,1,'Qual é o operador utilizado em Python para concatenar duas strings?'),(3,1,'Qual é a diferença entre uma tupla e uma lista em Python?'),(4,1,'Qual é a sintaxe correta para criar uma função em Python?'),(5,1,'Qual é a função utilizada em Python para imprimir na tela?'),(6,1,'Qual é a diferença entre um método e uma função em Python?'),(7,1,'Qual é a função utilizada em Python para ler dados do usuário?'),(8,1,'Qual é a estrutura de controle utilizada em Python para iterar sobre uma lista?'),(9,1,'Qual é a sintaxe correta para abrir um arquivo em Python?'),(10,1,'Qual é a função utilizada em Python para obter o comprimento de uma lista?'),(11,2,'Qual é o método utilizado em Java para imprimir na tela?'),(12,2,'Qual é a diferença entre uma classe abstrata e uma interface em Java?'),(13,2,'Qual é o operador utilizado em Java para incrementar uma variável em 1?'),(14,2,'Qual é a estrutura de controle utilizada em Java para iterar sobre uma lista?'),(15,2,'Qual é o método utilizado em Java para ler dados do usuário?'),(16,2,'Qual é a diferença entre uma variável local e uma variável de instância em Java?'),(17,2,'Qual é o método utilizado em Java para converter uma string em um número inteiro?'),(18,2,'Qual é a sintaxe correta para criar um objeto em Java?'),(19,2,'Qual é a diferença entre um array e um ArrayList em Java?'),(20,2,'Qual é a classe utilizada em Java para manipular datas e horas?'),(31,3,'O que é uma classe em modelagem orientada a objetos?'),(32,3,'Qual é o princípio da modelagem orientada a objetos que indica que uma classe deve ter apenas uma responsabilidade?'),(33,3,'O que é herança em modelagem orientada a objetos?'),(34,3,'O que é encapsulamento em modelagem orientada a objetos?'),(35,3,'O que é polimorfismo em modelagem orientada a objetos?'),(36,3,'Qual é o termo usado para descrever a relação \"é um\" entre classes em modelagem orientada a objetos?'),(37,3,'Qual é o termo usado para descrever a relação \"tem um\" entre classes em modelagem orientada a objetos?'),(38,3,'Qual é o termo usado para descrever a relação \"parte de\" entre classes em modelagem orientada a objetos?'),(39,3,'O que é uma interface em modelagem orientada a objetos?'),(40,3,'O que é sobrecarga de métodos em modelagem orientada a objetos?'),(41,4,'Qual é o comando utilizado em MySQL para criar uma nova tabela?'),(42,4,'Qual é o comando utilizado em MySQL para adicionar uma nova coluna em uma tabela existente?'),(43,4,'Qual é o comando utilizado em MySQL para selecionar todos os registros de uma tabela?'),(44,4,'Qual é o comando utilizado em MySQL para selecionar apenas registros únicos de uma tabela?'),(45,4,'Qual é o comando utilizado em MySQL para ordenar os registros de uma tabela em ordem crescente?'),(46,4,'Qual é o comando utilizado em MySQL para filtrar registros de uma tabela com base em uma condição?'),(47,4,'Qual é o comando utilizado em MySQL para agrupar registros com base em uma coluna específica?'),(48,4,'Qual é o tipo de dados utilizado em MySQL para armazenar valores de data e hora?'),(49,4,'Qual é o comando utilizado em MySQL para excluir registros de uma tabela?'),(50,4,'Qual é o comando utilizado em MySQL para atualizar registros de uma tabela com base em uma condição?');
/*!40000 ALTER TABLE `perguntas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-31  0:30:16
