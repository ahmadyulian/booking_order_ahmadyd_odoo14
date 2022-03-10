from odoo import models, fields, api, exceptions, _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time

class CancelOrder(models.TransientModel):
    _name = "cancel.workorder"

    #oftxt
    notes = fields.Text('Notes')

    def cancelled(self):
        cancel = self.env['work.order'].browse(self.env.context['active_id'])
        cancel_create = cancel.update({'notes': self.notes, 'state': 'cancelled'})