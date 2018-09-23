#-*- coding: UTF-8 -*-
import datetime
import unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from emc.kb.testing import INTEGRATION_TESTING
#sqlarchemy
from sqlalchemy import text
from sqlalchemy import func


class TestLogDatabase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def test_db_mapping_model(self):
        from emc.kb.mapping_db import  AdminLog
        from emc.kb import log_session as Session
        AdminLog = AdminLog()
        AdminLog.id = 1
        AdminLog.adminid = u"admin"
        AdminLog.userid = u"user2"
        AdminLog.datetime = "2018-09-12 20:12:35"
        AdminLog.ip = u"192.168.3.101"
        AdminLog.type = 0
        AdminLog.level = 5
        AdminLog.result = 1
        AdminLog.description = u"admin删除了用户user2"
        Session.add(AdminLog)
        Session.flush()
        nums = Session.query(func.count(AdminLog.id)).scalar()
        self.assertTrue(AdminLog.id is not None)
        self.assertEqual(int(nums),1)

 
    def test_model_locator(self):
        from emc.kb.mapping_db import  AdminLog
        from emc.kb.interfaces import IAdminLogLocator
        from zope.component import getUtility
        from emc.kb import log_session as Session

        locator = getUtility(IAdminLogLocator)
        #getModel
        values = {'id':2,'adminid':'admin','userid':'user3','datetime':'2018-09-22 20:12:35',
                  'ip':u"192.168.3.101",'type':0,'level':4,'result':1,'description':u'admin删除了用户user3'}                


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


