-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb2` DEFAULT CHARACTER SET utf8 ;
USE `mydb2` ;

-- -----------------------------------------------------
-- Table `mydb2`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb2`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
