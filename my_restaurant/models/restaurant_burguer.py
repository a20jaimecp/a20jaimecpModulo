# -*- coding: utf-8 -*-
from odoo import models, fields


class RestaurantBurguer(models.Model):
    _name = 'restaurant.burguer'
    _description = 'Restaurant Burguer'
    _order = 'name'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    meet=fields.Selection([
        ('meet','Meet'),
        ('chicken','Chicken')
    ], default='meet')
    sauces=fields.Selection([
        ('mayonnaise','Mayonnaise'),
        ('nothing','nothing'),
        ('ketchup','Ketchup'),
        ('mustard','Mustard'),
        ('bbq','BBQ'),
        ('ali-oli','Ali-Oli')
    ], default='nothing',required=False)
    price=fields.Float(string='Price',required=True)

    
