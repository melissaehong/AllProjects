-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema the_wall_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema the_wall_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `the_wall_db` DEFAULT CHARACTER SET utf8 ;
USE `the_wall_db` ;

-- -----------------------------------------------------
-- Table `the_wall_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `the_wall_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `the_wall_db`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `the_wall_db`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `message` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_users_idx` (`user_id` ASC),
  CONSTRAINT `fk_messages_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `the_wall_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `the_wall_db`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `the_wall_db`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `message_id` INT NOT NULL,
  `comment` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_users1_idx` (`user_id` ASC),
  INDEX `fk_comments_messages1_idx` (`message_id` ASC),
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `the_wall_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_messages1`
    FOREIGN KEY (`message_id`)
    REFERENCES `the_wall_db`.`messages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
