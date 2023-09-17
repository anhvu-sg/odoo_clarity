# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import api, models, _

logger = logging.getLogger(__name__)


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        session_info = super().session_info()
        return self._add_odoo_clarity_tracking_code_session_info(session_info)

    @api.model
    def _add_odoo_clarity_tracking_code_session_info(self, session_info):
        odoo_clarity_tracking_code = self.env['ir.config_parameter'].sudo().get_param('odoo_clarity.odoo_clarity_tracking_code', 'iqzpfnsz2v')
        if odoo_clarity_tracking_code:
            session_info['odoo_clarity_tracking_code'] = odoo_clarity_tracking_code
        return session_info
