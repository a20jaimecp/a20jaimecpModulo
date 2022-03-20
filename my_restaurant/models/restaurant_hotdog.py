# -*- coding: utf-8 -*-
from odoo import models, fields

class RestaurantHotdogs(models.Model):
    _name = 'restaurant.hotdog'
    _description = 'Restaurant Hotdogs'
    _order = 'name'

    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
    sauces=fields.Selection([
        ('mayonnaise','Mayonnaise'),
        ('nothing','nothing'),
        ('ketchup','Ketchup'),
        ('mustard','Mustard'),
        ('ali-oli','Ali-Oli')
    ], default='nothing',required=False)
    price=fields.Float('Price',required=True)
