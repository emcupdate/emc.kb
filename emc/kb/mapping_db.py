#-*- coding: UTF-8 -*-
import sqlalchemy.types
import sqlalchemy.schema
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from five import grok
from zope import schema
from zope.interface import Interface,implements
from emc.kb import ORMBase
from emc.kb import _

class IModel(Interface):
    """编号number 记录表
    """
    modelId = schema.Int(
            title=_(u"model table primary key"),
        )
    # 型号代码
    xhdm = schema.TextLine(
            title=_(u"model code"),
        )
    #型号名称
    xhmc = schema.TextLine(
            title=_(u"model name"),
        )

class Model(ORMBase):
    """Database-backed implementation of IModel
    """
    implements(IModel)

    __tablename__ = 'model'

    modelId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )

    xhdm = sqlalchemy.schema.Column(sqlalchemy.types.String(8),
            nullable=False,
        )
    xhmc = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )

class Modeltest(ORMBase):
    """Database-backed implementation of IModel
    """
#     implements(IModel)

    __tablename__ = 'modeltest2'

    ID = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
                                       primary_key=True,)
    XHDM = sqlalchemy.schema.Column(sqlalchemy.types.String(8))
    XHMC = sqlalchemy.schema.Column(sqlalchemy.types.String(32))

class IFashej(Interface):
    """发射机
    """
    fashejId = schema.Int(
            title=_(u"table primary key"),
        )
    sbdm = schema.TextLine(
            title=_(u"she bei dai ma"),
        )
    sbmc = schema.TextLine(
            title=_(u"fa she ji ming cheng"),
        )
    # 分系统代码
    pcdm = schema.TextLine(
            title=_(u"zhuang tai pi ci dai ma"),
        )
    #分系统名称
    location = schema.TextLine(
            title=_(u"wei zhi"),
        )
    #分系统类别
    freq = schema.Float(
            title=_(u"gongzuo pinlv"),
        )
    pd_upper = schema.Float(
            title=_(u"shang bian pin"),
        )
    pd_lower = schema.Float(
            title=_(u"xia bian pin"),
        )
    num = schema.Int(
            title=_(u"pinlv dian shu"),
        )
    freq_upper = schema.Float(
            title=_(u"pinlv shang xian"),
        )
    freq_lower = schema.Float(
            title=_(u"pinlv xia xian"),
        )
    bw = schema.Float(
            title=_(u"fashe dai kuan"),
        )
    base_power = schema.Float(
            title=_(u"ji pin gong lv"),
        )
    tzlx = schema.TextLine(
            title=_(u"tiao zhi lei xing"),
        )
    bzf = schema.Float(
            title=_(u"ben zhen pin lv"),
        )
    mid_freq = schema.Float(
            title=_(u"zhong pin"),
        )
    comment1 = schema.TextLine(
            title=_(u"bei zhu"),
        )
class Fashej(ORMBase):
    """Database-backed implementation of IFashej
    """
    implements(IFashej)

    __tablename__ = 'fashej'

    fashejId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )

    sbdm = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    sbmc = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    pcdm = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
#     model = sqlalchemy.orm.relation(Model,primaryjoin=Model.modelId==modelId,)
    location = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    freq = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    pd_upper = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    pd_lower = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    num = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            nullable=False,
        )
    freq_upper = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    freq_lower = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    bw = sqlalchemy.schema.Column(sqlalchemy.types.Float(),
            nullable=False,
        )
    base_power = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    tzlx = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    bzf = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    mid_freq = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    comment1 = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
class IJieshouj(Interface):
    """接收机
    """
    jieshoujId = schema.Int(
            title=_(u"table primary key"),
        )
    sbdm = schema.TextLine(
            title=_(u"she bei dai ma"),
        )
    sbmc = schema.TextLine(
            title=_(u"jie shou ji ming cheng"),
        )
    pcdm = schema.TextLine(
            title=_(u"zhuang tai pi ci dai ma"),
        )
    location = schema.TextLine(
            title=_(u"wei zhi"),
        )
    fb_upper = schema.Float(
            title=_(u"pin duan shang xian"),
        )
    fb_lower = schema.Float(
            title=_(u"pin duan xia xian"),
        )
    freq = schema.Float(
            title=_(u"gongzuo pinlv"),
        )
    f_upper = schema.Float(
            title=_(u"shang bian pin"),
        )
    f_lower = schema.Float(
            title=_(u"xia bian pin"),
        )
    bw_receiver = schema.Float(
            title=_(u"jie shou ji dai kuan"),
        )
    sen_receiver = schema.Float(
            title=_(u"jie shou ji lin ming du"),
        )
    mf_freq_sign = schema.TextLine(
            title=_(u"zhong pin fu hao"),
        )
    mf_freq = schema.Float(
            title=_(u"zhong pin pin lv"),
        )
    lo_freq = schema.Float(
            title=_(u"ben zhen pin lv"),
        )

