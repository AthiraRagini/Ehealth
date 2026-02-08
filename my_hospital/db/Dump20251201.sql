-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: hospi
-- ------------------------------------------------------
-- Server version	8.0.42

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add appointment',7,'add_appointment'),(26,'Can change appointment',7,'change_appointment'),(27,'Can delete appointment',7,'delete_appointment'),(28,'Can view appointment',7,'view_appointment'),(29,'Can add patient',8,'add_patient'),(30,'Can change patient',8,'change_patient'),(31,'Can delete patient',8,'delete_patient'),(32,'Can view patient',8,'view_patient'),(33,'Can add doctor',9,'add_doctor'),(34,'Can change doctor',9,'change_doctor'),(35,'Can delete doctor',9,'delete_doctor'),(36,'Can view doctor',9,'view_doctor'),(37,'Can add payment',10,'add_payment'),(38,'Can change payment',10,'change_payment'),(39,'Can delete payment',10,'delete_payment'),(40,'Can view payment',10,'view_payment'),(41,'Can add health data',11,'add_healthdata'),(42,'Can change health data',11,'change_healthdata'),(43,'Can delete health data',11,'delete_healthdata'),(44,'Can view health data',11,'view_healthdata');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$W4KZe49MpcfQArVSQUPUmF$i9Rv/a4XXbPhmDrvJx0GOVH4p/ry/a2MsyWBumARKDY=','2025-12-01 01:12:49.891850',1,'aswin1','','','aswinkv1@gmail.com',1,1,'2025-11-23 14:11:08.446038'),(2,'pbkdf2_sha256$600000$9nyljsw1VlKlxhiNUJorzS$Z91/a5P0XF887kJNCfisPky8r9JdCBOPuMzk2LT70w0=','2025-11-23 14:17:25.000000',0,'aswinkv@123','aswin','kv','aswinkv487@gmail.com',0,1,'2025-11-23 14:15:48.000000'),(3,'pbkdf2_sha256$600000$g3oFElFplzVyCS1msrN1M9$v0ll/SZbs3nIsI0FBnLnifX2ZkRUpbwIyh4FzL21tqo=','2025-11-23 14:32:14.926848',0,'jon','','','swswdswdwd123@gmail.com',0,1,'2025-11-23 14:31:51.076053'),(5,'pbkdf2_sha256$600000$pm4CoBfMJ8JipvakjtsEsj$NiDoEnE+rBVlS8OwVllIQdhXLXgLhXTZNfv01h79zTk=','2025-11-23 15:22:01.456332',0,'soj','','','swswdswdwd123@gmail.com',0,1,'2025-11-23 15:21:50.658753'),(6,'pbkdf2_sha256$600000$FcMP0nKMHAfrrPx3UCFjeD$fVaXASpy/VkllHHd6iH4/j4uYp2jPPCV59RlVk4LUMg=',NULL,0,'aju123456@123','','','',0,1,'2025-11-25 02:43:24.710390'),(7,'pbkdf2_sha256$600000$G3bLdkZ68SKKVa9L1UzHXz$lBVAJjxsYSgwBCG145I25H/iZLj4yxM3wOfnTJrxTPk=',NULL,0,'aswin12','','','swswdswdwd123@gmail.com',0,1,'2025-11-25 02:47:07.243257'),(8,'pbkdf2_sha256$600000$LCpdBMta2YQrowPiPm9Hgo$0dFcm6THYsPuVRk6cVdmoKHF9srLT603OzqRo0qFSfA=','2025-12-01 01:11:58.718864',0,'aswin123','','','ererere@gmail.com',0,1,'2025-11-25 02:52:37.892384'),(9,'pbkdf2_sha256$600000$7PZyTLbjV4jcFzPi8AgLCD$O6C5jb5tHO6waPCtfJErmOHVy0pmCi0B4YMhO9Fnr48=',NULL,0,'amal@123','','','',0,1,'2025-11-25 04:55:29.285146'),(10,'pbkdf2_sha256$600000$eyimCSCDugENlAe1SJCTqR$TT+vQuMj57M2MmFNAQ91F3cp2CBWVnT7IvhBBXL0hzY=','2025-11-26 05:05:42.659208',0,'sony','','','swswdswdwd123@gmail.com',0,1,'2025-11-26 05:05:32.333528'),(11,'pbkdf2_sha256$600000$75w0IXLv6f1yxoeMGJGeyv$QwjTn2FmUGm8r2mjXbsU/gZ1/L5NFhmsCyXie+R5zAI=','2025-11-26 05:08:49.064256',0,'john kuruvila','','','swswdswdwd123@gmail.com',0,1,'2025-11-26 05:08:33.273701'),(12,'pbkdf2_sha256$600000$m7ZiIkivBOhi1NPty4PCu3$1PkgEFt3g34cfEAbejFNQVd2XVcDU8WAsp59Y5P3ZQE=','2025-11-27 02:42:49.242846',0,'ron','','','swswdswdwd123@gmail.com',0,1,'2025-11-26 05:15:36.172830'),(13,'pbkdf2_sha256$600000$b4SrhwGq1pbyfwbASUCfAy$OU+LYymDB+PZBn1hEuuKn3h6FRMKl4nrjdu/BqZJRMs=','2025-11-26 05:40:28.611314',0,'raju','','','swswdswdwd123@gmail.com',0,1,'2025-11-26 05:40:20.772574'),(14,'pbkdf2_sha256$600000$lwAc7Bo4jUE1Y2KEmybbqP$lIfNX//NTXpmkS9yyUoR7i+JYJ7NDpw9tqUwV/GAnu4=','2025-11-26 05:50:39.926522',0,'antony','','','swswdswdwd123@gmail.com',0,1,'2025-11-26 05:50:26.199330'),(15,'pbkdf2_sha256$600000$eRZgLF34NWGkc5cYt8K52X$NC0Q8JHG6UhVynjfIgjLcAcmHBFSXKrqx7JH0YNoQR8=','2025-11-26 07:04:08.942302',0,'siva','','','swswdswdwd123@gmail.com',0,1,'2025-11-26 07:01:47.364945'),(16,'pbkdf2_sha256$600000$0gF5oEcOaTs2BTdtmInvqJ$A2CE+LD493w2i725f85teb6YgbHdXp8aj8V4Ao3vCiw=','2025-12-01 01:12:29.376941',0,'rakhav','','','swswdswdwd123@gmail.com',0,1,'2025-11-26 07:11:59.399608'),(17,'pbkdf2_sha256$600000$tO8dqlm8kLFFgGvW9QSg1d$nsHZ7umsroASXZZ3jlO7AbLgf9oPvsDnUgafnkabWsM=','2025-11-26 07:13:08.022264',0,'sachin','','','swswdswdwd123@gmail.com',0,1,'2025-11-26 07:13:00.518226'),(18,'pbkdf2_sha256$600000$9GCTFEhFhQYbhOrHCAkyQT$poo6DWmsyQarbCRD6hX8kduqYBBMdd41OV3EjwUe/WI=','2025-11-28 07:16:54.693283',0,'samuel','','','swswdswdwd123@gmail.com',0,1,'2025-11-26 07:25:31.328186'),(19,'pbkdf2_sha256$600000$Gin4PNoJIXVzaCpTCVN55O$qj3qyqa1p1vNa9Cswss0stmzizclYO3Ty87XYBLbbfk=','2025-11-27 02:41:42.648853',0,'jony','','','swswdswdwd123@gmail.com',0,1,'2025-11-27 02:41:30.451876'),(20,'pbkdf2_sha256$600000$ZMGqIzQcKI8Q4fWHhAPlRs$szGPFAByTH1Ln1xeTd51rDuNZC6Wv/otNoZA1A0cgrw=','2025-11-28 06:39:31.520339',0,'leo','','','swswdswdwd123@gmail.com',0,1,'2025-11-28 04:54:21.250942');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-11-25 02:43:26.246851','6','aju123456@123',1,'[{\"added\": {}}]',4,1),(2,'2025-11-25 02:43:32.436842','4','aju123456@123',1,'[{\"added\": {}}]',9,1),(3,'2025-11-25 02:59:17.595690','2','aswinkv@123',2,'[{\"changed\": {\"fields\": [\"Username\", \"First name\", \"Last name\"]}}]',4,1),(4,'2025-11-25 02:59:59.837446','6','aswinkv@123',1,'[{\"added\": {}}]',9,1),(5,'2025-11-25 03:02:54.272324','4','ram27@123',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,1),(6,'2025-11-25 03:03:29.325894','4','ram27@123',3,'',4,1),(7,'2025-11-25 04:55:30.724112','9','amal@123',1,'[{\"added\": {}}]',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'members','appointment'),(9,'members','doctor'),(11,'members','healthdata'),(8,'members','patient'),(10,'members','payment'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-11-20 07:11:40.649508'),(2,'auth','0001_initial','2025-11-20 07:11:41.720076'),(3,'admin','0001_initial','2025-11-20 07:11:41.997173'),(4,'admin','0002_logentry_remove_auto_add','2025-11-20 07:11:42.013173'),(5,'admin','0003_logentry_add_action_flag_choices','2025-11-20 07:11:42.031220'),(6,'contenttypes','0002_remove_content_type_name','2025-11-20 07:11:42.225555'),(7,'auth','0002_alter_permission_name_max_length','2025-11-20 07:11:42.379562'),(8,'auth','0003_alter_user_email_max_length','2025-11-20 07:11:42.437558'),(9,'auth','0004_alter_user_username_opts','2025-11-20 07:11:42.451658'),(10,'auth','0005_alter_user_last_login_null','2025-11-20 07:11:42.552887'),(11,'auth','0006_require_contenttypes_0002','2025-11-20 07:11:42.559889'),(12,'auth','0007_alter_validators_add_error_messages','2025-11-20 07:11:42.578883'),(13,'auth','0008_alter_user_username_max_length','2025-11-20 07:11:42.702907'),(14,'auth','0009_alter_user_last_name_max_length','2025-11-20 07:11:42.877644'),(15,'auth','0010_alter_group_name_max_length','2025-11-20 07:11:42.918223'),(16,'auth','0011_update_proxy_permissions','2025-11-20 07:11:42.936969'),(17,'auth','0012_alter_user_first_name_max_length','2025-11-20 07:11:43.035210'),(18,'sessions','0001_initial','2025-11-20 07:11:43.100827'),(19,'members','0001_initial','2025-11-23 14:09:50.002100'),(20,'members','0002_add_assignment_status','2025-11-28 02:40:20.363972');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('xoz3tqssz9z5zmudcj7ng9nhm2xxfo6n','.eJxVjEEOwiAQRe_C2hCGFoa6dO8ZyAygVA0kpV0Z725JutDtf-_9t_C0rdlvLS1-juIstDj9bkzhmUoH8UHlXmWoZV1mll2RB23yWmN6XQ737yBTy3ttjUl6DJrBMiJaBRDVCDgwArnJTIRwc4l24lB11xBYy6TZkB2U-HwBrMs2dQ:1vNAsg:I6qImkSFIdb1Iw_aLhsFZH5LtXz96m9D6Oz8jEzYY4c','2025-12-07 14:15:58.395912'),('z6htvigxzar9mml7i520cjy9u8c06oyy','.eJxVjMsOwiAURP-FtSGXZ8Gle7-BAPciVUOT0q6M_64kXehuMufMvFiI-1bD3mkNM7IzE4KdfssU84PaIHiP7bbwvLRtnRMfCj9o59cF6Xk53L-DGnv9ro2R3omC4DWVNBUgqb1CspMDKLEQGJdHVAhROUA0UudEyiUy1kr2_gAB5DgH:1vO7lo:Sx_rc295eE9ufrOlpRPkCtXud4dFg7ot1ieH-3Jc4Ms','2025-12-10 05:08:48.832255');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members_appointment`
--

DROP TABLE IF EXISTS `members_appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members_appointment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time(6) DEFAULT NULL,
  `description` longtext NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `doctor_id` bigint NOT NULL,
  `patient_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `members_appointment_doctor_id_e2b41016_fk_members_doctor_id` (`doctor_id`),
  KEY `members_appointment_patient_id_4e4627d4_fk_members_patient_id` (`patient_id`),
  CONSTRAINT `members_appointment_doctor_id_e2b41016_fk_members_doctor_id` FOREIGN KEY (`doctor_id`) REFERENCES `members_doctor` (`id`),
  CONSTRAINT `members_appointment_patient_id_4e4627d4_fk_members_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `members_patient` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members_appointment`
--

LOCK TABLES `members_appointment` WRITE;
/*!40000 ALTER TABLE `members_appointment` DISABLE KEYS */;
INSERT INTO `members_appointment` VALUES (1,'2025-11-25','10:02:00.000000','got a eye injury','confirmed','2025-11-25 02:56:37.455651',4,2),(2,'2026-02-11','11:10:00.000000','','confirmed','2025-11-26 05:07:41.978752',4,3),(4,'2026-12-28','10:12:00.000000','i need to take care of my eye','confirmed','2025-11-26 07:05:15.102547',4,5),(5,'2025-11-26','10:10:00.000000','got neurological problem need urgent treatement','confirmed','2025-11-26 07:15:48.297710',10,6),(6,'2026-02-26','11:11:00.000000','my condition is pathetic so i need pathology','confirmed','2025-11-26 07:27:43.800951',8,7),(7,'2026-02-27','10:18:00.000000','need treatement','confirmed','2025-11-27 04:48:24.261879',10,2),(8,'2026-06-27','10:29:00.000000','','confirmed','2025-11-27 04:59:28.849675',4,2),(9,'2026-06-27','10:52:00.000000','','confirmed','2025-11-27 05:17:26.506830',8,2),(10,'2027-06-27','12:53:00.000000','','confirmed','2025-11-27 05:21:20.462721',11,2),(11,'2026-06-03','12:21:00.000000','','confirmed','2025-11-27 06:49:32.285144',1,2),(12,'2026-11-28','12:29:00.000000','','confirmed','2025-11-27 06:55:40.427799',4,2),(13,'2026-10-27','12:31:00.000000','','confirmed','2025-11-27 06:57:31.687579',10,2),(14,'2028-02-27','13:05:00.000000','','confirmed','2025-11-27 07:31:31.366766',8,2),(15,'2026-10-28','07:35:00.000000','','confirmed','2025-11-28 02:01:17.418468',10,2),(16,'2026-10-28','07:42:00.000000','','rejected','2025-11-28 02:08:17.811702',10,2),(17,'2026-10-28','08:14:00.000000','','confirmed','2025-11-28 02:41:26.203272',10,2),(18,'2026-06-28','08:20:00.000000','','confirmed','2025-11-28 02:46:38.732601',10,2),(19,'2026-10-28','08:24:00.000000','','confirmed','2025-11-28 02:51:20.608175',10,2),(20,'2026-06-28','10:30:00.000000','','confirmed','2025-11-28 04:55:24.888745',10,2),(21,'2026-10-28','12:08:00.000000','','confirmed','2025-11-28 06:32:31.863323',12,2);
/*!40000 ALTER TABLE `members_appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members_doctor`
--

DROP TABLE IF EXISTS `members_doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members_doctor` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `specialization` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `fee` decimal(10,2) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `members_doctor_user_id_526d76c9_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members_doctor`
--

LOCK TABLES `members_doctor` WRITE;
/*!40000 ALTER TABLE `members_doctor` DISABLE KEYS */;
INSERT INTO `members_doctor` VALUES (1,'Skin Care','2333222332',130.00,3),(3,'Skin Care','2333222332',0.00,5),(4,'Eye Care','2333222332',246.00,6),(5,'','',0.00,7),(6,'Skin Care','2333222332',200.00,2),(7,'','',0.00,11),(8,'Pathology','2333222332211',900.00,12),(10,'neurology','2333222332',150.00,16),(11,'cardio','2333222332',100.00,19),(12,'cardio','2333222332',5500.00,20);
/*!40000 ALTER TABLE `members_doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members_healthdata`
--

DROP TABLE IF EXISTS `members_healthdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members_healthdata` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `blood_pressure` varchar(20) NOT NULL,
  `sugar` varchar(20) NOT NULL,
  `pse` varchar(20) NOT NULL,
  `weight` varchar(20) NOT NULL,
  `notes` longtext NOT NULL,
  `date` date NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `patient_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `members_healthdata_patient_id_70c6d4bd_fk_members_patient_id` (`patient_id`),
  CONSTRAINT `members_healthdata_patient_id_70c6d4bd_fk_members_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `members_patient` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members_healthdata`
--

LOCK TABLES `members_healthdata` WRITE;
/*!40000 ALTER TABLE `members_healthdata` DISABLE KEYS */;
INSERT INTO `members_healthdata` VALUES (1,'120/80','100','72/98/60','70','','2025-11-26','2025-11-26 05:06:29.613430',3),(2,'120/80','100','72/98/60','70','','2025-11-26','2025-11-26 07:05:44.227494',5),(3,'120/80','100','72/98/60','70','','2025-11-26','2025-11-26 07:13:24.477019',6),(4,'120/80','100','72/98/60','70','','2025-11-26','2025-11-26 07:25:55.627488',7),(5,'120/80','100','72/98/60','70','','2025-11-28','2025-11-28 06:31:53.559087',2);
/*!40000 ALTER TABLE `members_healthdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members_patient`
--

DROP TABLE IF EXISTS `members_patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members_patient` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `age` int DEFAULT NULL,
  `phone` varchar(20) NOT NULL,
  `assigned_doctor_id` bigint DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `members_patient_assigned_doctor_id_bdde3835_fk_members_doctor_id` (`assigned_doctor_id`),
  CONSTRAINT `members_patient_assigned_doctor_id_bdde3835_fk_members_doctor_id` FOREIGN KEY (`assigned_doctor_id`) REFERENCES `members_doctor` (`id`),
  CONSTRAINT `members_patient_user_id_f09f7d6f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members_patient`
--

LOCK TABLES `members_patient` WRITE;
/*!40000 ALTER TABLE `members_patient` DISABLE KEYS */;
INSERT INTO `members_patient` VALUES (1,2,'2333222332',3,2),(2,NULL,'',12,8),(3,NULL,'',NULL,10),(5,NULL,'',NULL,15),(6,NULL,'',NULL,17),(7,NULL,'',NULL,18);
/*!40000 ALTER TABLE `members_patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members_payment`
--

DROP TABLE IF EXISTS `members_payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members_payment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) NOT NULL,
  `status` varchar(20) NOT NULL,
  `payment_date` datetime(6) NOT NULL,
  `transaction_id` varchar(100) NOT NULL,
  `appointment_id` bigint NOT NULL,
  `doctor_id` bigint NOT NULL,
  `patient_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `members_payment_appointment_id_7873d92e_fk_members_a` (`appointment_id`),
  KEY `members_payment_doctor_id_46eb818d_fk_members_doctor_id` (`doctor_id`),
  KEY `members_payment_patient_id_5b5b6a9f_fk_members_patient_id` (`patient_id`),
  CONSTRAINT `members_payment_appointment_id_7873d92e_fk_members_a` FOREIGN KEY (`appointment_id`) REFERENCES `members_appointment` (`id`),
  CONSTRAINT `members_payment_doctor_id_46eb818d_fk_members_doctor_id` FOREIGN KEY (`doctor_id`) REFERENCES `members_doctor` (`id`),
  CONSTRAINT `members_payment_patient_id_5b5b6a9f_fk_members_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `members_patient` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members_payment`
--

LOCK TABLES `members_payment` WRITE;
/*!40000 ALTER TABLE `members_payment` DISABLE KEYS */;
INSERT INTO `members_payment` VALUES (1,246.00,'paid','2025-11-25 02:56:37.467659','12345678',1,4,2),(2,246.00,'paid','2025-11-26 05:07:41.987878','12345678',2,4,3),(4,246.00,'paid','2025-11-26 07:05:15.112554','12345678',4,4,5),(5,150.00,'paid','2025-11-26 07:15:48.304713','12345678',5,10,6),(6,900.00,'paid','2025-11-26 07:27:43.812941','12345678',6,8,7),(7,150.00,'paid','2025-11-27 04:48:24.277878','12345678',7,10,2),(8,246.00,'paid','2025-11-27 04:59:28.863711','12345678',8,4,2),(9,900.00,'paid','2025-11-27 05:17:26.521346','A7808AF77784',9,8,2),(10,100.00,'paid','2025-11-27 05:21:20.476742','19CCD4473D69',10,11,2),(11,130.00,'paid','2025-11-27 06:49:32.296149','238C09EFE45E',11,1,2),(12,246.00,'paid','2025-11-27 06:55:40.438917','C60EE7AF7AE8',12,4,2),(13,150.00,'paid','2025-11-27 06:57:31.696643','866702936F2C',13,10,2),(14,900.00,'paid','2025-11-27 07:31:31.377762','C3A305D484D1',14,8,2),(15,150.00,'paid','2025-11-28 02:01:17.433041','7D19D78FD295',15,10,2),(16,150.00,'pending','2025-11-28 02:08:17.923882','',16,10,2),(17,150.00,'paid','2025-11-28 02:41:26.214962','280BF61D1553',17,10,2),(18,150.00,'paid','2025-11-28 02:46:38.745504','D261512F42D6',18,10,2),(19,150.00,'paid','2025-11-28 02:51:20.622692','DDCF3EDA709F',19,10,2),(20,150.00,'paid','2025-11-28 04:55:24.900285','5743438440BA',20,10,2),(21,5500.00,'paid','2025-11-28 06:32:31.872577','3AD7C5A29833',21,12,2);
/*!40000 ALTER TABLE `members_payment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-01 10:17:27
