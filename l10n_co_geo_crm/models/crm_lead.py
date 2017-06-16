# -*- coding: utf-8 -*-
# Copyright 2016 David Arnold, DevCO Colombia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, api


class CRMLead(models.Model):
    _name = 'crm.lead'
    _inherit = ['crm.lead', 'partner.city.abstract']

    @api.multi
    def _create_lead_partner_data(self, name, is_company, parent_id=False):
        # Depends on https://github.com/odoo/odoo/pull/16493
        vals = super(CRMLead, self)._create_lead_partner_data(name, is_company, parent_id=parent_id)
        vals['city_id'] = self.city_id.id
        return vals
