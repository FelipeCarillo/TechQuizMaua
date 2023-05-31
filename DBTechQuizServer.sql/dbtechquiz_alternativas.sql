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
-- Table structure for table `alternativas`
--

DROP TABLE IF EXISTS `alternativas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alternativas` (
  `idResposta` int(11) NOT NULL AUTO_INCREMENT,
  `idPergunta` int(11) NOT NULL,
  `Alternativa` varchar(100) NOT NULL,
  `isRight` tinyint(1) NOT NULL,
  PRIMARY KEY (`idResposta`),
  KEY `alternativas_ibfk_1` (`idPergunta`),
  CONSTRAINT `alternativas_ibfk_1` FOREIGN KEY (`idPergunta`) REFERENCES `perguntas` (`idPergunta`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=265 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alternativas`
--

LOCK TABLES `alternativas` WRITE;
/*!40000 ALTER TABLE `alternativas` DISABLE KEYS */;
INSERT INTO `alternativas` VALUES (1,1,'lista = [1, 2, 3]',1),(2,1,'lista = {1, 2, 3}',0),(3,1,'lista = (1, 2, 3)',0),(4,1,'lista = \"1, 2, 3\"',0),(5,2,'+',1),(6,2,'*',0),(7,2,'/',0),(8,2,'-',0),(9,3,'As tuplas são imutáveis e as listas são mutáveis',1),(10,3,'As tuplas são mutáveis e as listas são imutáveis',0),(11,3,'As tuplas são ordenadas e as listas são desordenadas',0),(12,3,'Não há diferença entre as tuplas e as listas',0),(13,4,'def minha_funcao():',1),(14,4,'minha_funcao():',0),(15,4,'function minha_funcao():',0),(16,4,'function minha_funcao()',0),(17,5,'print()',1),(18,5,'print(f\"\")',1),(19,5,'println()',0),(20,5,'write()',0),(21,6,'Os métodos são definidos dentro de uma classe e as funções não.',1),(22,6,'As funções são definidas dentro de uma classe e os métodos não',0),(23,6,'Não há diferença entre métodos e funções em Python.',0),(24,6,'Os métodos e as funções são ambos definidos dentro de uma classe',0),(25,7,'input()',1),(26,7,'read()',0),(27,7,'get()',0),(28,7,'scanf()',0),(29,8,'for',1),(30,8,'while',0),(31,8,'repeat',0),(32,8,'foreach',0),(33,9,'open(\"meu_arquivo.txt\")',0),(34,9,'open(\"meu_arquivo.txt\", \"w\")',0),(35,9,'open(\"meu_arquivo.txt\", \"r\")',1),(36,9,'open(\"meu_arquivo.txt\", \"a\")',0),(37,10,'len()',1),(38,10,'count()',0),(39,10,'length()',0),(40,10,'size()',0),(41,11,'System.out.println()',1),(42,11,'System.out.printf()',0),(43,11,'System.out.print()',0),(44,11,'System.out.write()',0),(45,12,'As classes abstratas podem ser instanciadas e as interfaces não podem.',1),(46,12,'As interfaces não podem ter métodos e as classes abstratas podem.',0),(47,12,'As interfaces podem ter atributos e as classes abstratas não podem.',0),(48,12,'As classes abstratas podem ter construtores e as interfaces não podem.',0),(49,13,'++',1),(50,13,'+=',0),(51,13,'/=',0),(52,13,'--',0),(53,14,'for',1),(54,14,'while',0),(55,14,'repeat',0),(56,14,'foreach',0),(57,15,'System.in()',1),(58,15,'System.read()',0),(59,15,'System.console()',0),(60,15,'System.getInput()',0),(61,16,'As variáveis locais só podem ser acessadas dentro de um método e as variáveis de instância podem ser',1),(62,16,'As variáveis locais são definidas dentro de um método e as variáveis de instância são definidas fora',0),(63,16,'As variáveis locais são definidas fora de uma classe e as variáveis de instância são definidas dentr',0),(64,16,' Não há diferença entre variáveis locais e de instância em Java',0),(65,17,'Integer.parseInt()',1),(66,17,'String.toInt()',0),(67,17,'String.parseInt()',0),(68,17,'Integer.valueOf()',0),(69,18,'new objeto();',1),(70,18,'objeto.new();',0),(71,18,'new objeto;',0),(72,18,'objeto.new;',0),(73,19,'Os arrays têm tamanho fixo e os ArrayLists têm tamanho dinâmico.',1),(74,19,'Os arrays podem ter valores de diferentes tipos e os ArrayLists não podem.',0),(75,19,'Os arrays são mais eficientes em termos de memória do que os ArrayLists.',0),(76,19,' Não há diferença entre arrays e ArrayLists em Java.',0),(77,20,'Calendar',1),(78,20,'Date',0),(79,20,'Time',0),(80,20,'DateTime',0),(121,31,'Um modelo de um objeto',1),(122,31,'Um objeto',0),(123,31,'Um tipo de dado',0),(124,31,'Uma estrutura de dados',0),(125,32,'Coesão',1),(126,32,'Encapsulamento',0),(127,32,'Abstração',0),(128,32,'Herança',0),(129,33,'Uma forma de estender uma classe existente',1),(130,33,'Uma forma de agrupar objetos relacionados',0),(131,33,'Uma forma de encapsular comportamentos',0),(132,33,'Uma forma de definir interfaces',0),(133,34,'Uma forma de ocultar a implementação de uma classe',1),(134,34,'Uma forma de agrupar objetos relacionados',0),(135,34,'Uma forma de estender uma clse existente',0),(136,34,'Uma forma de definir interfaces',0),(137,35,'Uma forma de tratar objetos de diferentes classes de forma uniforme',1),(138,35,'Uma forma de definir interfaces',0),(139,35,'Uma forma de estender uma classe existente',0),(140,35,'Uma forma de agrupar objetos relacionados',0),(141,36,'Herança',1),(142,36,'Agregação',0),(143,36,'Composição',0),(144,36,'Associação',0),(145,37,'Agregação',1),(146,37,'Composição',0),(147,37,'Herança',0),(148,37,'Associação',0),(149,38,'Composição',1),(150,38,'Agregação',0),(151,38,'Herança',0),(152,38,'Associação',0),(153,39,'Um contrato que define um conjunto de métodos',1),(154,39,'Uma classe abstrata que define métodos',0),(155,39,'Um objeto que implementa um conjunto de métodos',0),(156,39,'Uma forma de estender uma classe existente',0),(157,40,'Uma forma de definir vários métodos com o mesmo nome, mas com parâmetros diferentes',1),(158,40,'Uma forma de ocultar a implementação de uma classe',0),(159,40,'Uma forma de agrupar objetos relacionados',0),(160,40,'Uma forma de estender uma classe existente',0),(161,41,'CREATE TABLE',1),(162,41,'CREATE DATABASE',0),(163,41,'CREATE COLUMN',0),(164,41,'CREATE INDEX',0),(165,42,'ADD COLUMN',1),(166,42,'ALTER COLUMN',0),(167,42,'UPDATE COLUMN',0),(168,42,'MODIFY COLUMN',0),(169,43,'SELECT *',1),(170,43,'SELECT ALL',0),(171,43,'SELECT ROWS',0),(172,43,'SELECT EVERYTHING',0),(173,44,'SELECT DISTINCT',1),(174,44,'SELECT ALL',0),(175,44,'SELECT UNIQUE',0),(176,44,'SELECT ONLY',0),(177,45,'ORDER ASC',1),(178,45,'SORT ASC',0),(179,45,'GROUP ASC',0),(180,45,'ASC ORDER',0),(181,46,'SELECT WHERE',1),(182,46,'SELECT FILTER',0),(183,46,'SELECT SEARCH',0),(184,46,'SELECT IF',0),(185,47,'GROUP BY',1),(186,47,'SORT BY',0),(187,47,'ORDER BY',0),(188,47,'FILTER BY',0),(189,48,'DATE',1),(190,48,'INTEGER',0),(191,48,'FLOAT',0),(192,48,'VARCHAR',0),(193,49,'DELETE',1),(194,49,'DROP',0),(195,49,'REMOVE',0),(196,49,'ERASE',0),(197,40,'UPDATE',1),(198,40,'MODIFY',0),(199,40,'CHANGE',0),(200,40,'ALTER',0);
/*!40000 ALTER TABLE `alternativas` ENABLE KEYS */;
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
