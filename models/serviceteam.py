from odoo import api, fields, models

class ServiceTeam(models.Model):
    _name = 'service.team'
    _description = 'Deskripsi Service Team'

    #ofchar
    name = fields.Char(
        string='Nama Tim',
        required=True)

    #ofm2o
    team_leader = fields.Many2one(comodel_name='res.users',
        string='Ketua Tim',
        required=True)

    #ofm2m
    team_member = fields.Many2many(
        comodel_name='res.users',
        string='Anggota Member')