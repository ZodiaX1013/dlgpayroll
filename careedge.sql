-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: us-cdbr-east-06.cleardb.net    Database: heroku_dbb5a8d2e1d2fbf
-- ------------------------------------------------------
-- Server version	5.6.50-log

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
-- Table structure for table `department`
--

use heroku_2454cdb096d1842;

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `depID` int(11) NOT NULL AUTO_INCREMENT,
  `DepartmentName` varchar(255) NOT NULL,
  PRIMARY KEY (`depID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `eid` int(11) NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) NOT NULL,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
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
  `Localleave` int(11) DEFAULT NULL,
  `Sickleave` int(11) DEFAULT NULL,
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
  PRIMARY KEY (`EmployeeID`),
  UNIQUE KEY `id_UNIQUE` (`eid`),
  UNIQUE KEY `EmployeeID_UNIQUE` (`EmployeeID`),
  UNIQUE KEY `Bank AC_UNIQUE` (`BankAC`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `leavedata`
--

DROP TABLE IF EXISTS `leavedata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leavedata` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) NOT NULL,
  `Date` date DEFAULT NULL,
  `LeaveType` varchar(45) DEFAULT NULL,
  `LeaveDays` varchar(45) DEFAULT NULL,
  `ExtraLeave` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`),
  UNIQUE KEY `lid_UNIQUE` (`lid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `payable`
--

DROP TABLE IF EXISTS `payable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`EmployeeID`),
  UNIQUE KEY `EmployeeID_UNIQUE` (`EmployeeID`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COMMENT='	';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `paye`
--

DROP TABLE IF EXISTS `paye`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paye` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `paysheet`
--

DROP TABLE IF EXISTS `paysheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paysheet` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `EmployeeID` varchar(45) NOT NULL,
  `EmployeeName` varchar(255) DEFAULT NULL,
  `BasicSalary` int(11) DEFAULT NULL,
  `Arrears` int(11) DEFAULT NULL,
  `Overseas` int(11) DEFAULT NULL,
  `TravelAllow` int(11) DEFAULT NULL,
  `OtherAllow` int(11) DEFAULT NULL,
  `Gross` int(11) DEFAULT NULL,
  `PAYE` int(11) DEFAULT NULL,
  `CSG` int(11) DEFAULT NULL,
  `NSF` int(11) DEFAULT NULL,
  `Medical` int(11) DEFAULT NULL,
  `SLevy` int(11) DEFAULT NULL,
  `Net` int(11) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `department` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`),
  UNIQUE KEY `EmployeeID_UNIQUE` (`EmployeeID`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `salary`
--

DROP TABLE IF EXISTS `salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `salary` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `Employee ID` varchar(45) NOT NULL,
  `arrears` varchar(45) DEFAULT NULL,
  `transport` varchar(45) DEFAULT NULL,
  `Other allow` varchar(45) DEFAULT NULL,
  `Local refund` varchar(45) DEFAULT NULL,
  `Sick refund` varchar(45) DEFAULT NULL,
  `Special bonus` varchar(45) DEFAULT NULL,
  `Fixed allow` varchar(45) DEFAULT NULL,
  `Disct bonus` varchar(45) DEFAULT NULL,
  `Other ded` varchar(45) DEFAULT NULL,
  `Att bonus` varchar(45) DEFAULT NULL,
  `OT1 hour` varchar(45) DEFAULT NULL,
  `OT1 amo` varchar(45) DEFAULT NULL,
  `OT2 hour` varchar(45) DEFAULT NULL,
  `OT2 amo` varchar(45) DEFAULT NULL,
  `OT3 hour` varchar(45) DEFAULT NULL,
  `OT3 amo` varchar(45) DEFAULT NULL,
  `Late hour` varchar(45) DEFAULT NULL,
  `Late amo` varchar(45) DEFAULT NULL,
  `Tax allow desc` varchar(45) DEFAULT NULL,
  `Tax allow amo` varchar(45) DEFAULT NULL,
  `NTax allow desc` varchar(45) DEFAULT NULL,
  `NTax allow amo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Employee ID`),
  UNIQUE KEY `sid_UNIQUE` (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-15 10:41:42
