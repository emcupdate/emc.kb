#-*- coding: UTF-8 -*-
import csv
from cStringIO import StringIO
from zope import event
from zope.component import getMultiAdapter
from five import grok
from zope.interface import implements
from zope.interface import Interface
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage
from emc.kb import _

# field names will be imported
data_PROPERTIES = [
    'admnid',
    'userid',
    'datetime',
    'ip',
    'type',
    'level',
    'description',        
    'result'
    ] 
# need byte string
data_VALUES = [
               u"主体".encode('utf-8'),
               u"客体".encode('utf-8'),
               u"时间".encode('utf-8'),
               u"ip".encode('utf-8'),
               u"级别".encode('utf-8'),
               u"描述".encode('utf-8'),
               u"结果".encode('utf-8')
               ]


class DataOut (grok.View):
    """Data import and export as CSV files.
    """
    grok.context(Interface)
    grok.name('export_csv')
    grok.require('zope2.View')
    
    def searchview(self,viewname="admin_logs"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def render(self):
        method = self.request.get('REQUEST_METHOD', 'GET')
#         import pdb
#         pdb.set_trace()
        if (method != 'POST'):
            return self.request.response.redirect(self.context.absolute_url())

        if self.request.form.get('form.button.Cancel'):
            return self.request.response.redirect(self.context.absolute_url())
        searchview = self.searchview()
 # datadic receive front ajax post data
        datadic = self.request.form
        start = int(datadic['start']) # batch search start position
        size = int(datadic['size'])      # batch search size
        sortcolumn = datadic['sortcolumn']
        sortdirection = datadic['sortdirection']
        keyword = (datadic['searchabletext']).strip()
#         origquery = searchview.getPathQuery()
        origquery = {}
        # default reverse,as is desc
        origquery['sort_on'] = sortcolumn
        # sql db sortt_order:asc,desc
        origquery['sort_order'] = sortdirection
 #模糊搜索
        if keyword != "":
            origquery['SearchableText'] = '%'+keyword+'%'
        else:
            origquery['SearchableText'] = ""
#origquery provide  batch search
        origquery['size'] = size
        origquery['start'] = start
#totalquery  search all
        totalquery = origquery.copy()
        totalquery['size'] = 0
        # search all   size = 0 return numbers of recorders
        totalnum = searchview.search_multicondition(totalquery)
        origquery.update({"size":totalnum})
        resultDicLists = searchview.search_multicondition(origquery)
        del origquery
        del totalquery
#call output function
# resultDicLists like this:[(u'C7', u'\u4ed6\u7684\u624b\u673a')]

        return self.exportData(resultDicLists)
        


    def exportData(self,recorders):
        """Export Data within CSV file."""

        datafile = self._createCSV(self._getDataInfos(recorders))
        return self._createRequest(datafile.getvalue(), "sheet_log_export.csv")
       
    
    def _getDataInfos(self,recorders):
        """Generator filled with the recorders."""
        
        from emc.kb.utils import kind
        from emc.kb.utils import level as log_level
        from emc.kb.utils import result as log_result       
        for i in recorders:
            i = list(i)                             
            i[4] = kind[i[4]]
            i[5] = log_level[i[5]]
            i[7] = log_result[i[7]]                   
            yield i


    def _createCSV(self, lines):
        """Write header and lines within the CSV file."""
        datafile = StringIO()
        writor = csv.writer(datafile)
        writor.writerow(data_VALUES)
        map(writor.writerow, lines)
        return datafile

    def _createRequest(self, data, filename):
        """Create the request to be returned.

        Add the right header and the CSV file.
        """
        self.request.response.addHeader('Content-Disposition', "attachment; filename=%s" % filename)
        self.request.response.addHeader('Content-Type', "text/csv;charset=utf-8")
        self.request.response.addHeader("Content-Transfer-Encoding", "8bit")        
        self.request.response.addHeader('Content-Length', "%d" % len(data))
        self.request.response.addHeader('Pragma', "no-cache")
        self.request.response.addHeader('Cache-Control', "must-revalidate, post-check=0, pre-check=0, public")
        self.request.response.addHeader('Expires', "0")
        return data   
    