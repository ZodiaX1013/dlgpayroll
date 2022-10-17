-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: demo-do-user-12574852-0.b.db.ondigitalocean.com    Database: defaultdb
-- ------------------------------------------------------
-- Server version	8.0.28

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'c1b60e6a-43bd-11ed-a472-32f93e74fabf:1-356';

--
-- Table structure for table `ModifyVariables`
--

DROP TABLE IF EXISTS `ModifyVariables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ModifyVariables` (
  `id` int NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) DEFAULT NULL,
  `Arrears` varchar(45) DEFAULT NULL,
  `LocalRef` varchar(45) DEFAULT NULL,
  `FixedAllowance` varchar(45) DEFAULT NULL,
  `DiscBns` varchar(45) DEFAULT NULL,
  `AttBns` varchar(45) DEFAULT NULL,
  `Transport` varchar(45) DEFAULT NULL,
  `SickRef` varchar(45) DEFAULT NULL,
  `SpeBns` varchar(45) DEFAULT NULL,
  `OtherAlw` varchar(45) DEFAULT NULL,
  `Overseas` varchar(45) DEFAULT NULL,
  `OtherDed` varchar(45) DEFAULT NULL,
  `Absences` varchar(45) DEFAULT NULL,
  `ot1` varchar(45) DEFAULT NULL,
  `amt1` varchar(45) DEFAULT NULL,
  `ot2` varchar(45) DEFAULT NULL,
  `amt2` varchar(45) DEFAULT NULL,
  `ot3` varchar(45) DEFAULT NULL,
  `amt3` varchar(45) DEFAULT NULL,
  `lateness` varchar(45) DEFAULT NULL,
  `amt4` varchar(45) DEFAULT NULL,
  `TaxDes` varchar(45) DEFAULT NULL,
  `tax` varchar(45) DEFAULT NULL,
  `NTaxDes` varchar(45) DEFAULT NULL,
  `ntax` varchar(45) DEFAULT NULL,
  `Month` varchar(45) DEFAULT NULL,
  `UNQ` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ModifyVariables`
--

LOCK TABLES `ModifyVariables` WRITE;
/*!40000 ALTER TABLE `ModifyVariables` DISABLE KEYS */;
/*!40000 ALTER TABLE `ModifyVariables` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OriginalData`
--

