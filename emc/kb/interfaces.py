#-*- coding: UTF-8 -*-
from zope.interface import Interface
from zope import schema

from emc.kb import _


class ILogSettings(Interface):
    """A utility used to set log system 's  timeout and max limit.
    """
    
    timeout = schema.Int(
            title=_(u"timeout"),
            description=_(u"how many days that log at least will be reserved"),
            default=180,
            required=False,
        )
    max = schema.Int(
            title=_(u"max recorders"),
            description=_(u"How many recorders that log at least will be reserved"
                          " before the log dumped."),
            default=10000,
            required=False,
        )
    bsize = schema.Int(
            title=_(u"batch size"),
            description=_(u"How many log recorders will be deleted when every log dumped"),
            default=2000,
            required=False,
        )    
         

class InputError(Exception):
    """Exception raised if there is an error making a data input
    """

# db insterface
class IDbapi (Interface):
    """Db api """

    def get_rownumber():
        "fetch table's rownumber"

    def bulk_delete():
        "bulk delete"

    def fetch_oldest():
        "fetch the oldest recorder from db"
        
        
class IModelLocator (Interface):
    """medel table add row"""

    def addModel(self):
        "add a model data"

    def queryModel(self):
        "query model by search condition"

class IBranchLocator (Interface):
    """medel table add row"""

    def addBranch(self):
        "add a model data"

    def queryBranch(self):
        "query model by search condition"

class IFashejLocator (Interface):
    """fashej table add row"""

    def add(**kwargs):
        "add a row data"

    def query(code):
        "query  by search condition"

    def deleteByCode(code):
        "query  by search condition"

    def updateByCode(code):
        "query  by search condition"


class IAdminLogLocator(IFashejLocator):
    """admin_logs table's database api"""
    
class IUserLogLocator(IFashejLocator):
    """user_logs table's database api"""
    
class IFashetxLocator (IFashejLocator):
    """fashetx table add row"""

class IJieshoujLocator (IFashejLocator):
    """jieshouj table add row"""

class IJieshoutxLocator (IFashejLocator):
    """jieshouj table add row"""

class ILvboqLocator (IFashejLocator):
    """jieshouj table add row"""

class IJieshoujLocator (IFashejLocator):
    """jieshouj table add row"""

class IDianxingtxzyzkLocator (IFashejLocator):
    """jieshouj table add row"""

class ITianxianzkLocator (IFashejLocator):
    """jieshouj table add row"""

class IJieshoujzkLocator (IFashejLocator):
    """jieshouj table add row"""

class IFashejzkLocator (IFashejLocator):
    """jieshouj table add row"""

# add db interfaces for database which called emc_test

# 暂时继承IFashejLocator,
class IDanweiLocator(IFashejLocator):
    """temp Interface for test"""
