 /*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80027
Source Host           : localhost:3306
Source Database       : db_school

Target Server Type    : MYSQL
Target Server Version : 80027
File Encoding         : 65001

Date: 2022-12-14 09:55:47
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for application
-- ----------------------------
DROP TABLE IF EXISTS `application`;
CREATE TABLE `application` (
  `app_grade_id` int NOT NULL,
  `app_stu_id` bigint NOT NULL,
  `app_ins_id` int NOT NULL,
  `app_time` datetime NOT NULL,
  `app_reason_site` text,
  `app_is_out` tinyint DEFAULT NULL,
  `app_is_agreed` tinyint DEFAULT NULL,
  `app_id` int unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`app_id`),
  KEY `const_app_stu` (`app_stu_id`),
  KEY `const_app_ins` (`app_ins_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of application
-- ----------------------------


-- ----------------------------
-- Table structure for grade
-- ----------------------------
DROP TABLE IF EXISTS `grade`;
CREATE TABLE `grade` (
  `grade_id` int NOT NULL,
  `grade_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `grade_is_delete` tinyint DEFAULT NULL,
  PRIMARY KEY (`grade_id`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of grade
-- ----------------------------


-- ----------------------------
-- Table structure for instructor
-- ----------------------------
DROP TABLE IF EXISTS `instructor`;
CREATE TABLE `instructor` (
  `ins_id` int NOT NULL,
  `ins_name` varchar(255) DEFAULT NULL,
  `ins_password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `ins_gender` varchar(5) DEFAULT NULL,
  `ins_is_delete` tinyint DEFAULT NULL,
  `ins_tele` varchar(11) DEFAULT NULL,
  `ins_grade_id` int DEFAULT NULL
  PRIMARY KEY (`ins_id`)
  KEY `const_ins_grade` (`ins_grade_id`),
  CONSTRAINT `const_ins_grade` FOREIGN KEY (`ins_grade_id`) REFERENCES `grade` (`grade_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of instructor
-- ----------------------------


-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `stu_id` bigint NOT NULL,
  `stu_name` varchar(255) DEFAULT NULL,
  `stu_password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `stu_gender` varchar(5) DEFAULT NULL,
  `stu_is_delete` tinyint DEFAULT NULL,
  `stu_age` int DEFAULT NULL,
  `stu_grade_id` int DEFAULT NULL,
  `stu_ins_id` int DEFAULT NULL,
  PRIMARY KEY (`stu_id`),
  KEY `const_stu_ins` (`stu_ins_id`),
  KEY `const_stu_grade` (`stu_grade_id`),
  CONSTRAINT `const_stu_grade` FOREIGN KEY (`stu_grade_id`) REFERENCES `grade` (`grade_id`),
  CONSTRAINT `const_stu_ins` FOREIGN KEY (`stu_ins_id`) REFERENCES `instructor` (`ins_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of student
-- ----------------------------

