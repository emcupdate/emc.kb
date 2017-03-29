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
            # nullable=False,
        )
    danweilxfs = sqlalchemy.schema.Column(sqlalchemy.types.String(64),
            # nullable=False,
        )

class IT_ry(Interface):
    """docstring for IT_ry."""
    t_ryId = schema.Int(
            title=_(u"ce shi ren yuan talbe primary key"),
        )
    t_ryname = schema.TextLine(
            title=_(u"ce shi ren yuan ming cheng"),
        )
    t_rygender = schema.TextLine(
            title=_(u"ce shi ren yuan xing bie"),
        )
    t_ryage = schema.Int(
            title=_(u"ce shi ren yuan nian ling"),
        )
    t_rydegree = schema.TextLine(
            title=_(u"ce shi ren yuan xue li"),
        )
    t_rytitle = schema.TextLine(
            title=_(u"ce shi ren yuan zhi cheng"),
        )
    t_rynumber= schema.TextLine(
            title=_(u"ce shi ren yuan zheng shu bian hao"),
        )
    f_danweimc = schema.Object(
            title=_(u"ce shi ren yuan dan wei ID"),
            schema=IDanwei,
        )

class T_ry(ORMBase):
    """docstring for T_ry."""

    implements(IT_ry)

    __tablename__ = 't_ry'

    t_ryId = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            primary_key=True,
            autoincrement=True,
        )
    t_ryname = sqlalchemy.schema.Column(sqlalchemy.types.String(64),
            nullable=False,
        )
    t_rygender = sqlalchemy.schema.Column(sqlalchemy.types.String(8),
            nullable=False,
        )
    t_ryage = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            nullable=False,
        )
    t_rydegree = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    t_rytitle = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    t_rynumber = sqlalchemy.schema.Column(sqlalchemy.types.String(32),

        )
    t_ry_f_dwId = sqlalchemy.schema.Column(
            ForeignKey(danwei.danweiId)
        )

    f_danweimc = relationship("Danwei",backref="danwei",order_by="Danwei.danweiId")