DROP TABLE IF EXISTS `OriginalData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `OriginalData` (
  `id` int NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) DEFAULT NULL,
  `EmployeeName` varchar(45) DEFAULT NULL,
  `BasicSalary` varchar(45) DEFAULT NULL,
  `FixedAllow` varchar(45) DEFAULT NULL,
  `OtherDeduction` varchar(45) DEFAULT NULL,
  `Overtime` varchar(45) DEFAULT NULL,
  `DiscBonus` varchar(45) DEFAULT NULL,
  `NSFEmpee` varchar(45) DEFAULT NULL,
  `OtherAllow` varchar(45) DEFAULT NULL,
  `TaxableAllow` varchar(45) DEFAULT NULL,
  `Medical` varchar(45) DEFAULT NULL,
  `Transport` varchar(45) DEFAULT NULL,
  `overseas` varchar(45) DEFAULT NULL,
  `NTaxableAllow` varchar(45) DEFAULT NULL,
  `EDF` varchar(45) DEFAULT NULL,
  `Arrears` varchar(45) DEFAULT NULL,
  `AttendanceBns` varchar(45) DEFAULT NULL,
  `EOY` varchar(45) DEFAULT NULL,
  `Loan` varchar(45) DEFAULT NULL,
  `CarBenefit` varchar(45) DEFAULT NULL,
  `LeaveRef` varchar(45) DEFAULT NULL,
  `SLevy` varchar(45) DEFAULT NULL,
  `SpecialBns` varchar(45) DEFAULT NULL,
  `Lateness` varchar(45) DEFAULT NULL,
  `EducationRel` varchar(45) DEFAULT NULL,
  `SpeProBns` varchar(45) DEFAULT NULL,
  `NPS` varchar(45) DEFAULT NULL,
  `MedicalRel` varchar(45) DEFAULT NULL,
  `Payable` varchar(45) DEFAULT NULL,
  `Deduction` varchar(45) DEFAULT NULL,
  `NetPay` varchar(45) DEFAULT NULL,
  `NetPaysheet` varchar(45) DEFAULT NULL,
  `CurrentGross` varchar(45) DEFAULT NULL,
  `cGrossTax` varchar(45) DEFAULT NULL,
  `PrevGross` varchar(45) DEFAULT NULL,
  `PrevIET` varchar(45) DEFAULT NULL,
  `IET` varchar(45) DEFAULT NULL,
  `NetCh` varchar(45) DEFAULT NULL,
  `CurrentPAYE` varchar(45) DEFAULT NULL,
  `PrevPAYE` varchar(45) DEFAULT NULL,
  `PAYE` varchar(45) DEFAULT NULL,
  `eCSG` varchar(45) DEFAULT NULL,
  `eNSF` varchar(45) DEFAULT NULL,
  `eLevy` varchar(45) DEFAULT NULL,
  `PRGF` varchar(45) DEFAULT NULL,
  `PrevThreshold` varchar(45) DEFAULT NULL,
  `Threshold` varchar(45) DEFAULT NULL,
  `netchar` varchar(45) DEFAULT NULL,
  `CurrentSLevy` varchar(45) DEFAULT NULL,
  `PrevSLevy` varchar(45) DEFAULT NULL,
  `slevyPay` varchar(45) DEFAULT NULL,
  `Absences` varchar(45) DEFAULT NULL,
  `Month` varchar(45) DEFAULT NULL,
  `Year` varchar(45) DEFAULT NULL,
  `UNQ` varchar(45) DEFAULT NULL,
  `LockSal` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OriginalData`
--

