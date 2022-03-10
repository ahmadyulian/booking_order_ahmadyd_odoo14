import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, exceptions, _


class Cancelled(models.TransientModel):
    _name = "cancelled.wo"

    notes = fields.Text('notes')

    def cancelled(self):
        cancel = self.env['work.order'].browse(self.env.context['active_id'])
        cancel_create = cancel.update({'notes': self.notes, 'state': 'cancelled'})
