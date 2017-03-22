create database if not exists emc_test;
use emc_test;

-- 测试单位
create table if not exists danwei (
  danweiId integer unsigned not null auto_increment primary key,
  danweimc varchar(64) not null,
  danweidz char(64) not null,
  danweilxfs char(64) not null,
  index danwei_mc(danweimc)
) engine=InnoDB DEFAULT CHARSET=utf8;

-- 测试人员（测试人员姓名，性别，年龄，学历，职称，证书编号）
create table if not exists t_ry(
  t_ryId integer unsigned not null auto_increment primary key,
  t_ryname varchar(64) not null,
  t_rygender varchar(8) not null,
  t_ryage varchar(8) not null,
  t_rydegree char(32) not null,
  t_rytitle char(32) not null,
  t_rynumber char(32),
  index t_ry_id(t_ryname)
) engine=InnoDB DEFAULT CHARSET=utf8;

-- 测试环境（测试时间，地点、温度、湿度）
create table if not exists t_hj(
  t_hjId integer unsigned not null auto_increment primary key,
  t_hjsj date not null,
  t_hjdd char(32) not null,
  t_hjwd float(16) not null,
  t_hjsd float(16) not null,
  index t_hj_id(t_hjdd)
) engine=InnoDB DEFAULT CHARSET=utf8

-- 测试实验室（测试实验室名称，等级，简介，单位名称，）
create table if not exists t_lab(
  t_labId integer unsigned not null auto_increment primary key,
  t_labmc varchar(16) not null,
  t_lablv varchar(16) not null,
  t_labintro char(64) not null,
  t_lab_f_dwmc varchar(64) not null,
  t_lab_f_dwdz char(64) not null,
  t_lab_f_lxfs char(64) not null,
  index t_lab_id(t_labId)
) engine=InnoDB DEFAULT CHARSET=utf8;

-- 测试仪器表（仪器编号，型号，名称，制造国家，厂名，购买时间，主要技术指标，目前状态，所属单位）
create table if not exists t_yq(
  t_yqId integer unsigned not null auto_increment primary key,
  t_yqxh varchar(16) not null,
  t_yqmc char(16) not null,
  t_yqzzgj char(16) not null,
  t_yqzzs char(16) not null,
  t_yqgmsj date not null,
  t_yqintro char(64) not null,
  t_yqzt char(16) not null,
  t_yq_f_dwmc varchar(64) not null,
  index t_yq_mc(t_yqmc)
) engine=InnoDB DEFAULT CHARSET=utf8;

-- 测试方法表（测试方法编号，方法名称，适用范围，测试方法示意图，测试步骤，备注，测试仪器）
create table if not exists t_method(
  t_ffId integer unsigned not null auto_increment primary key,
  t_ffmc varchar(16) not null,
  t_ffsyfw char(32) not null,
  t_ffdiagrams char(64),
  t_ffstep char(32) not null,
  t_ffmemo char(32),
  t_ff_f_yqmcchar(16) not null,
  index t_method_ffmc(t_ffmc),
) engine=InnoDB DEFAULT CHARSET=utf8;
