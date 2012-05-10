# -*- encoding: utf-8 -*-

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import decimal_precision as dp
import time
import netsvc
import pooler, tools
import math
from tools.translate import _

from osv import fields, osv

class FiscalDocHeader(osv.osv):
   _inherit = "fiscaldoc.header"
   _columns = {'agente2':fields.many2one('sale.agent', 'Agente di vendita', required=False, help='Campo di sola visualizzazione di quanto impostato sul cliente.')
                            
               
               }
   def onchange_partner_id(self, cr, uid, ids, part, context):
        res = super(FiscalDocHeader, self).onchange_partner_id(cr, uid, ids, part, context)
        val = res.get('value', False)
        warning = res.get('warning', False)
        #import pdb;pdb.set_trace()
        if val and part.agent_id:
            val['agente2']=part.agent_id.id
            
        
            
            
        return {'value': val, 'warning': warning}
FiscalDocHeader()