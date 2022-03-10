from odoo import models, fields, api, exceptions, _
from odoo.osv import osv
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time
import logging

_logger = logging.getLogger(__name__)

class ServiceTeam(models.Model):
    _name = 'service.team'
    _description = 'Deskripsi Service Team'

    #ofchar
    name = fields.Char(string='Nama Tim', readonly=False, default=False, required=True)

    #ofm2o
    team_leader = fields.Many2one(comodel_name='res.users', 
    string='Ketua Tim', 
    readonly=False, 
    required=True)
    
    #ofm2m
    team_member = fields.Many2many(comodel_name='res.users', 
    string='Anggota Tim', 
    readonly=False, 
    required=False)