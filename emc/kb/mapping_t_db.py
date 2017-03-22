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

class IDanwei(Interface):
    """docstring for IDanwei."""
    danweiId = schema.Int(
            title=_(u"danwei talbe primary key"),
        )
    danweimc = schema.TextLine(
            title=_(u"dan wei ming cheng"),
        )
    danweidz = schema.TextLine(
            title=_(u"dan wei di zhi"),
        )
    danweilxfs = schema.TextLine(
            title=_(u"dan wei lian xi fang shi"),
        )

class Danwei(ORMBase):
    """docstring for Danwei."""
    implements(IDanwei)
    __tablename__ = 'danwei'
    danweiId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )
    danweimc = sqlalchemy.schema.Column(sqlalchemy.types.String(64),
            nullable=False,
        )
    danweidz = sqlalchemy.schema.Column(sqlalchemy.types.String(64),
            nullable=False,
        )
    danweilxfs = sqlalchemy.schema.Column(sqlalchemy.types.String(64),
            nullable=False,
        )
