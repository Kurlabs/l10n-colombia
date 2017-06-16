# -*- coding: utf-8 -*-
# Copyright 2016 David Arnold, DevCO Colombia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from openerp import models, fields, api


class PartnerCityAbstract(models.AbstractModel):
    _name = 'partner.city.abstract'

    city_id = fields.Many2one('res.country.state.city', 'City')

    @api.onchange('city_id')
    def _onchange_city(self):
        self.city = self.city_id.name
        if self.city_id:
            self.state_id = self.city_id.state_id
            self.country_id = self.city_id.country_id

    @api.onchange('state_id')
    def _onchange_state_city(self):
        if self.city_id.state_id != self.state_id:
            self.city_id = False

    @api.onchange('country_id')
    def _onchange_country(self):
        if self.city_id.country_id != self.country_id:
            self.city_id = False
        if self.state_id.country_id != self.country_id:
            self.state_id = False
