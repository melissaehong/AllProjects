-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`dojos` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `location` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`addresses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`addresses` (
  `id` INT NOT NULL,
  `street` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `state` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`students` (
  `id` INT NOT NULL,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `created_at` VARCHAR(45) NULL,
  `updated_at` VARCHAR(45) NULL,
  `dojo_id` INT NOT NULL,
  `address_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_students_dojos_idx` (`dojo_id` ASC),
  INDEX `fk_students_addresses1_idx` (`address_id` ASC),
  CONSTRAINT `fk_students_dojos`
    FOREIGN KEY (`dojo_id`)
    REFERENCES `mydb`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_students_addresses1`
    FOREIGN KEY (`address_id`)
    REFERENCES `mydb`.`addresses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`interests`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`interests` (
  `id` INT NOT NULL,
  `interest` VARCHAR(45) NULL,
  `created_at` VARCHAR(45) NULL,
  `updated_at` VARCHAR(45) NULL,
  `students_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_interests_students1_idx` (`students_id` ASC),
  CONSTRAINT `fk_interests_students1`
    FOREIGN KEY (`students_id`)
    REFERENCES `mydb`.`students` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
