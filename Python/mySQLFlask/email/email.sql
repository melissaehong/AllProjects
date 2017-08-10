-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema email
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema email
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `email` DEFAULT CHARACTER SET utf8 ;
USE `email` ;

-- -----------------------------------------------------
-- Table `email`.`emails`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `email`.`emails` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
