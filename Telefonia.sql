



-- Autor: Fernando Pereira Alves
-- GitHub: @Fernandodev0102
-- Contato: 85976014779


-- Desabilitar verificação de chave estrangeira temporariamente
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;

CREATE SCHEMA IF NOT EXISTS `Telefonia` DEFAULT CHARACTER SET utf8 ;
USE `Telefonia` ;

-- Criar a tabela ListaContatos
CREATE TABLE IF NOT EXISTS `ListaContatos` (
  `Nome` VARCHAR(45) NOT NULL,
  `Numero` VARCHAR(30) NOT NULL,
  `Cidade` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Numero`)
) ENGINE = InnoDB;

SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
