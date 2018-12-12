#-*- coding: UTF-8 -*-
import datetime
import unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from emc.kb.testing import INTEGRATION_TESTING
#sqlarchemy
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
import datetime
from emc.policy import fmt
from emc.kb.interfaces import IDbapi
from zope.component import queryUtility
from emc.kb import log_session as Session
from emc.kb import ora_engine as engine


class TestDatabase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def drop_tables(self,tbls=None):
        """create all db tables
        employees.drop(engine)
        employees.create(engine)
        """

        if tbls == None:
            tbls = ['Fashej','Jieshouj','Fashetx','Jieshoutx','Lvboq','Dianxingtxzyzk',
                'Tianxianzk','Jieshoujzk','Fashejzk','Ceshishysh',
                'Ceshiry','Ceshiff','Ceshibg','Ceshixm']
        for tb in tbls:
            import_str = "from %(p)s import %(t)s as tablecls" % dict(p='emc.kb.mapping_db',t=tb) 
            exec import_str
            tablecls.__table__.drop(engine)                    

    def create_tables(self,tbls=None):
        """create all db tables
        employees.drop(engine)
        employees.create(engine)
        """

        if tbls == None:
            tbls = ['Model','Fashej','Jieshouj','Fashetx','Jieshoutx','Lvboq','Dianxingtxzyzk',
                'Tianxianzk','Jieshoujzk','Fashejzk','Ceshishysh',
                'Ceshiry','Ceshiff','Ceshibg','Ceshixm']
        for tb in tbls:
            import_str = "from %(p)s import %(t)s as tablecls" % dict(p='emc.kb.mapping_db',t=tb) 
            exec import_str
            tablecls.__table__.create(engine)

    def test_dbapi_fashej(self):

        import os
        os.environ['NLS_LANG'] = '.AL32UTF8'            
#         self.create_tables(tbls=['Fashej'])
#         self.drop_tables(tbls=['Fashej'])
#         import pdb
#         pdb.set_trace()
        
# ('333333002','发射机01','asd2w23sds212211111','m',2.4,0,2.8,10,0,2.8,20,1.1,'AM-V',2,1,' 常用发射机1')
        values = dict(sbdm="333333002",sbmc=u"发射机01",pcdm="asd2w23sds212211111",location=u"m",
                      freq=2.4,pd_upper=0,pd_lower=2.8,num=10,
                      freq_upper=0,freq_lower=2.8,bw=20,base_power=1.1,
                      tzlx="AM-V",bzf=2,mid_freq=1,comment1=u"常用发射机1")        
        dbapi = queryUtility(IDbapi, name='fashej')
        dbapi.add(values)
        import pdb
        pdb.set_trace()
        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})
        import pdb
        pdb.set_trace()
        id = nums[0].id        
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)

    def test_dbapi_jieshouj(self):

        import os
        os.environ['NLS_LANG'] = '.AL32UTF8'            
#         self.create_tables(tbls=['Jieshouj'])
#         self.drop_tables(tbls=['Jieshouj'])
#         import pdb
#         pdb.set_trace()
        
#('sb-1234','接收机1','sb-1234-1','m',1800,900,300,1500,1000,50000,-90,'1',300,1500)
        values = dict(sbdm="sb-1234",sbmc=u"接收机1",pcdm="sb-1234-1",location=u"m",
                      fb_upper=1800,fb_lower=900,freq=300,f_upper=1500,
                      f_lower=1000,bw_receiver=50000,sen_receiver=-90,mf_freq_sign='1',
                      mf_freq=300,lo_freq=1500)        
        dbapi = queryUtility(IDbapi, name='jieshouj')
        dbapi.add(values)
        import pdb
        pdb.set_trace()
        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})
        import pdb
        pdb.set_trace()
        id = nums[0].id        
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)
 
    def test_dbapi_fashetx(self):

        import os
        os.environ['NLS_LANG'] = '.AL32UTF8'            
#         self.create_tables(tbls=['Fashetx'])
#         self.drop_tables(tbls=['Fashetx'])
#         import pdb
#         pdb.set_trace()
        
# ('sb-1234','接收天线1','pc-1-pass','m',10.2,'Ver',30,20,10)
        values = dict(cssbdm="sb-1234",cssbmc=u"接收天线1",pcdm="pc-1-pass",location=u"m",
                      gain=10.2,polarization='Ver',fwbskd=30,fybskd=20,txzxj=10)        
        dbapi = queryUtility(IDbapi, name='fashetx')
        dbapi.add(values)
        import pdb
        pdb.set_trace()
        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})
        import pdb
        pdb.set_trace()
        id = nums[0].id        
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)
 
    def test_dbapi_jieshoutx(self):

        import os
        os.environ['NLS_LANG'] = '.AL32UTF8'            
#         self.create_tables(tbls=['Jieshoutx'])
#         self.drop_tables(tbls=['Jieshoutx'])
        import pdb
        pdb.set_trace()
        
# ('sb-1234','接收天线1','pc-1-pass','m',10.2,'Ver',30,20,10)
        values = dict(cssbdm="sb-1234",cssbmc=u"接收天线1",pcdm="pc-1-pass",location=u"m",
                      gain=10.2,polarization='Ver',fwbskd=30,fybskd=20,txzxj=10)        
        dbapi = queryUtility(IDbapi, name='fashetx')
        dbapi.add(values)
        import pdb
        pdb.set_trace()
        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})
        import pdb
        pdb.set_trace()
        id = nums[0].id        
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)

    def test_dbapi_lvboq(self):

        import os
        os.environ['NLS_LANG'] = '.AL32UTF8'            
        self.create_tables(tbls=['Lvboq'])
#         self.drop_tables(tbls=['Lvboq'])
        import pdb
        pdb.set_trace()
        
# ('sb-1234','滤波器1','pc-1-pass','m',1500,1600,1400,5,1.5)
        values = dict(cssbdm="sb-1234",cssbmc=u"滤波器1",pcdm="pc-1-pass",location=u"m",
                      freq=1500,f_upper=1600,f_lower=1400,order1=5,s21=1.5)        
        dbapi = queryUtility(IDbapi, name='lvboq')
        dbapi.add(values)
        import pdb
        pdb.set_trace()
        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})
        import pdb
        pdb.set_trace()
        id = nums[0].id        
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)
                   
    def test_dbapi_add(self):

        import os
        os.environ['NLS_LANG'] = '.AL32UTF8'        
#         Model.__table__.drop(engine)
#         Model.__table__.create(engine)      
        values = dict(xhdm="a10",xhmc=u"计算机")        
        dbapi = queryUtility(IDbapi, name='model')
        dbapi.add(values)
        import pdb
        pdb.set_trace()
        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})
        import pdb
        pdb.set_trace()
        id = nums[0].id        
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)