LOCK TABLES `OriginalData` WRITE;
/*!40000 ALTER TABLE `OriginalData` DISABLE KEYS */;
/*!40000 ALTER TABLE `OriginalData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cred`
--

DROP TABLE IF EXISTS `cred`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cred` (
  `id` varchar(45) NOT NULL,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cred`
--

LOCK TABLES `cred` WRITE;
/*!40000 ALTER TABLE `cred` DISABLE KEYS */;
INSERT INTO `cred` VALUES ('1','admin','788073cefde4b240873e1f52f5371d7d');
/*!40000 ALTER TABLE `cred` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `depID` int NOT NULL AUTO_INCREMENT,
  `DepartmentName` varchar(255) NOT NULL,
  PRIMARY KEY (`depID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `eid` int NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) DEFAULT NULL,
  `FirstName` varchar(45) DEFAULT NULL,
  `LastName` varchar(45) DEFAULT NULL,
  `Title` varchar(45) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `clocked` varchar(45) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `country` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `mobile` varchar(45) DEFAULT NULL,
  `fax` varchar(45) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `image` varchar(45) DEFAULT NULL,
  `NICno` varchar(45) DEFAULT NULL,
  `TaxAC` varchar(45) DEFAULT NULL,
  `Bank` varchar(255) DEFAULT NULL,
  `BankAC` varchar(45) DEFAULT NULL,
  `Bankcode` varchar(45) DEFAULT NULL,
  `report` varchar(45) DEFAULT NULL,
  `NPS` varchar(45) DEFAULT NULL,
  `Carbenefit` varchar(45) DEFAULT NULL,
  `hire` date DEFAULT NULL,
  `salary` varchar(45) DEFAULT NULL,
  `position` varchar(45) DEFAULT NULL,
  `department` varchar(45) DEFAULT NULL,
  `Subdepartment` varchar(45) DEFAULT NULL,
  `Payescheme` varchar(45) DEFAULT NULL,
  `Payepercentage` varchar(45) DEFAULT NULL,
  `Localleave` varchar(45) DEFAULT NULL,
  `Sickleave` varchar(45) DEFAULT NULL,
  `Fixedallow` varchar(45) DEFAULT NULL,
  `Travelmode` varchar(45) DEFAULT NULL,
  `Travelallow` varchar(45) DEFAULT NULL,
  `expatriate` varchar(45) DEFAULT NULL,
  `EDF` varchar(45) DEFAULT NULL,
  `months` varchar(45) DEFAULT NULL,
  `MonthlyEDF` varchar(45) DEFAULT NULL,
  `Houseinterest` varchar(45) DEFAULT NULL,
  `Educationrel` varchar(45) DEFAULT NULL,
  `Medicalrel` varchar(45) DEFAULT NULL,
  `Paymentmode` varchar(45) DEFAULT NULL,
  `medical` varchar(45) DEFAULT NULL,
  `working` varchar(45) DEFAULT NULL,
  `Lastwork` date DEFAULT NULL,
  `Specialbonus` varchar(45) DEFAULT NULL,
  `Workingdays` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`eid`),
  UNIQUE KEY `id_UNIQUE` (`eid`)
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (96,'AF001','Francois Louis','Anthonee','Mr.','1986-03-15','No','John Kennedy Street','Cottage','','59256014','','','','','A1503864607','','SBM Bank (Mauritius) Ltd','0000','0000','','Paid','0','2016-01-06','23150','Maintenance Officer','dep1','dep1','Monthly','100','0','0','0','','0','No','325000','13','25000','0','54646','3456','Bank','0','Yes','0001-01-01','0','26'),(97,'AZ001','Muhammad Faarooq Azhar','Khodabux','Mr.','1993-09-30','No','','','','','','','','','','','','','','','Paid','0','2021-11-08','20790','Front Desk Executive','dep2','dep2','Monthly','100','0','0','0','Bus','0','No','325000','13','25000','0','0','0','Bank','0','Yes','0001-01-01','0','22'),(98,'BBS1','Beebee Shabnaz','Bauhadoor','Ms.','1999-09-15','No','','','','','','','','','','','','','','','Paid','0','2021-06-21','15069','Axxounts/Debtors Clerk','dep3','dep3','Monthly','100','0','0','0','Bus','0','No','325000','13','25000','0','0','0','Bank','0','Yes','0001-01-01','0','22'),(99,'CR001','Corinne','Ramsamy','Mrs.','1969-08-30','No','','','','','','','','','','','','','','','Paid','0','2001-02-01','77000','GROUP ACCOUNTANT','dep4','dep4','Monthly','100','22','15','0','Car','7000','No','515000','13','39615','0','0','30000','Bank','1310','No','2006-12-20','0','26'),(100,'csac1','Cheong Shaow','Ah Ching','Mr.','1967-06-19','No','','','','','','','','','','','','','','','Paid','0','2020-01-20','310150','Management','dep1','dep1','Monthly','100','0','0','0','Car','0','No','730000','13','56154','0','0','0','Bank','0','Yes','0001-01-01','0','26'),(101,'LEUNJ','Johnny','Leung Lam Hing','Mr.','1963-12-17','No','','','','','','','','','','','','','','','Paid','10750','2002-01-01','185150','','dep1','dep1','Monthly','100','22','15','0','Car','0','No','325000','13','25000','0','0','0','Bank','0','Yes','0001-01-01','162990','26'),(102,'HA001','Aveenash Kumar','Heeroo','Mr.','1984-03-30','No','','','','','','','','','H3003844601556','','SBM Bank (Mauritius) Ltd','0140100042560','11','','Paid','9500','2017-01-03','103692','Property Manager','dep1','dep1','Monthly','100','0','0','5000','Car','0','No','435000','13','33462','108612','0','30000','Bank','0','Yes','0001-01-01','0','22'),(103,'PA01','Prisca Angeline','Samy','Mrs.','1978-07-18','No','','','','','','','','','','','','','','','Paid','0','2021-01-21','78000','','dep1','dep1','Monthly','100','22','15','1000','Car','25000','No','350000','13','26923','0','0','0','Bank','0','Yes','0001-01-01','0','22'),(107,'BG01','Gavin','Bungari','Mr.','1990-01-28','No','','','','','','','','','B2801904606247','','The Mauritius Commercial Bank Ltd','052322157','','','Paid','0','2019-03-13','30900','Facilities Officer','dep1','dep1','Monthly','100','0','0','1500','Car','0','No','325000','13','25000','0','0','0','Bank','156','Yes','0001-01-01','0','26'),(108,'FONSI','Danny','Fon Sing','Mr.','1968-09-15','No','','','','','','','','','','','','','','','Paid','12000','1994-01-01','98500','Director','dep1','dep1','Monthly','100','22','15','0','Car','0','No','600000','13','','0','200000','0','Bank','0','Yes','0001-01-01','0','26'),(109,'CD001','Deeneesh Kumar','Cassy','Mr.','1967-01-27','No','','','','','','','','','C270167210032B','','SBM Bank (Mauritius) Ltd','','','','Paid','0','2021-12-22','10950','','','','Monthly','100','0','0','0','Bus','0','No','325000','13','25000','0','0','0','Bank','0','Yes','0001-01-01','0','26'),(110,'CG001','Christine','Gobeegadoo','Mrs.','1981-12-13','No','','','','','','','','','','','','','','','Paid','0','2011-01-04','13100','','','','Monthly','100','22','15','0','Bus','0','No','515000','13','39615','0','0','0','Bank','156','Yes','0001-01-01','0','26'),(111,'DHH01','Henna Hotri','Daby','Mrs.','1992-05-09','No','','','','','','','','','','','','','','','Paid','0','2019-11-25','14319','','','','Monthly','100','0','0','0','Bus','0','No','325000','13','25000','0','0','0','Bank','','Yes','0001-01-01','0','22'),(112,'DI001','Ian','Dindoyal','Mr.','1986-05-14','No','','','','','','','','','','','','','','','Paid','0','2021-09-21','75750','','','','','','0','0','21000','Car','0','No','325000','13','25000','0','0','0','Bank','','Yes','0001-01-01','0','22'),(113,'HJ001','Ram','Kumar','Mr.','1978-09-13','No','','','','','','','','','','','','','','','Paid','0','2022-05-13','500000','','','','','','0','0','0','','50000','No','325000','13','25000','0','0','0','Bank','','Yes','0001-01-01','0','0');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leavedata`
--

DROP TABLE IF EXISTS `leavedata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leavedata` (
  `lid` int NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) NOT NULL,
  `Date` date DEFAULT NULL,
  `LeaveType` varchar(45) DEFAULT NULL,
  `LeaveDays` varchar(45) DEFAULT NULL,
  `ExtraLeave` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`),
  UNIQUE KEY `lid_UNIQUE` (`lid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leavedata`
--

LOCK TABLES `leavedata` WRITE;
/*!40000 ALTER TABLE `leavedata` DISABLE KEYS */;
/*!40000 ALTER TABLE `leavedata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payable`
--

DROP TABLE IF EXISTS `payable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payable` (
  `id` int NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) NOT NULL,
  `BasicSalary` varchar(45) DEFAULT NULL,
  `Overtime` varchar(45) DEFAULT NULL,
  `OtherAllow` varchar(45) DEFAULT NULL,
  `Transport` varchar(45) DEFAULT NULL,
  `Arrears` varchar(45) DEFAULT NULL,
  `EOY` varchar(45) DEFAULT NULL,
  `LeaveRef` varchar(45) DEFAULT NULL,
  `SpeBonus` varchar(45) DEFAULT NULL,
  `SpeProBonus` varchar(45) DEFAULT NULL,
  `FixedAllow` varchar(45) DEFAULT NULL,
  `DiscBonus` varchar(45) DEFAULT NULL,
  `TaxAllow` varchar(45) DEFAULT NULL,
  `NTaxAllow` varchar(45) DEFAULT NULL,
  `AttBonus` varchar(45) DEFAULT NULL,
  `Loan` varchar(45) DEFAULT NULL,
  `PAYE` varchar(45) DEFAULT NULL,
  `Lateness` varchar(45) DEFAULT NULL,
  `NPS` varchar(45) DEFAULT NULL,
  `OtherDed` varchar(45) DEFAULT NULL,
  `NSF` varchar(45) DEFAULT NULL,
  `Medical` varchar(45) DEFAULT NULL,
  `EDF` varchar(45) DEFAULT NULL,
  `travel` varchar(45) DEFAULT NULL,
  `car` varchar(45) DEFAULT NULL,
  `SLevy` varchar(45) DEFAULT NULL,
  `EducationRelief` varchar(45) DEFAULT NULL,
  `gross` varchar(45) DEFAULT NULL,
  `Payable` varchar(45) DEFAULT NULL,
  `Deduction` varchar(45) DEFAULT NULL,
  `NetPay` varchar(45) DEFAULT NULL,
  `OT1hr` varchar(45) DEFAULT NULL,
  `OT1amt` varchar(45) DEFAULT NULL,
  `OT2hr` varchar(45) DEFAULT NULL,
  `OT2amt` varchar(45) DEFAULT NULL,
  `OT3hr` varchar(45) DEFAULT NULL,
  `OT3amt` varchar(45) DEFAULT NULL,
  `LatenessHr` varchar(45) DEFAULT NULL,
  `Month` varchar(45) DEFAULT NULL,
  `Year` varchar(45) DEFAULT NULL,
  `IET` varchar(45) DEFAULT NULL,
  `UNQ` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb3 COMMENT='	';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payable`
--

LOCK TABLES `payable` WRITE;
/*!40000 ALTER TABLE `payable` DISABLE KEYS */;
/*!40000 ALTER TABLE `payable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paye`
--

DROP TABLE IF EXISTS `paye`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paye` (
  `pid` int NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) NOT NULL,
  `BasicSalary` varchar(45) DEFAULT NULL,
  `overtime` varchar(45) DEFAULT NULL,
  `OtherAllow` varchar(45) DEFAULT NULL,
  `Transport` varchar(45) DEFAULT NULL,
  `Arrears` varchar(45) DEFAULT NULL,
  `EOY` varchar(45) DEFAULT NULL,
  `LeaveRefund` varchar(45) DEFAULT NULL,
  `SpecialBonus` varchar(45) DEFAULT NULL,
  `FixedAllow` varchar(45) DEFAULT NULL,
  `DiscBonus` varchar(45) DEFAULT NULL,
  `TaxableAllow` varchar(45) DEFAULT NULL,
  `SpeProBonus` varchar(45) DEFAULT NULL,
  `AttBonus` varchar(45) DEFAULT NULL,
  `CarBenefit` varchar(45) DEFAULT NULL,
  `CurrGross` varchar(45) DEFAULT NULL,
  `PrevGross` varchar(45) DEFAULT NULL,
  `IET` varchar(45) DEFAULT NULL,
  `NetCh` varchar(45) DEFAULT NULL,
  `CurrPAYE` varchar(45) DEFAULT NULL,
  `PrevPAYE` varchar(45) DEFAULT NULL,
  `PAYE` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`),
  UNIQUE KEY `pid_UNIQUE` (`pid`),
  UNIQUE KEY `EmployeeID_UNIQUE` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paye`
--

LOCK TABLES `paye` WRITE;
/*!40000 ALTER TABLE `paye` DISABLE KEYS */;
/*!40000 ALTER TABLE `paye` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payecsv`
--

DROP TABLE IF EXISTS `payecsv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payecsv` (
  `id` int NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) DEFAULT NULL,
  `LastName` varchar(45) DEFAULT NULL,
  `FirstName` varchar(45) DEFAULT NULL,
  `Emoluments` varchar(45) DEFAULT NULL,
  `PAYE` varchar(45) DEFAULT NULL,
  `working` varchar(45) DEFAULT NULL,
  `SLevy` varchar(45) DEFAULT NULL,
  `EmolumentsNet` varchar(45) DEFAULT NULL,
  `month` varchar(45) DEFAULT NULL,
  `UNQ` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=148 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payecsv`
--

LOCK TABLES `payecsv` WRITE;
/*!40000 ALTER TABLE `payecsv` DISABLE KEYS */;
/*!40000 ALTER TABLE `payecsv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paysheet`
--

DROP TABLE IF EXISTS `paysheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paysheet` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) NOT NULL,
  `EmployeeName` varchar(255) DEFAULT NULL,
  `BasicSalary` int DEFAULT NULL,
  `Arrears` int DEFAULT NULL,
  `Overseas` int DEFAULT NULL,
  `TravelAllow` int DEFAULT NULL,
  `OtherAllow` int DEFAULT NULL,
  `Gross` int DEFAULT NULL,
  `PAYE` int DEFAULT NULL,
  `CSG` int DEFAULT NULL,
  `NSF` int DEFAULT NULL,
  `Medical` int DEFAULT NULL,
  `SLevy` int DEFAULT NULL,
  `Net` int DEFAULT NULL,
  `Month` varchar(45) DEFAULT NULL,
  `department` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`),
  UNIQUE KEY `EmployeeID_UNIQUE` (`EmployeeID`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paysheet`
--

LOCK TABLES `paysheet` WRITE;
/*!40000 ALTER TABLE `paysheet` DISABLE KEYS */;
/*!40000 ALTER TABLE `paysheet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payslip`
--

DROP TABLE IF EXISTS `payslip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payslip` (
  `idpayslip` int NOT NULL AUTO_INCREMENT,
  `JoinDate` varchar(45) DEFAULT NULL,
  `Company` varchar(45) DEFAULT NULL,
  `EmpName` varchar(45) DEFAULT NULL,
  `Position` varchar(45) DEFAULT NULL,
  `NIC` varchar(45) DEFAULT NULL,
  `BasicSalary` varchar(45) DEFAULT NULL,
  `TravelAlw` varchar(45) DEFAULT NULL,
  `Bonus` varchar(45) DEFAULT NULL,
  `Gross` varchar(45) DEFAULT NULL,
  `PAYE` varchar(45) DEFAULT NULL,
  `NPF` varchar(45) DEFAULT NULL,
  `NSF` varchar(45) DEFAULT NULL,
  `SLevy` varchar(45) DEFAULT NULL,
  `Deduction` varchar(45) DEFAULT NULL,
  `NetPay` varchar(45) DEFAULT NULL,
  `Payable` varchar(45) DEFAULT NULL,
  `NetPayAcc` varchar(45) DEFAULT NULL,
  `eNPF` varchar(45) DEFAULT NULL,
  `eNSF` varchar(45) DEFAULT NULL,
  `eLevy` varchar(45) DEFAULT NULL,
  `ePRGF` varchar(45) DEFAULT NULL,
  `month` varchar(45) DEFAULT NULL,
  `UNQ` varchar(45) DEFAULT NULL,
  `Lock` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idpayslip`)
) ENGINE=InnoDB AUTO_INCREMENT=890 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payslip`
--

LOCK TABLES `payslip` WRITE;
/*!40000 ALTER TABLE `payslip` DISABLE KEYS */;
/*!40000 ALTER TABLE `payslip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prgfcsv`
--

DROP TABLE IF EXISTS `prgfcsv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prgfcsv` (
  `id` int NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) DEFAULT NULL,
  `LastName` varchar(45) DEFAULT NULL,
  `FirstName` varchar(45) DEFAULT NULL,
  `Pension` varchar(45) DEFAULT NULL,
  `Working` varchar(45) DEFAULT NULL,
  `Hire` date DEFAULT NULL,
  `Basic` varchar(45) DEFAULT NULL,
  `Allowance` varchar(45) DEFAULT NULL,
  `Commission` varchar(45) DEFAULT NULL,
  `TotalRem` varchar(45) DEFAULT NULL,
  `PRGF` varchar(45) DEFAULT NULL,
  `month` varchar(45) DEFAULT NULL,
  `UNQ` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prgfcsv`
--

LOCK TABLES `prgfcsv` WRITE;
/*!40000 ALTER TABLE `prgfcsv` DISABLE KEYS */;
/*!40000 ALTER TABLE `prgfcsv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salary`
--

DROP TABLE IF EXISTS `salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary` (
  `id` int NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) DEFAULT NULL,
  `EmployeeName` varchar(45) DEFAULT NULL,
  `BasicSalary` varchar(45) DEFAULT NULL,
  `FixedAllow` varchar(45) DEFAULT NULL,
  `OtherDeduction` varchar(45) DEFAULT NULL,
  `Overtime` varchar(45) DEFAULT NULL,
  `DiscBonus` varchar(45) DEFAULT NULL,
  `NSFEmpee` varchar(45) DEFAULT NULL,
  `OtherAllow` varchar(45) DEFAULT NULL,
  `TaxableAllow` varchar(45) DEFAULT NULL,
  `Medical` varchar(45) DEFAULT NULL,
  `Transport` varchar(45) DEFAULT NULL,
  `overseas` varchar(45) DEFAULT NULL,
  `NTaxableAllow` varchar(45) DEFAULT NULL,
  `EDF` varchar(45) DEFAULT NULL,
  `Arrears` varchar(45) DEFAULT NULL,
  `AttendanceBns` varchar(45) DEFAULT NULL,
  `EOY` varchar(45) DEFAULT NULL,
  `Loan` varchar(45) DEFAULT NULL,
  `CarBenefit` varchar(45) DEFAULT NULL,
  `LeaveRef` varchar(45) DEFAULT NULL,
  `SLevy` varchar(45) DEFAULT NULL,
  `SpecialBns` varchar(45) DEFAULT NULL,
  `Lateness` varchar(45) DEFAULT NULL,
  `EducationRel` varchar(45) DEFAULT NULL,
  `SpeProBns` varchar(45) DEFAULT NULL,
  `NPS` varchar(45) DEFAULT NULL,
  `MedicalRel` varchar(45) DEFAULT NULL,
  `Payable` varchar(45) DEFAULT NULL,
  `Deduction` varchar(45) DEFAULT NULL,
  `NetPay` varchar(45) DEFAULT NULL,
  `NetPaysheet` varchar(45) DEFAULT NULL,
  `CurrentGross` varchar(45) DEFAULT NULL,
  `cGrossTax` varchar(45) DEFAULT NULL,
  `PrevGross` varchar(45) DEFAULT NULL,
  `PrevIET` varchar(45) DEFAULT NULL,
  `IET` varchar(45) DEFAULT NULL,
  `NetCh` varchar(45) DEFAULT NULL,
  `CurrentPAYE` varchar(45) DEFAULT NULL,
  `PrevPAYE` varchar(45) DEFAULT NULL,
  `PAYE` varchar(45) DEFAULT NULL,
  `eCSG` varchar(45) DEFAULT NULL,
  `eNSF` varchar(45) DEFAULT NULL,
  `eLevy` varchar(45) DEFAULT NULL,
  `PRGF` varchar(45) DEFAULT NULL,
  `PrevThreshold` varchar(45) DEFAULT NULL,
  `Threshold` varchar(45) DEFAULT NULL,
  `netchar` varchar(45) DEFAULT NULL,
  `CurrentSLevy` varchar(45) DEFAULT NULL,
  `PrevSLevy` varchar(45) DEFAULT NULL,
  `slevyPay` varchar(45) DEFAULT NULL,
  `Absences` varchar(45) DEFAULT NULL,
  `Month` varchar(45) DEFAULT NULL,
  `Year` varchar(45) DEFAULT NULL,
  `UNQ` varchar(45) DEFAULT NULL,
  `LockSal` varchar(45) DEFAULT 'No',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=890 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary`
--

LOCK TABLES `salary` WRITE;
/*!40000 ALTER TABLE `salary` DISABLE KEYS */;
/*!40000 ALTER TABLE `salary` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-17 17:51:18
