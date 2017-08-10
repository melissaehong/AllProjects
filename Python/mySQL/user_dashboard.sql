-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema user_dashboard
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema user_dashboard
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `user_dashboard` DEFAULT CHARACTER SET utf8 ;
USE `user_dashboard` ;

-- -----------------------------------------------------
-- Table `user_dashboard`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `user_dashboard`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `admin_id` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `user_dashboard`.`user_levels`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `user_dashboard`.`user_levels` (
  `id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `user_level` VARCHAR(10) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_user_info_users1_idx` (`user_id` ASC),
  CONSTRAINT `fk_user_info_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `user_dashboard`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `user_dashboard`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `user_dashboard`.`messages` (
  `id` INT NOT NULL,
  `content` TEXT NULL,
  `user_level_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_t` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_user_info1_idx` (`user_level_id` ASC),
  CONSTRAINT `fk_messages_user_info1`
    FOREIGN KEY (`user_level_id`)
    REFERENCES `user_dashboard`.`user_levels` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `user_dashboard`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `user_dashboard`.`comments` (
  `id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `content` TEXT NULL,
  `messages_id` INT NOT NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_messages1_idx` (`messages_id` ASC),
  INDEX `fk_comments_users1_idx` (`users_id` ASC),
  CONSTRAINT `fk_comments_messages1`
    FOREIGN KEY (`messages_id`)
    REFERENCES `user_dashboard`.`messages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `user_dashboard`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
