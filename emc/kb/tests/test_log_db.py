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

class TestLogDatabase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def test_db_mapping_model(self):
        from emc.kb.mapping_log_db import  AdminLog
        from emc.kb import log_session as Session
        from emc.kb import ora_engine as engine
        import os
        os.environ['NLS_LANG'] = '.AL32UTF8'
        Base = declarative_base()
        import pdb
        pdb.set_trace()
#         Base.metadata.create_all(engine)
        adminlog = AdminLog()
#         AdminLog.id = 9
        adminlog.adminid = u"admin4"
        adminlog.userid = u" "
        adminlog.datetime = "2018-10-12 20:12:35"
        adminlog.ip = u"192.168.3.101"
        adminlog.type = 0
        adminlog.operlevel = 5
        adminlog.result = 1
        adminlog.description = u"admin2 删除 user2"

        Session.add(adminlog)
        Session.flush()
        nums = Session.query(func.count(AdminLog.id)).scalar()
        self.assertTrue(AdminLog.id is not None)
#         self.assertEqual(int(nums),3)
        Session.commit()
        Session.rollback()

 
    def test_model_locator(self):
        from emc.kb.mapping_db import  AdminLog
        from emc.kb.interfaces import IAdminLogLocator
        from zope.component import getUtility
#         from emc.kb import log_session as Session

        locator = getUtility(IAdminLogLocator)
        #getModel
        values = {'id':2,'adminid':'admin','userid':'user3','datetime':'2018-09-22 20:12:35',
                  'ip':u"192.168.3.101",'type':0,'operlevel':4,'result':1,'description':u'admin删除了用户user3'}                


        record = locator.getByCode(1)
        #add
        import pdb
        pdb.set_trace()
        # remove old  delete

        locator.add(values)
        record = locator.getByCode(2)
        self.assertEqual(int(record.id),2)
        # query pagenation 分页查询
        recorders = locator.query(start=0,size=1)
        import pdb
        pdb.set_trace()
        self.assertEqual(len(recorders),1)


