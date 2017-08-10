-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema courses
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema courses
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `courses` DEFAULT CHARACTER SET utf8 ;
USE `courses` ;

-- -----------------------------------------------------
-- Table `courses`.`coursenames`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `courses`.`coursenames` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `course_name` VARCHAR(45) NULL,
  `description` LONGTEXT NULL,
  `created_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
