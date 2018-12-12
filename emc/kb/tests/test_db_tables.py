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

    def test_drop_tables(self):
        """create all db tables
        employees.drop(engine)
        employees.create(engine)
        """

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
