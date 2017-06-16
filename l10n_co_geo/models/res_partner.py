# -*- coding: utf-8 -*-
# Copyright 2016 David Arnold, DevCO Colombia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, api


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = ['res.partner', 'partner.city.abstract']

    @api.model
    def _address_fields(self):
        return super(ResPartner, self)._address_fields() + ['city_id']
