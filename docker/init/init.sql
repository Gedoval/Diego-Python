CREATE DATABASE IF NOT EXISTS test;
USE test;
DROP TABLE IF EXISTS `Facturas`;
CREATE TABLE `Facturas` (
  `FacturaId` int(11) NOT NULL AUTO_INCREMENT,
  `GestorId` int(11) DEFAULT NULL,
  `NombreCliente` varchar(50) DEFAULT NULL,
  `PrecioTotal` double NOT NULL,
  PRIMARY KEY (`FacturaId`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `Usuarios`;
CREATE TABLE `Usuarios` (
  `UsuarioId` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) DEFAULT NULL,
  `Apellido` varchar(50) DEFAULT NULL,
  `CUIT` double NOT NULL,
  PRIMARY KEY (`UsuarioId`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

INSERT INTO `Facturas` VALUES (1, 109, 'Pedrito', 100),(2,109, 'Shanghai', 400),(3,287, 'Martita', 699);
INSERT INTO `Usuarios` VALUES (109,'Juancito', 'Pascal', 11111222),(287,'Marianito', 'Rodriguez', 44865413), (388,'Armando', 'Barreda', 23412685);