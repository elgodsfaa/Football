# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Player(models.Model):
     _name = 'football.player'
     _description = 'football.player'

     name = fields.Char(string="Name", required=True)
     last_name = fields.Char(string="Last Name")
     shirt_number = fields.Integer(string="Shirt Number")
     position = fields.Char(string="Position")
     
     # Many2one (N:1) relationship with Team
     team_id = fields.Many2one('football.team', string="Team")
     
     # Many2many (N:M) relationship with Match
     match_ids = fields.Many2many('football.match', string="Matches")

#
     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
