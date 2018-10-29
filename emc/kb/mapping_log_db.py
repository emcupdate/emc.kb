#-*- coding: UTF-8 -*-
import sqlalchemy.types
import sqlalchemy.schema
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship, backref
from sqlalchemy import Sequence
from five import grok
from zope import schema
from zope.interface import Interface,implements
from emc.kb import ORMBase
from emc.kb import _


class IAdminLog(Interface):
    """管理员操作日志
    """
    id = schema.Int(
            title=_(u"the table's primary key"),
        )
    # 主体
    adminid = schema.TextLine(
            title=_(u"administrator's user id"),
        )
    #客体
    userid = schema.TextLine(
            title=_(u"the user id of user which had been processed by administrator"),
        )
    #操作时间
    datetime = schema.TextLine(
            title=_(u"operation time"),
        )
    ip = schema.TextLine(
            title=_(u"the client's ip address"),
        )
    type = schema.Int(
            title=_(u"type of the operation"),
        )
    operlevel = schema.Int(
            title=_(u"level of the operation"),
        )
    description = schema.Text(
            title=_(u"the operation's detail description"),
        )    
    result = schema.Int(
            title=_(u"result of the operation"),
        )        
class AdminLog(ORMBase):
    """Database-backed implementation of IModel
    """
    implements(IAdminLog)

    __tablename__ = 'admin_logs'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('log_id_seq'),
            primary_key=True,
            autoincrement=True,
        )
    adminid = sqlalchemy.schema.Column(sqlalchemy.types.String(128),
            nullable=False,
        )
    userid = sqlalchemy.schema.Column(sqlalchemy.types.String(128),
            nullable=False,
        )
    datetime = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    ip = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    type = sqlalchemy.schema.Column(sqlalchemy.types.SmallInteger,
            nullable=False,
        )
    operlevel = sqlalchemy.schema.Column(sqlalchemy.types.SmallInteger,
            nullable=False,
        )
    description = sqlalchemy.schema.Column(sqlalchemy.types.String(128),
            nullable=False,
        )     
    result = sqlalchemy.schema.Column(sqlalchemy.types.SmallInteger,
            nullable=False,
        )                         

