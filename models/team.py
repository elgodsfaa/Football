# -*- coding: utf-8 -*-

from odoo import models, fields


class Team(models.Model):
    _name = 'football.team'
    _description = 'Football Team'

    name = fields.Char(string='Team Name', required=True)
    city = fields.Char(string='City')

    # Relationships
    coach_id = fields.Many2one('res.users', string='Coach')
    player_ids = fields.One2many('football.player', 'team_id', string='Players')

    # Relationships for matches (home and away)
    home_match_ids = fields.One2many('football.match', 'home_team_id', string='Home Matches')
    away_match_ids = fields.One2many('football.match', 'away_team_id', string='Away Matches')
