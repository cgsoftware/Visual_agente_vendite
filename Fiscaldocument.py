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
        if not part:
            return {'value': {'partner_indfat_id': False, 'partner_indcons_id': False}}
        addr = self.pool.get('res.partner').address_get(cr, uid, [part], ['delivery', 'invoice', 'contact'])
        part = self.pool.get('res.partner').browse(cr, uid, part)
        pricelist = part.property_product_pricelist and part.property_product_pricelist.id or False
        pagamento_id = part.property_payment_term and part.property_payment_term.id or False
#       fiscal_position = part.property_account_position and part.property_account_position.id or False
        agente = part.user_id and part.user_id.id or uid
        if part.bank_ids:
            banca_cliente = part.bank_ids[0].bank.id
        else:
            banca_cliente = False

        val = {
            'partner_indfat_id': addr['invoice'],
            'partner_indcons_id': addr['delivery'],
            'pagamento_id':pagamento_id,
            'sconto_pagamento':part.property_payment_term.sconto,
            'agente':agente,
            'str_sconto_partner':part.str_sconto_partner,
            'sconto_partner':part.sconto_partner,
            'spedizione':part.spedizione.id,
            'vettore':part.property_delivery_carrier.id,
            'porto_id':part.carriage_condition_id.id,
            'aspetto_esteriore_id':part.goods_description_id.id,
            'banca_patner':banca_cliente,
            'agente2':part.agent_id.id
            
        }
        if pricelist:
            val['listino_id'] = pricelist

        warning = {}
            
        
            
            
        return {'value': val, 'warning': warning}
FiscalDocHeader()