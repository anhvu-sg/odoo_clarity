# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class InheritedResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    odoo_clarity_tracking_code = fields.Char(config_parameter='odoo_clarity.odoo_clarity_tracking_code',
        string='Tracking Code', copy=True, default='', store=True
    )
