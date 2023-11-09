-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 09, 2023 at 07:03 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perpus_1122102060`
--

-- --------------------------------------------------------

--
-- Table structure for table `buku_1122102060`
--

CREATE TABLE `buku_1122102060` (
  `Kode_Buku` int(11) NOT NULL,
  `Nama_Buku` varchar(255) NOT NULL,
  `Penerbit` varchar(255) DEFAULT NULL,
  `Pengarang` varchar(255) DEFAULT NULL,
  `Jumlah_Buku` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `buku_1122102060`
--

INSERT INTO `buku_1122102060` (`Kode_Buku`, `Nama_Buku`, `Penerbit`, `Pengarang`, `Jumlah_Buku`) VALUES
(1, 'buku alkitab', 'petrus', 'poveus', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `buku_1122102060`
--
ALTER TABLE `buku_1122102060`
  ADD PRIMARY KEY (`Kode_Buku`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `buku_1122102060`
--
ALTER TABLE `buku_1122102060`
  MODIFY `Kode_Buku` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
