# -*- coding: utf-8 -*-
from odoo import models, fields


class RestaurantCombo(models.Model):
    _name = 'restaurant.combo'
    _description = 'Restaurant ComboBurguer'
    _order = 'name'

    name = fields.Char(string='Title', required=True)
    burguer=fields.Many2one('restaurant.burguer',string='Burguer')
    other=fields.Many2one('restaurant.other',string='Other')
    price=fields.Float(string='Price',required=True)

    