class Jieshouj(ORMBase):
    """Database-backed implementation of IFashej
    """
    implements(IJieshouj)

    __tablename__ = 'jieshouj'

    jieshoujId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )

    sbdm = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    sbmc = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    pcdm = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    location = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    fb_upper = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    fb_lower = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    freq = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    f_upper = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    f_lower = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    bw_receiver = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    sen_receiver = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    mf_freq_sign = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    mf_freq = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    lo_freq = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
class IFashetx(Interface):
    """发射天线
    """
    fashetxId = schema.Int(
            title=_(u"table primary key"),
        )
    cssbdm = schema.TextLine(
            title=_(u"cong shu she bei dai ma"),
        )
    cssbmc = schema.TextLine(
            title=_(u"cong shu she bei ming cheng"),
        )
    pcdm = schema.TextLine(
            title=_(u"zhuang tai pi ci dai ma"),
        )
    location = schema.TextLine(
            title=_(u"wei zhi"),
        )
    gain = schema.Float(
            title=_(u"zeng yi"),
        )
    polarization = schema.TextLine(
            title=_(u"ji hua"),
        )
    fwbskd = schema.Float(
            title=_(u"fang wei bo su dai kuan"),
        )
    fybskd = schema.Float(
            title=_(u"fu yang bo su dai kuan"),
        )
    txzxj = schema.Float(
            title=_(u"tian xian zhi xiang jiao"),
        )


class Fashetx(ORMBase):
    """Database-backed implementation of IFashej
    """
    implements(IFashetx)

    __tablename__ = 'fashetx'

    fashetxId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )

    cssbdm = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    cssbmc = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    pcdm = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    location = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    gain = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    polarization = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    fwbskd = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    fybskd = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    txzxj = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
class IJieshoutx(Interface):
    """接收天线
    """
    jieshoutxId = schema.Int(
            title=_(u"table primary key"),
        )
    cssbdm = schema.TextLine(
            title=_(u"cong shu she bei dai ma"),
        )
    cssbmc = schema.TextLine(
            title=_(u"jie shou tian xian ming cheng"),
        )
    pcdm = schema.TextLine(
            title=_(u"zhuang tai pi ci dai ma"),
        )
    location = schema.TextLine(
            title=_(u"wei zhi"),
        )
    gain = schema.Float(
            title=_(u"zeng yi"),
        )
    polarization = schema.TextLine(
            title=_(u"ji hua"),
        )
    fwbskd = schema.Float(
            title=_(u"fang wei bo su dai kuan"),
        )
    fybskd = schema.Float(
            title=_(u"fu yang bo su dai kuan"),
        )
    txzxj = schema.Float(
            title=_(u"tian xian zhi xiang jiao"),
        )


class Jieshoutx(ORMBase):
    """Database-backed implementation of IFashej
    """
    implements(IJieshoutx)

    __tablename__ = 'jieshoutx'

    jieshoutxId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )

    cssbdm = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    cssbmc = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    pcdm = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    location = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    gain = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    polarization = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    fwbskd = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    fybskd = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    txzxj = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
class ILvboq(Interface):
    """滤波器
    """
    lvboqId = schema.Int(
            title=_(u"table primary key"),
        )
    cssbdm = schema.TextLine(
            title=_(u"cong shu she bei dai ma"),
        )
    cssbmc = schema.TextLine(
            title=_(u"lv bo qi ming cheng"),
        )
    pcdm = schema.TextLine(
            title=_(u"zhuang tai pi ci dai ma"),
        )
    location = schema.TextLine(
            title=_(u"wei zhi"),
        )
    freq = schema.Float(
            title=_(u"gong zuo pin lv"),
        )
    f_upper = schema.Float(
            title=_(u"shang bian pin"),
        )
    f_lower = schema.Float(
            title=_(u"xia bian pin"),
        )
    order1 = schema.Float(
            title=_(u"lv bo qi ji shu"),
        )
    s21 = schema.Float(
            title=_(u"lv bo qi cha sun"),
        )

class Lvboq(ORMBase):
    """Database-backed implementation of IFashej
    """
    implements(ILvboq)

    __tablename__ = 'lvboq'

    lvboqId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )

    cssbdm = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    cssbmc = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    pcdm = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    location = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    freq = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    f_upper = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    f_lower = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    order1 = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    s21 = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )


