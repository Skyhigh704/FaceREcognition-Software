-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 20, 2022 at 01:17 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognition_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `person`
--

CREATE TABLE `person` (
  `id` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `phn_no` varchar(11) DEFAULT NULL,
  `dob` varchar(45) DEFAULT NULL,
  `year` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `photo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `person`
--

INSERT INTO `person` (`id`, `name`, `address`, `email`, `phn_no`, `dob`, `year`, `gender`, `location`, `photo`) VALUES
(1, 'Suborno Izak Bari', 'California', 'ss@gmail.com', '01987878787', 'April 2,2010', '2020', 'Male', 'Barisal', 'YES'),
(2, 'Sakib al Hasan', 'Jessore', 'sk@gmail.com', '01976888888', 'June 3,1986', '2019', 'Male', 'Dhaka', 'YES'),
(3, 'Taskin Ahmed', 'Mymensingh', 'ts@gmail.com', '0187756789', 'April 4,1989', '2022', 'Male', 'Dhaka', 'YES'),
(4, 'Sakib Al Hasan', 'Jessore', 'sk@gmail.com', '01878888885', 'June 3.1986', '2022', 'Male', 'Dhaka', 'YES'),
(5, 'Mashrafee bin mortoza', 'Narail', 'mm@gmail.com', '09877777777', 'Octobar 8,1983', '2022', 'Male', 'Dhaka', 'YES'),
(6, 'Mahmudullah Riyad', 'Mymensingh', 'mm@gmail.com', '9815151515', 'February 3,1989', '2021', 'Male', 'Dhaka', 'YES');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `person`
--
ALTER TABLE `person`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
