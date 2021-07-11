/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : wsm01

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 11/12/2020 20:56:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for employee
-- ----------------------------
DROP TABLE IF EXISTS employee;
CREATE TABLE employee  (
  employee_id varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  name varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  SSN varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  phone varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  address varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  title varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (employee_id) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of employee
-- ----------------------------
INSERT INTO employee VALUES ('1', 'JACK', '11', '1234123', 'sdfsaf', 'manage');
INSERT INTO employee VALUES ('2', 'peter', '22', '13213', 'afsasf', 'accounting');
INSERT INTO employee VALUES ('3', 'xiaolong', '33', '1313', 'afdsf', 'worker');
INSERT INTO employee VALUES ('4', 'anna', '234', '234', '234', 'manage');
INSERT INTO employee VALUES ('5', '5', '5', '5', '5', '5');

-- ----------------------------
-- Table structure for inventory
-- ----------------------------
DROP TABLE IF EXISTS inventory;
CREATE TABLE inventory  (
  inventory_id varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  store_id varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  product_id varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  inventory varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (inventory_id) USING BTREE,
  INDEX store_id(store_id) USING BTREE,
  INDEX product_id(product_id) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of inventory
-- ----------------------------
INSERT INTO inventory VALUES ('1', 'APPLE', 'apple 12', '5');
INSERT INTO inventory VALUES ('2', 'APPLE', 'power bank', '10');
INSERT INTO inventory VALUES ('3', 'HUAWEI', 'p40', '3');
INSERT INTO inventory VALUES ('4', 'HUAWEI', 'power bank', '8');

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS product;
CREATE TABLE product  (
  product_id varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  name varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (product_id) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO product VALUES ('1', 'apple 12');
INSERT INTO product VALUES ('2', 'P40');
INSERT INTO product VALUES ('3', 'power bank');

-- ----------------------------
-- Table structure for store
-- ----------------------------
DROP TABLE IF EXISTS store;
CREATE TABLE store  (
  store_id varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  store_phone varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  store_adderss varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  store_manage varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  store_name varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (store_id) USING BTREE,
  INDEX store_manage(store_manage) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of store
-- ----------------------------
INSERT INTO store VALUES ('1', '1234', 'beijng', '1', 'APPLE');
INSERT INTO store VALUES ('2', '2342', '234', '4', 'HUAWEI');

SET FOREIGN_KEY_CHECKS = 1;
