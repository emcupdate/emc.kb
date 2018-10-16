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

class dbLocator(object):
    """db locator base class"""
    
    def __init__(self,package,table,factorycls):
        self.package = package
        self.table = table
        self.factorycls = factorycls
        
class AdminLogLocator(grok.GlobalUtility):
    """docstring for AdminLogLocator."""
    implements(IAdminLogLocator)

    def add(self,kwargs):
#         try:
#             tablename = kwargs['table']
#             exec("from %s import %s as tablecls"%(self.package,self.table))
#         except:
#             pass
        recorder = AdminLog()
        for kw in kwargs.keys():
            setattr(recorder,kw,kwargs[kw])
        session.add(recorder)
        try:
            session.commit()
        except:
            session.rollback()
            pass

    def query(self,kwargs):
        """以分页方式提取记录，参数：start 游标起始位置；size:每次返回的记录条数;
        fields:field list
        if size = 0,then不分页，返回所有记录集
        order_by(text("id"))
        """

        start = int(kwargs['start'])
        size = int(kwargs['size'])
        keyword = kwargs['SearchableText']
        direction = kwargs['sort_order'].strip()        

        if size != 0:
            if keyword == "":
                if direction == "reverse":
                    selectcon = text("select * from admin_logs  order by id desc limit :start,:size")
                else:
                    selectcon = text("select * from admin_logs  order by id asc limit :start,:size")
                recorders = session.query("adminid","userid","datetime",
                                      "ip","type","level","description","result").\
                            from_statement(selectcon.params(start=start,size=size)).all()
            else:
                if direction == "reverse":
                    selectcon = text("select * from admin_logs where"
                                 " description LIKE :x "
                                  " OR userid LIKE :x"
                                  " OR adminid LIKE :x"
                                  " OR level LIKE :x"
                                  " OR result LIKE :x"
                                  " OR ip LIKE :x"
                                  " order by id DESC limit :start,:size")
                else:
                    selectcon = text("select * from admin_logs where"
                                 " description LIKE :x "
                                  " OR userid LIKE :x"
                                  " OR adminid LIKE :x"
                                  " OR level LIKE :x"
                                  " OR result LIKE :x"
                                  " OR ip LIKE :x"
                                  " order by id ASC limit :start,:size")
                recorders = session.query("adminid","userid","datetime",
                                      "ip","type","level","description","result").\
                                      from_statement(selectcon.params(x=keyword,start=start,size=size)).all()  
                
        else:
            if keyword == "":
                selectcon = text("select * from admin_logs  order by id desc ")
                recorders = session.query("adminid","userid","datetime",
                                      "ip","type","level","description","result").\
                            from_statement(selectcon).all()
            else:
                selectcon = text("select * from admin_logs where"
                                 " description LIKE :x "
                                  " OR userid LIKE :x"
                                  " OR adminid LIKE :x"
                                  " OR level LIKE :x"
                                  " OR result LIKE :x"
                                  " OR ip LIKE :x"
                                  " order by id DESC ")

                recorders = session.query("adminid","userid","datetime",
                                      "ip","type","level","description","result").\
                                      from_statement(selectcon.params(x=keyword)).all()  
            
            
            nums = len(recorders)
            return nums
        try:
            session.commit()
            return recorders
        except:
            session.rollback()
            pass


    def DeleteByCode(self,id):
        "delete the specify id recorder"

#         xhdm = kwargs['xhdm']
        if id != "":
            try:
                recorder = session.query(AdminLog).\
                from_statement(text("SELECT * FROM admin_logs WHERE id=:id")).\
                params(id=id).one()
                session.delete(recorder)
                session.commit()
            except:
                session.rollback()
                pass
        else:
            return None

    def getByCode(self,id):
        if id != "":
            try:
                recorder = session.query(AdminLog).\
                from_statement(text("SELECT * FROM admin_logs WHERE id=:id")).\
                params(id=id).one()
                return recorder
            except:
                session.rollback()
                None
        else:
            return None


