-- MySQL dump 10.13  Distrib 5.5.14, for Linux (i686)
--
-- Host: localhost    Database: emclog
-- ------------------------------------------------------
-- Server version 5.5.14
--
-- Current Database: `emclog`
--
CREATE DATABASE  `emclog` CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `emclog`;
--
-- Table structure for table `admin_logs`
--
DROP TABLE IF EXISTS `admin_logs`;
CREATE TABLE `admin_logs` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增id ',
  `adminid` varchar(128) NOT NULL COMMENT '管理员操作id',
  `userid` varchar(128) NOT NULL COMMENT '被操作的用户id',
  `datetime` varchar(32) NOT NULL COMMENT '操作发生时间,2018-12-12 21:12:18',
  `ip` varchar(32) DEFAULT '' NOT NULL COMMENT '操作端ip地址',
  `type` tinyint DEFAULT 0 NOT NULL COMMENT '操作类型,0:一般行为；1:异常行为；2:违规行为',
  `level` tinyint DEFAULT 5 NOT NULL COMMENT '风险等级,0:紧急；1:报警；2:关键...',
  `description` varchar(128) NOT NULL COMMENT '操作内容',
  `result` tinyint DEFAULT 1 NOT NULL COMMENT '操作结果,0:失败;1:成功',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `login_logs`
--
/*
DROP TABLE IF EXISTS `login_logs`;
CREATE TABLE `login_logs` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '自增id ',
  `username` varchar(128) NOT NULL COMMENT '用户登录名',
  `ipaddress` varchar(128) DEFAULT NULL COMMENT '登录ip地址 ',
  `areaname` varchar(128) NOT NULL COMMENT '区域地址',
  `date` datetime NOT NULL COMMENT '时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=697 DEFAULT CHARSET=utf8;
*/
