from odoo import models, fields, api, exceptions, _


class CancelWorkOrder(models.TransientModel):
    _name = "cancel.workorder"

    note = fields.Text('Note')

    def cancelled(self):
        cancel = self.env['work.order'].browse(self.env.context['active_id'])
        cancel_create = cancel.update({'note': self.note, 'state': 'cancelled'})