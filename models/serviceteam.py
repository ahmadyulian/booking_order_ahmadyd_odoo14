from odoo import api, fields, models

class ServiceTeam(models.Model):
    _name = 'service.team'
    _description = 'Deskripsi Service Team'

    name = fields.Char(string='Name', required=True)
    team_leader = fields.Many2one(comodel_name='res.user', string='Team Leader', required=True)
    team_member = fields.Many2many(comodel_name='res.user', string='Team Member', required=False)