class IDianxingtxzyzk(Interface):
    """典型天线增益子库
    """
    dianxingtxzyzkId = schema.Int(
            title=_(u"table primary key"),
        )
    type_antennas = schema.TextLine(
            title=_(u"tian xian lei xing"),
        )
    gain = schema.Int(
            title=_(u"zeng yi"),
        )


class Dianxingtxzyzk(ORMBase):
    """Database-backed implementation of IFashej
    """
    implements(IDianxingtxzyzk)

    __tablename__ = 'dianxingtxzyzk'

    dianxingtxzyzkId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )

    type_antennas = sqlalchemy.schema.Column(sqlalchemy.types.String(30),
            nullable=False,
        )
    gain = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            nullable=False,
        )


class ITianxianzk(Interface):
    """天线子库
    """
    tianxianzkId = schema.Int(
            title=_(u"table primary key"),
        )
    lib_code = schema.TextLine(
            title=_(u"zi ku dai ma"),
        )
    lib_name = schema.TextLine(
            title=_(u"zi ku ming cheng"),
        )


class Tianxianzk(ORMBase):
    """Database-backed implementation of ITianxianzk
    """
    implements(ITianxianzk)

    __tablename__ = 'tianxianzk'

    tianxianzkId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )
    lib_code = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    lib_name = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )


class IJieshoujzk(Interface):
    """接收机子库
    """
    jieshoujzkId = schema.Int(
            title=_(u"table primary key"),
        )
    lib_code = schema.TextLine(
            title=_(u"zi ku dai ma"),
        )
    lib_name = schema.TextLine(
            title=_(u"zi ku ming cheng"),
        )


class Jieshoujzk(ORMBase):
    """Database-backed implementation of IFashej
    """
    implements(IJieshoujzk)

    __tablename__ = 'jieshoujzk'

    jieshoujzkId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )
    lib_code = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    lib_name = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )


class IFashejzk(Interface):
    """发射机子库
    """
    fashejzkId = schema.Int(
            title=_(u"table primary key"),
        )
    lib_code = schema.TextLine(
            title=_(u"zi ku dai ma"),
        )
    lib_name = schema.TextLine(
            title=_(u"zi ku ming cheng"),
        )


class Fashejzk(ORMBase):
    """Database-backed implementation of IFashej
    """
    implements(IFashejzk)

    __tablename__ = 'fashejzk'

    fashejzkId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )
    lib_code = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    lib_name = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
#  add by yanghaa for other datebase templates comment to help nav
# 测试实验室start
class ICeshishysh(Interface):
    """测试实验室
    """
    ceshishyshId = schema.Int(
            title=_(u"talbe primary key")
        )
    name = schema.TextLine(
            title=_(u"ming cheng")
        )
    unit = schema.TextLine(
            title=_(u"dan wei")
        )
    level1 = schema.TextLine(
            title=_(u"ji bie")
        )
    survey = schema.TextLine(
            title=_(u"gai kuang")
        )

class Ceshishysh(ORMBase):
    """Database-backed implementation of ICeshishysh
    """
    implements(ICeshishysh)

    __tablename__ = 'ceshishysh'

    ceshishyshId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )
    name = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    unit = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    level1 = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    survey = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
# 测试实验室end

# 测试人员start
class ICeshiry(Interface):
    """测试人员
    """
    ceshiryId = schema.Int(
            title=_(u"talbe primary key")
        )
    name = schema.TextLine(
            title=_(u"xing ming")
        )
    sex = schema.TextLine(
            title=_(u"xing bie")
        )
    age = schema.Int(
            title=_(u"nian ling")
        )
    edu_level = schema.TextLine(
            title=_(u"xue li")
        )
    post = schema.TextLine(
            title=_(u"zhi cheng")
        )
    certificate_code = schema.TextLine(
            title=_(u"zheng shu bian hao")
        )
    unit = schema.TextLine(
            title=_(u"dan wei")
        )

class Ceshiry(ORMBase):
    """Database-backed implementation of ICeshiry
    """
    implements(ICeshiry)

    __tablename__ = 'ceshiry'

    ceshiryId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )
    name = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    sex = sqlalchemy.schema.Column(sqlalchemy.types.String(2),
            nullable=False,
        )
    age = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            nullable=False,
        )
    edu_level = sqlalchemy.schema.Column(sqlalchemy.types.String(8),
            nullable=False,
        )
    post = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    certificate_code = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    unit = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
# 测试人员end

