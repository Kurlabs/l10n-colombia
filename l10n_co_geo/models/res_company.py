# -*- coding: utf-8 -*-
# Copyright 2016 David Arnold, DevCO Colombia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api, _  # noqa


class ResCompany(models.Model):
    _name = 'res.company'
    _inherit = ['res.company', 'partner.city.abstract']

    city_id = fields.Many2one(
        'res.country.state.city', 'City',
        compute="_compute_address", inverse='_inverse_city_id', store=False)

    def _get_company_address_fields(self, partner):
        res = super(ResCompany, self)._get_company_address_fields(partner)
        res.update(city_id=partner.city_id)
        return res

    def _inverse_city_id(self):
        for company in self:
            company.partner_id.city_id = company.city_id
