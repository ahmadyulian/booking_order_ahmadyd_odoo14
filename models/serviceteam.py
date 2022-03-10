import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, exceptions, _
from odoo.osv import osv
import logging

_logger = logging.getLogger(__name__)


class ServiceTeam(models.Model):
    _name = 'service.team'
    _description = 'Service Team'

    name = fields.Char(string='Team Name', readonly=False, default=False, required=True)
    team_leader = fields.Many2one(comodel_name='res.users', readonly=False, string='Team Leader', required=True)
    team_members = fields.Many2many(comodel_name='res.users', readonly=False, string='Team Members', required=False)