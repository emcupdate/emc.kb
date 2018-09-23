#-*- coding: UTF-8 -*-
from five import grok
from datetime import datetime
from zope import schema
from zope.interface import implements
#sqlarchemy
from sqlalchemy import text
from sqlalchemy import func

from emc.kb import log_session as session

from emc.kb.mapping_db import AdminLog,IAdminLog
from emc.kb.interfaces import IAdminLogLocator

from emc.kb import _

class AdminLogLocator(grok.GlobalUtility):
    """docstring for AdminLogLocator."""
    implements(IAdminLogLocator)

    def add(self,kwargs):
        recorder = AdminLog()
        for kw in kwargs.keys():
            setattr(recorder,kw,kwargs[kw])
        session.add(recorder)
        try:
            session.commit()
        except:
            session.rollback()
            pass

    def query(self,**kwargs):
        """以分页方式提取Danwei 记录，参数：start 游标起始位置；size:每次返回的记录条数;
        fields:field list
        if size = 0,then不分页，返回所有记录集
        order_by(text("id"))
        """

        start = int(kwargs['start'])
        size = int(kwargs['size'])

        if size != 0:
            recorders = session.query("adminid","userid","datetime",
                                      "ip","type","level","description","result").\
            from_statement(
            text("select * from AdminLog  order by id desc limit :start,:size").\
            params(start=start,size=size)).all()
        else:
            nums = session.query(func.count(AdminLog.id)).scalar()
            return int(nums)
        try:
            session.commit()
            return recorders
        except:
            session.rollback()
            pass


