#-*- coding: UTF-8 -*-
import datetime
import unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from emc.kb.testing import INTEGRATION_TESTING
#sqlarchemy
from sqlalchemy import text
from sqlalchemy import func

class TestEmc_test(unittest.TestCase):
    """docstring for TestEmc_test."""

    layer = INTEGRATION_TESTING

    def test_t_db_mapping_danwei(self):
        from emc.kb.mapping_t_db import Danwei
        from emc.kb import t_session as Session

        dw = Danwei()
        dw.danweimc = u"单位名称1"
        dw.danweidz = u"单位地址1"
        dw.danweilxfs = u"单位电话:85414302"
        Session.add(dw)
        nums = Session.query(func.count(dw.danweiId)).scalar()
        import pdb
        pdb.set_trace()
        self.assertTrue(dw.danweiId is not None)
        print dw.danweimc

    def test_t_db_danwei_locator(self):
        from emc.kb.mapping_t_db import Danwei
        from emc.kb.interfaces import IDaneiLocator
        from zope.component import getUtility
        from emc.kb import t_session as Session

        locator = getUtility(IDanweiLocator)
        danweimc = u"单位名称1"
        danweidz = u"单位地址1"
        danweilxfs = u"单位电话:85414302"

        danwei = locator.getByCode(danweimc)
        import pdb
        pdb.set_trace()
        if danwei == None:
            locator.add(danweimc)
