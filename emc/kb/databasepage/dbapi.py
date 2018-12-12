#-*- coding: UTF-8 -*-
from five import grok
from datetime import datetime
from zope import schema
from zope.interface import implements
#sqlarchemy
from sqlalchemy import text
from sqlalchemy import func
from emc.kb import log_session as session
from emc.kb.interfaces import IDbapi
import datetime
from emc.policy import fmt
from emc.kb import _

class Dbapi(object):
    """db API base class"""
    implements(IDbapi)
    
    def __init__(self,session,package,table,factorycls,columns=None,fullsearch_clmns=None):
        """
        parameters:
        :session db mapper session,
        :package the package where table class in here. for example:'emc.kb.mapping_log_db',
        :table the table name that will be query, 'admin_logs',
        :factorycls the class name that will be create table object instance,'AdminLog',
        :columns will return table columns,
        :fullsearch_clmns the columns that will been used keyword full text search
        """
        
        self.session = session
        self.package = package
        self.table = table
        self.factorycls = factorycls
        self.columns = columns
        self.fullsearch_clmns = fullsearch_clmns
        
        import os
        os.environ['NLS_LANG'] = '.AL32UTF8'        


    def search_clmns2sqltxt(self,clmns):
        """get columns that will been used keyword full text search
        :input:clmns = ['tit','des']
        :output:" tit LIKE :x OR des LIKE :x "
                                  
        """
        if self.fullsearch_clmns == None:
            return ""                       
        else:
            srt=''
            for i in clmns:
                if not bool(srt):
                    srt = "%(c)s LIKE :x" % dict(c=i)
                    continue
                else:
                    srt = "%(pre)s OR %(c)s LIKE :x" % dict(c=i,pre=srt)
            return srt        
        
    def get_columns(self):
        "get return columns by query"
        
        if self.columns == None:
            import_str = "from %(p)s import %(t)s as tablecls" % dict(p=self.package,t=self.factorycls) 
            exec import_str
            from sqlalchemy.inspection import inspect
            table = inspect(tablecls)
            columns = [column.name for column in table.c]
            return columns                        
        else:
            return self.columns            
            
    def add(self,kwargs):
        
        import_str = "from %(p)s import %(t)s as tablecls" % dict(p=self.package,t=self.factorycls) 
        exec import_str
        recorder = tablecls()
        for kw in kwargs.keys():
            setattr(recorder,kw,kwargs[kw])
        session.add(recorder)
        try:
            session.commit()
        except:
            session.rollback()
            

    def query(self,kwargs):
        """分页查询
        columns = request.args.getlist('columns')
        stmt = select([column(c) for c in columns]).\
    select_from(some_table)
    stmt = select([table.c[c] for c in columns])
    results = db.session.execute(stmt).fetchall()
    session.query.with_entities(SomeModel.col1)
        """
        
        import_str = "from %(p)s import %(t)s as tablecls" % dict(p=self.package,t=self.factorycls) 
        exec import_str        
        start = int(kwargs['start']) 
        size = int(kwargs['size'])
        max = size + start + 1 
        keyword = kwargs['SearchableText']        
        direction = kwargs['sort_order'].strip()        

        if size != 0:
            if keyword == "":
                if direction == "reverse":
                    sqltext = """select * from 
                    (select a.*,rownum rn from 
                    (select * from %s ORDER BY id DESC) a  
                    where rownum < :max) where rn > :start""" % self.table
                    selectcon = text(sqltext)
                else:
                    sqltext = """select * from 
                    (select a.*,rownum rn from 
                    (select * from %s ORDER BY id ASC) a  
                    where rownum < :max) where rn > :start""" % self.table                    
                    selectcon = text(sqltext)                    
                clmns = self.get_columns()
                recorders = session.query(tablecls).with_entities(*clmns).\
                            from_statement(selectcon.params(start=start,max=max)).all()
            else:
                keysrchtxt = self.search_clmns2sqltxt(self.fullsearch_clmns)
                if direction == "reverse":                    
                    sqltxt = """SELECT * FROM
                    (SELECT a.*,rownum rn FROM 
                    (SELECT * FROM %(tbl)s WHERE %(ktxt)s  ORDER BY id DESC ) a 
                     WHERE rownum < :max) WHERE rn > :start
                    """ % dict(tbl=self.table,ktxt=keysrchtxt)
                    selectcon = text(sqltxt)
                else:
                    sqltxt = """SELECT * FROM
                    (SELECT a.*,rownum rn FROM 
                    (SELECT * FROM %(tbl)s WHERE %(ktxt)s  ORDER BY id ASC ) a 
                     WHERE rownum < :max) WHERE rn > :start
                    """ % dict(tbl=self.table,ktxt=keysrchtxt)                    
                    selectcon = text(sqltxt)
                clmns = self.get_columns()
                recorders = session.query(tablecls).with_entities(*clmns).\
                                      from_statement(selectcon.params(x=keyword,start=start,max=max)).all()               
        else:
            if keyword == "":
                selectcon = text("SELECT * FROM %s ORDER BY id DESC " % self.table)
                clmns = self.get_columns()
                recorders = session.query(tablecls).with_entities(*clmns).\
                            from_statement(selectcon).all()
            else:
                keysrchtxt = self.search_clmns2sqltxt(self.fullsearch_clmns)
                sqltext = """SELECT * FROM %(tbl)s WHERE %(ktxt)s  
                 ORDER BY id DESC """ % dict(tbl=self.table,ktxt=keysrchtxt)
                selectcon = text(sqltext)
                clmns = self.get_columns()
                recorders = session.query(tablecls).with_entities(*clmns).\
                                      from_statement(selectcon.params(x=keyword)).all()                         
            nums = len(recorders)
            return nums
        try:
            return recorders
        except:
            return []    
        
    def DeleteByCode(self,id):
        "delete the specify id recorder"
        import_str = "from %(p)s import %(t)s as tablecls" % dict(p=self.package,t=self.factorycls) 
        exec import_str
        if id != "":
            sqltext = "SELECT * FROM %(tbl)s WHERE id=:id" % dict(tbl=self.table) 
            try:
                recorder = session.query(tablecls).\
                from_statement(text(sqltext)).\
                params(id=id).one()
                session.delete(recorder)
                session.commit()
                return True
            except:
                session.rollback()
                return False
        else:
            return None

    def getByCode(self,id):
        import_str = "from %(p)s import %(t)s as tablecls" % dict(p=self.package,t=self.factorycls) 
        exec import_str        
        if id != "":
            sqltext = "SELECT * FROM %(tbl)s WHERE id=:id" % dict(tbl=self.table)            
            try:
                recorder = session.query(tablecls).\
                from_statement(text(sqltext)).\
                params(id=id).one()
                return recorder
            except:
