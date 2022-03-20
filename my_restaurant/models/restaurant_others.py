# -*- coding: utf-8 -*-
from odoo import models, fields


class RestaurantOthers(models.Model):
    _name = 'restaurant.other'
    _description = 'Restaurant Other'
    _order = 'name'

    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
    price=fields.Float('Price',required=True)
