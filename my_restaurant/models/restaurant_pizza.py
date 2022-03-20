# -*- coding: utf-8 -*-
from odoo import models, fields


class RestaurantPizzas(models.Model):
    _name = 'restaurant.pizzas'
    _description = 'Restaurant Pizza'
    _order = 'name'

    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
    masa=fields.Selection([
        ('fina','Slime'),
        ('gruesa','Thick')
        
    ], default='gruesa')
    
    price=fields.Float('Price',required=True)
