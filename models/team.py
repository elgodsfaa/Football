# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Team(models.Model):
    _name = 'football.team'
    _description = 'Football Team'

    team_id = fields.Integer(string='Team ID')
    name = fields.Char(string='Team Name', required=True)
    city = fields.Char(string='City')
    
    # Relationships based on the diagram
    coach_id = fields.Many2one('football.user', string='Coach')
    player_ids = fields.One2many('football.player', 'team_id', string='Players')

    # Relationships for matches (home and away)
    home_match_ids = fields.One2many('football.match', 'home_team_id', string='Home Matches')
    away_match_ids = fields.One2many('football.match', 'away_team_id', string='Away Matches')

     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