#                 session.rollback()
                return None
        else:
            return None
    
    def get_rownumber(self):
        "fetch table's rownumber"
#         query = "SELECT COUNT(*) FROM %(table)s;" % dict(table=self.table)
        import_str = "from %(p)s import %(t)s as tablecls" % dict(p=self.package,t=self.factorycls) 
        exec import_str
        try:
            num = self.session.query(func.count(tablecls.id)).scalar()         
            return num
        except:
            return 0            

    def fetch_oldest(self):
        "delete from(select * from <table_name>) where rownum<=1000;"
        
        s = self.session
        sql2 = """ 
        select datetime from (
          select * from %(tbl)s order by id asc
         )
          where rownum<= 1
        """ % dict(tbl=self.table)
        query2 = text(sql2)                                                                                                
        try:
            rownum = s.execute(query2).fetchone()
            if len(rownum):
                return datetime.strptime(rownum[0],fmt) 
            else:
                return datetime.datetime.now()
#             s.commit()
        except:
            return datetime.datetime.now()
    
    def bulk_delete(self,size):
        "delete from(select * from <table_name>) where rownum<=1000;"
        
        s = self.session
        sql2 = """
        delete %(tbl)s
         where  id in (
        select id from (
          select * from %(tbl)s order by id asc
         )
          where rownum<= :max
        )
        """ % dict(tbl=self.table)
        query2 = text(sql2).params(max=size)                                                                                                 
        try:
            rownum = s.execute(query2)
            s.commit()
        except:
            s.rollback()
        
adminlog = Dbapi(session,'emc.kb.mapping_log_db','admin_logs','AdminLog')
userlog =  Dbapi(session,'emc.kb.mapping_log_db','user_logs','UserLog')
model_sch = ['xhmc','xhdm']
model = Dbapi(session,'emc.kb.mapping_db','model','Model',fullsearch_clmns=model_sch)
fashejclmns = ['id','sbdm','sbmc','pcdm','location','freq','pd_upper','pd_lower','num','freq_upper',
               'freq_lower']
fashej_sch = ['sbdm','sbmc']
fashej = Dbapi(session,'emc.kb.mapping_db','para_fashej','Fashej',columns=fashejclmns,fullsearch_clmns=fashej_sch)
 