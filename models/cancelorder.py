from odoo import api, fields, models, exceptions, _

class CancelOrder(models.TransientModel):
    _name = "cancel.workorder"

    #oftxt
    note = fields.Text('note')

    def cancelled(self):
        cancel = self.env['work.order'].browse(self.env.context['active_id'])
        cancel_create = cancel.update({'note': self.note, 'state': 'cancelled'})