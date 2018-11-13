#-*- coding: UTF-8 -*-
from five import grok
from datetime import datetime
from zope import schema
from zope.interface import implements
#sqlarchemy
from sqlalchemy import text
from sqlalchemy import func

from emc.kb import log_session as session

from emc.kb.mapping_log_db import UserLog,IUserLog
from emc.kb.interfaces import IUserLogLocator

from emc.kb import _

class dbLocator(object):
    """db locator base class"""
    
    def __init__(self,package,table,factorycls):
        self.package = package
        self.table = table
        self.factorycls = factorycls
        
class UserLogLocator(grok.GlobalUtility):
    """docstring for UserLogLocator."""
    implements(IUserLogLocator)

    def add(self,kwargs):
#         try:
#             tablename = kwargs['table']
#             exec("from %s import %s as tablecls"%(self.package,self.table))
#         except:
#             pass
        import os
        os.environ['NLS_LANG'] = '.AL32UTF8'
        recorder = UserLog()
        for kw in kwargs.keys():
            setattr(recorder,kw,kwargs[kw])
#         if recorder.id == None:recorder.id = 1
#         import pdb
#         pdb.set_trace()
        session.add(recorder)
#         Session.flush()
        try:
            session.commit()
        except:
#             session.rollback()
            pass

    def query(self,kwargs):
        """以分页方式提取记录，参数：start 游标起始位置；size:每次返回的记录条数;
        fields:field list
        if size = 0,then不分页，返回所有记录集
        order_by(text("id"))
        --------------------------------
        //page是当前页序数，rows是显示行数
        int page=2;
        int rows=5;                            
        List<Articles> list=a.select(page*rows+1，(page-1)*rows);
        //  sql语句：  
        select * from(select a.*,rownum rn from (select * from t_articles) a where rownum < 11) where rn>5
　　　　　　//第一个参数，对应着第一个rownum<11,第二个参数对应着rn>5
        --------------------------------        
        """

        start = int(kwargs['start']) 
        size = int(kwargs['size'])
#         import pdb
#         pdb.set_trace()
        max = size + start + 1 
        keyword = kwargs['SearchableText']
        import os
        os.environ['NLS_LANG'] = '.AL32UTF8'        
        direction = kwargs['sort_order'].strip()        

        if size != 0:
            if keyword == "":
                if direction == "reverse":
                    selectcon = text("select * from"
                                     "(select a.*,rownum rn from "
                                     "(select * from user_logs ORDER BY id DESC) a "
                                     "where rownum < :max) where rn > :start")
                    
#                     selectcon = text("select * from admin_logs  ORDER BY id DESC")
                else:
                    selectcon = text("select * from"
                                     "(select a.*,rownum rn from "
                                     "(select * from user_logs ORDER BY id ASC) a "
                                     "where rownum < :max) where rn > :start")                    
#                     selectcon = text("select * from admin_logs  ORDER BY id ASC LIMIT :start,:size")

                recorders = session.query("userid","datetime",
                                      "ip","type","operlevel","description","result").\
                            from_statement(selectcon.params(start=start,max=max)).all()
            else:
                if direction == "reverse":
                    selectcon = text("select * from"
                                "(select a.*,rownum rn from "
                                "(select * from user_logs where"
                                 " description LIKE :x "
                                  " OR userid LIKE :x"
                                  " OR operlevel LIKE :x"
                                  " OR result LIKE :x"
                                  " OR ip LIKE :x"
                                  " ORDER BY id DESC ) a "
                                  "where rownum < :max) where rn > :start"
                                  )
                else:
                    selectcon = text("select * from"
                                "(select a.*,rownum rn from "
                                "(select * from user_logs where"
                                 " description LIKE :x "
                                  " OR userid LIKE :x"
                                  " OR operlevel LIKE :x"
                                  " OR result LIKE :x"
                                  " OR ip LIKE :x"
                                  " ORDER BY id ASC ) a "
                                  "where rownum < :max) where rn > :start"
                                  )
                recorders = session.query("userid","datetime",
                                      "ip","type","operlevel","description","result").\
                                      from_statement(selectcon.params(x=keyword,start=start,max=max)).all()  
                
        else:
            if keyword == "":
                selectcon = text("select * from user_logs  order by id desc ")
                recorders = session.query("userid","datetime",
                                      "ip","type","operlevel","description","result").\
                            from_statement(selectcon).all()
            else:
                selectcon = text("select * from user_logs where"
                                 " description LIKE :x "
                                  " OR userid LIKE :x"
                                  " OR operlevel LIKE :x"
                                  " OR result LIKE :x"
                                  " OR ip LIKE :x"
                                  " order by id DESC ")

                recorders = session.query("userid","datetime",
                                      "ip","type","operlevel","description","result").\
                                      from_statement(selectcon.params(x=keyword)).all()  
            
            
            nums = len(recorders)
            return nums
        try:
#             session.commit()
            return recorders
        except:
            session.rollback()
            pass


    def DeleteByCode(self,id):
        "delete the specify id recorder"

#         xhdm = kwargs['xhdm']
        if id != "":
            try:
                recorder = session.query(UserLog).\
                from_statement(text("SELECT * FROM user_logs WHERE id=:id")).\
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
                recorder = session.query(UserLog).\
                from_statement(text("SELECT * FROM user_logs WHERE id=:id")).\
                params(id=id).one()
                return recorder
            except:
                session.rollback()
                None
        else:
            return None


