-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : dim. 04 sep. 2022 à 02:49
-- Version du serveur : 10.4.24-MariaDB
-- Version de PHP : 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `employee`
--

-- --------------------------------------------------------

--
-- Structure de la table `empdata`
--

CREATE TABLE `empdata` (
  `Id` int(11) NOT NULL,
  `Name` varchar(1000) DEFAULT NULL,
  `Email_Id` text DEFAULT NULL,
  `Phone_no` int(11) DEFAULT NULL,
  `Address` text DEFAULT NULL,
  `Post` text DEFAULT NULL,
  `Salary` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `empdata`
--

INSERT INTO `empdata` (`Id`, `Name`, `Email_Id`, `Phone_no`, `Address`, `Post`, `Salary`) VALUES
(987, 'Ulises', 'uliseskpo2010@hotmail.com', 363568545, 'av siempre viva', '234', 800);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `empdata`
--
ALTER TABLE `empdata`
  ADD PRIMARY KEY (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
