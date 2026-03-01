-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-03-2026 a las 23:28:03
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `flask`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `encuestas`
--

CREATE TABLE `encuestas` (
  `nombre` varchar(25) NOT NULL,
  `apellido` varchar(25) NOT NULL,
  `titulo` varchar(50) NOT NULL,
  `opinion` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `encuestas`
--

INSERT INTO `encuestas` (`nombre`, `apellido`, `titulo`, `opinion`) VALUES
('Vanessa', 'Gomez', 'Losail 2025', 'ha sido un carrera interante pero me gustaria que la proxima vez se de mas incapie a resultado final y no tanto a la polemica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `nom_usu` varchar(50) NOT NULL,
  `email` varchar(125) NOT NULL,
  `contraseña` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='En esta tabla se guardaran los usaurios';

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`nom_usu`, `email`, `contraseña`) VALUES
('arman', 'arman@proven.cat', 'scrypt:32768:8:1$N6WnWXfXTVcoUDyZ$4a0058b82f8b6e307a37f420f305fe94f167fc2a0e7e9c7f670b445378d65812efd889a9814696dd95dd023705e308b2d450cb254b71f5a0f4e82ab78077b431'),
('hans', 'hans@proven.cat', 'scrypt:32768:8:1$XvResrsigvbYuwae$b1437fb47f225aa678d73f1f8d6fc3a3cf4ac47770bf867c345ed43a1f8037519570e77ab8f27a15536a113fa72f11852c68650413263c9fa1635ee2b061097c'),
('vane', 'vane@gmail.com', 'scrypt:32768:8:1$ka39nHx4OAgE3nQX$416d88b9d3d8e42b1a9c2f8f40d126e2e516874eb20fcce0c4af488ce4c2ec9440e461d9a383810887c521e497eeccde56d15c8ca370183402ab08eb9b4b4e0e');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`nom_usu`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