# 测试方法start
class ICeshiff(Interface):
    """测试方法
    """
    ceshiffId = schema.Int(
            title=_(u"talbe primary key")
        )
    m_id = schema.TextLine(
            title=_(u"fang fa bian hao")
        )
    m_title = schema.TextLine(
            title=_(u"fang fa biao ti")
        )
    range1 = schema.TextLine(
            title=_(u"shi yong fan wei")
        )
    device = schema.TextLine(
            title=_(u"yi qi she bei")
        )
    diagram = schema.TextLine(
            title=_(u"ce shi kuang tu")
        )
    step = schema.TextLine(
            title=_(u"ce shi bu zhou")
        )
    annotation = schema.TextLine(
            title=_(u"fu zhu")
        )

class Ceshiff(ORMBase):
    """Database-backed implementation of ICeshiff
    """
    implements(ICeshiff)

    __tablename__ = 'ceshiff'

    ceshiffId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )
    m_id = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    m_title = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    range1 = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    device = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    diagram = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    step = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    annotation = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
# 测试方法end

# 测试报告start
class ICeshibg(Interface):
    """测试报告
    """
    ceshibgId = schema.Int(
            title=_(u"talbe primary key")
        )
    t_id = schema.TextLine(
            title=_(u"ce shi zheng shu bian hao")
        )
    bailor = schema.TextLine(
            title=_(u"wei tuo fang")
        )
    address = schema.TextLine(
            title=_(u"wei tuo fang di zhi")
        )
    device = schema.TextLine(
            title=_(u"bei ce jian")
        )
    eut_id = schema.TextLine(
            title=_(u"EUT bian hao")
        )
    eut_type = schema.TextLine(
            title=_(u"EUT xing hao")
        )
    manufacturor = schema.TextLine(
            title=_(u"zhi zao shang")
        )
    t_date = schema.DateTime(
            title=_(u"ce shi ri qi")
        )
    t_address = schema.TextLine(
            title=_(u"ce shi di dian")
        )
    t_device = schema.TextLine(
            title=_(u"ce shi she bei")
        )
    t_device_type = schema.TextLine(
            title=_(u"ce shi she bei xing hao")
        )
    t_device_id = schema.TextLine(
            title=_(u"ce shi she bei bian hao")
        )
    reference = schema.TextLine(
            title=_(u"ce shi yi ju")
        )
    temp = schema.Float(
            title=_(u"wen du")
        )
    huminitily = schema.Float(
            title=_(u"shi du")
        )
    t_man = schema.TextLine(
            title=_(u"ce shi ren yuan")
        )
    signer = schema.TextLine(
            title=_(u"qian fa ren")
        )
    assessor = schema.TextLine(
            title=_(u"shen he ren")
        )
    t_result = schema.TextLine(
            title=_(u"ce shi jie guo")
        )

class Ceshibg(ORMBase):
    """Database-backed implementation of ICeshibg
    """
    implements(ICeshibg)

    __tablename__ = 'ceshibg'

    ceshibgId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )
    t_id = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    bailor = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    address = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    device = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    eut_id = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    eut_type = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    manufacturor = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    t_date = sqlalchemy.schema.Column(sqlalchemy.types.DateTime(),
            nullable=False,
        )
    t_address = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    t_device = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    t_device_type = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    t_device_id = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    reference = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    temp = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='3,1'),
            nullable=False,
        )
    huminitily = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='2,1'),
            nullable=False,
        )
    t_man = sqlalchemy.schema.Column(sqlalchemy.types.String(10),
            nullable=False,
        )
    signer = sqlalchemy.schema.Column(sqlalchemy.types.String(10),
            nullable=False,
        )
    assessor = sqlalchemy.schema.Column(sqlalchemy.types.String(10),
            nullable=False,
        )
    t_result = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
# 测试报告end

# 测试项目start
class ICeshixm(Interface):
    """测试报告
    """
    ceshixmId = schema.Int(
            title=_(u"talbe primary key")
        )
    project_id = schema.Int(
            title=_(u"bei ce xiang mu bian hao")
        )
    device = schema.TextLine(
            title=_(u"bei ce jian")
        )
    name = schema.TextLine(
            title=_(u"xiang mu ming cheng")
        )
    diagram = schema.TextLine(
            title=_(u"shi yi tu")
        )
    t_remark = schema.TextLine(
            title=_(u"ce shi shuo ming")
        )
    t_strument = schema.TextLine(
            title=_(u"ce shi yi qi")
        )
    t_value = schema.TextLine(
            title=_(u"ce shi shu ju")
        )
    t_result = schema.TextLine(
            title=_(u"ce shi shu ju")
        )

class Ceshixm(ORMBase):
    """Database-backed implementation of ICeshibxm
    """
    implements(ICeshixm)

    __tablename__ = 'ceshixm'

    ceshixmId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )
    project_id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            nullable=False,
        )
    device = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    name = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    diagram = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    t_remark = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    t_strument = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    t_value = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    t_result = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
# 测试项目end
