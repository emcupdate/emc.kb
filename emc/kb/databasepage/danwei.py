#-*- coding: UTF-8 -*-
from five import grok
from datetime import datetime
from zope import schema
from zope.interface import implements
#sqlarchemy
from sqlalchemy import text
from sqlalchemy import func

from emc.kb import t_session

from emc.kb.mapping_t_db import Danwei,IDanwei
from emc.kb.interfaces import IDanweiLocator

from emc.kb import _

class DanweiLocator(grok.GlobalUtility):
    """docstring for DanweiLocator."""
    implements(IDanweiLocator)

    def add(self,kwargs):
        recorder = Danwei()
        for kw in kwargs.keys():
            setattr(recorder,kw,kwargs[kw])
        t_session.add(recorder)
        try:
            t_session.commit()
        except:
            t_session.rollback()
            pass

    def query(self,**kwargs):
        """以分页方式提取Danwei 记录，参数：start 游标起始位置；size:每次返回的记录条数;
        fields:field list
        if size = 0,then不分页，返回所有记录集
        order_by(text("id"))
        """

        start = int(kwargs['start'])
        size = int(kwargs['size'])
#         fields = kwargs['fields']
        if size != 0:
            recorders = t_session.query("danweimc","danweidz","danweilxfs").\
            from_statement(
            text("select * from danwei  order by danweimc desc limit :start,:size").\
            params(start=start,size=size)).all()
        else:
            nums = t_session.query(func.count(Danwei.danweiId)).scalar()
            return int(nums)
        try:
            t_session.commit()
            return recorders
        except:
            t_session.rollback()
            pass

    def DeleteByCode(self,danweiId):
        "delete the specify danwei Danwei recorder"

#         xhdm = kwargs['xhdm']
        if danweimc != "":
            try:
                recorder = t_session.query(Danwei).\
                from_statement(text("SELECT * FROM danwei WHERE danweimc=:danweimc")).\
                params(danweimc=danweimc).one()
                t_session.delete(recorder)
                t_session.commit()
            except:
                t_session.rollback()
                pass
        else:
            return None

    def updateByCode(self,kwargs):
        "update the speicy danwei danwei recorder"

        """
        session.query(User).from_statement(text("SELECT * FROM users WHERE name=:name")).\
params(name='ed').all()
session.query(User).from_statement(
text("SELECT * FROM users WHERE name=:name")).params(name='ed').all()
        """

        danweimc = kwargs['danweiId']
        if danweimc != "":
            try:
                recorder = t_session.query(Danwei).\
                from_statement(text("SELECT * FROM danwei WHERE danweimc=:danweimc")).\
                params(danweimc=danweimc).one()
                updatedattrs = [kw for kw in kwargs.keys() if kw != 'danweimc']
                for kw in updatedattrs:
                    setattr(recorder,kw,kwargs[kw])
                t_session.commit()
            except:
                t_session.rollback()
                pass
        else:
            return None

    def getByCode(self,danweimc):
        if danweimc != "":
            try:
                recorder = t_session.query(Danwei).\
                from_statement(text("SELECT * FROM danwei WHERE danweimc=:danweimc")).\
                params(danweimc=danweimc).one()
                return recorder
            except:
                t_session.rollback()
                None
        else:
            return None
