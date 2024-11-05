# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sail_of_kalgur(models.Model):
     _name = 'sail_of_kalgur.sail_of_kalgur'
     _description = 'sail_of_kalgur.sail_of_kalgur'

     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class player(models.Model):
	_name = 'sail_of_kalgur.player'
	_description = 'Jugador'
	
	name = fields.Char()
	
	gold = fields.Float(default = 1000)
	silver = fields.Float(default = 1000)
	coal = fields.Float(default = 1000)
	boat = fields.Int(default = 1)
	workers = fields.Int(default = 1)
