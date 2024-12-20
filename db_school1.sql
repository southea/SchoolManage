/*
 Navicat Premium Data Transfer

 Source Server         : mysql1
 Source Server Type    : MySQL
 Source Server Version : 50724
 Source Host           : localhost:3306
 Source Schema         : db_school

 Target Server Type    : MySQL
 Target Server Version : 50724
 File Encoding         : 65001

 Date: 29/12/2022 12:10:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for application
-- ----------------------------
DROP TABLE IF EXISTS `application`;
CREATE TABLE `application`  (
  `app_grade_id` int(11) NOT NULL,
  `app_stu_id` bigint(12) NOT NULL,
  `app_ins_id` int(11) NOT NULL,
  `app_time` datetime NOT NULL COMMENT '提交申请的时间',
  `app_reason_site` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '出校或入校原因',
  `app_is_out` tinyint(4) NULL DEFAULT NULL,
  `app_is_agreed` tinyint(4) NULL DEFAULT NULL COMMENT '辅导员是否审批通过',
  `app_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`app_id`) USING BTREE,
  INDEX `const_app_stu`(`app_stu_id`) USING BTREE,
  INDEX `const_app_ins`(`app_ins_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of application
-- ----------------------------
INSERT INTO `application` VALUES (2021, 202100100001, 202101, '2022-12-10 22:44:20', '外出游玩', 1, 1, 1);
INSERT INTO `application` VALUES (2021, 202100100004, 202101, '2022-12-11 19:37:11', '外出吃饭', 1, 2, 2);
INSERT INTO `application` VALUES (2021, 202100400001, 202102, '2022-12-11 19:37:25', '跨校区调研', 1, 2, 3);
INSERT INTO `application` VALUES (2022, 202200400001, 202202, '2022-12-11 20:05:47', '外出实习', 1, 2, 4);
INSERT INTO `application` VALUES (2022, 202200100001, 202201, '2022-12-11 21:15:51', '团建', 1, 0, 5);
INSERT INTO `application` VALUES (2021, 202100100007, 202101, '2022-12-11 21:16:09', '团建', 1, 0, 6);
INSERT INTO `application` VALUES (2022, 202200400001, 202202, '2022-12-14 09:54:38', '团建', 1, 1, 7);

-- ----------------------------
-- Table structure for grade
-- ----------------------------
DROP TABLE IF EXISTS `grade`;
CREATE TABLE `grade`  (
  `grade_id` int(11) NOT NULL,
  `grade_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `grade_is_delete` tinyint(4) NULL DEFAULT NULL,
  PRIMARY KEY (`grade_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of grade
-- ----------------------------
INSERT INTO `grade` VALUES (2019, '19级', 0);
INSERT INTO `grade` VALUES (2020, '20级', 0);
INSERT INTO `grade` VALUES (2021, '21级', 0);
INSERT INTO `grade` VALUES (2022, '22级', 0);

-- ----------------------------
-- Table structure for instructor
-- ----------------------------
DROP TABLE IF EXISTS `instructor`;
CREATE TABLE `instructor`  (
  `ins_id` int(11) NOT NULL,
  `ins_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ins_password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ins_gender` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ins_is_delete` tinyint(4) NULL DEFAULT NULL,
  `ins_tele` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ins_grade_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`ins_id`) USING BTREE,
  INDEX `const_ins_grade`(`ins_grade_id`) USING BTREE,
  CONSTRAINT `const_ins_grade` FOREIGN KEY (`ins_grade_id`) REFERENCES `grade` (`grade_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of instructor
-- ----------------------------
INSERT INTO `instructor` VALUES (201901, '林珮瑜', '123456', '女', 0, '13265045789', 2019);
INSERT INTO `instructor` VALUES (201902, '朱政廷', '123456', '男', 0, '13225866850', 2019);
INSERT INTO `instructor` VALUES (201903, '查瑜舜', '123456', '男', 0, '17306008793', 2019);
INSERT INTO `instructor` VALUES (202001, '康永清', '123456', '男', 0, '17845036178', 2020);
INSERT INTO `instructor` VALUES (202002, '邓诗涵', '123456', '女', 0, '16630497249', 2020);
INSERT INTO `instructor` VALUES (202003, '周白芷', '123456', '女', 0, '15624466625', 2020);
INSERT INTO `instructor` VALUES (202101, '施卿', '1234567', '女', 0, '13363045368', 2021);
INSERT INTO `instructor` VALUES (202102, '陈智筠', '123456', '男', 0, '19960837254', 2021);
INSERT INTO `instructor` VALUES (202103, '卢志铭', '123456', '男', 0, '18118571244', 2021);
INSERT INTO `instructor` VALUES (202201, '贺方玉', '123456', '男', 0, '15532045187', 2022);
INSERT INTO `instructor` VALUES (202202, '张博海', '123456', '男', 0, '18501115289', 2022);
INSERT INTO `instructor` VALUES (202203, '周佳勋', '123456', '男', 0, '17735978525', 2022);

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `stu_id` bigint(12) NOT NULL,
  `stu_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `stu_password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `stu_gender` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `stu_is_delete` tinyint(4) NULL DEFAULT NULL,
  `stu_age` int(11) NULL DEFAULT NULL,
  `stu_grade_id` int(11) NULL DEFAULT NULL,
  `stu_ins_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`stu_id`) USING BTREE,
  INDEX `const_stu_ins`(`stu_ins_id`) USING BTREE,
  INDEX `const_stu_grade`(`stu_grade_id`) USING BTREE,
  CONSTRAINT `const_stu_grade` FOREIGN KEY (`stu_grade_id`) REFERENCES `grade` (`grade_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `const_stu_ins` FOREIGN KEY (`stu_ins_id`) REFERENCES `instructor` (`ins_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (202100100001, '张宿', '123456', '男', 0, 20, 2021, 202101);
INSERT INTO `student` VALUES (202100100002, '王硕', '123456', '女', 0, 20, 2021, 202101);
INSERT INTO `student` VALUES (202100100004, '蔡宜芸', '123456', '女', 0, 20, 2021, 202101);
INSERT INTO `student` VALUES (202100100005, '李士杰', '123456', '男', 0, 20, 2021, 202101);
INSERT INTO `student` VALUES (202100100007, '李姿伶', '123456', '女', 0, 20, 2021, 202101);
INSERT INTO `student` VALUES (202100400001, '谢佳儒', '123456', '女', 0, 20, 2021, 202102);
INSERT INTO `student` VALUES (202200100001, '赵树', '123456', '女', 0, 19, 2022, 202201);
INSERT INTO `student` VALUES (202200100002, '蔡书玮', '123456', '男', 0, 19, 2022, 202201);
INSERT INTO `student` VALUES (202200100005, '陈文婷', '123456', '女', 0, 19, 2022, 202201);
INSERT INTO `student` VALUES (202200100007, '李成白', '123456', '男', 1, 19, 2022, 202201);
INSERT INTO `student` VALUES (202200400001, '苏姿婷', '123456', '女', 0, 19, 2022, 202202);

SET FOREIGN_KEY_CHECKS = 1;
