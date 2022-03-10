from odoo import models, fields, api, exceptions, _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo.osv import osv
import time
import logging
_logger = logging.getLogger(__name__)

class ServiceTeam(models.Model):
    _name = 'service.team'
    _description = 'Deskripsi Service Team'

    #ofchar
    name = fields.Char(string='Nama Tim', required=True)
    
    #ofm2o
    team_leader = fields.Many2one(comodel_name='res.user', string='Ketua Tim', required=True)
    
    #ofm2m
    team_member = fields.Many2many(comodel_name='res.user', string='Anggota Tim')