from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext import declarative
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
os.environ['NLS_LANG'] = '.AL32UTF8'

# Set up the i18n message factory for our package
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('emc.kb')

InputDb = "emc.kb:Input db"
DoVote = "emc.kb:Do vote"

ORMBase = declarative.declarative_base()
ora_engine = create_engine('oracle://sys:password@kwsensen.f3322.net:1521/orcl2?charset=utf8',optimize_limits=True,use_binds_for_limits=False,convert_unicode=True, encoding='utf-8',pool_recycle=3600)
# some_engine = create_engine('mysql://kbdba:K0mdba$!9@127.0.0.1:3306/parameters?charset=utf8', pool_recycle=3600)
# emc_engine = create_engine('mysql://kbdba:K0mdba$!9@127.0.0.1:3306/emc_test?charset=utf8', pool_recycle=3600)
# log_engine = create_engine('mysql://kbdba:K0mdba$!9@127.0.0.1:3306/emclog?charset=utf8', pool_recycle=3600)
# Session = sessionmaker(bind=some_engine)
# Session_emc = sessionmaker(bind=emc_engine)
Session_log = sessionmaker(bind=ora_engine)
# kb_session = Session()
# t_session = Session_emc()
log_session = Session_log()
# pas sqlarchemy session:
#some_engine = create_engine('oracle+cx_oracle://HR:tome5857@192.168.2.10:1521/test', pool_recycle=3600)
#Session = sessionmaker(bind=some_engine)
pas_session = log_session
kb_session = log_session
t_session = log_session
