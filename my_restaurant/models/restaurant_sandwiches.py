# -*- coding: utf-8 -*-
from odoo import models, fields


class RestaurantSandwiches(models.Model):
    _name = 'restaurant.sandwich'
    _description = 'Restaurant Sandwich'
    _order = 'name'

    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
    meet=fields.Selection([
        ('meet','Meet'),
        ('chicken','Chicken'),
        ('lomo','Loin'),
        ('bacon','Bacon')
    ], default='chicken')
    sauces=fields.Selection([
        ('mayonnaise','Mayonnaise'),
        ('nothing','nothing'),
        ('ketchup','Ketchup'),
        ('mustard','Mustard'),
        ('ali-oli','Ali-Oli')
    ], default='nothing',required=False)
    price=fields.Float('Price',required=True)
