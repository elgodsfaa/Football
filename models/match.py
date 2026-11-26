# -*- coding: utf-8 -*-

from odoo import models, fields


class Match(models.Model):
    _name = 'football.match'
    _description = 'Football Match'

    matchday = fields.Char(string='Matchday')
    date = fields.Datetime(string='Date')

    # Relationships with Team (home and away)
    home_team_id = fields.Many2one('football.team', string='Home Team')
    away_team_id = fields.Many2one('football.team', string='Away Team')

    home_goals = fields.Integer(string='Home Goals')
    away_goals = fields.Integer(string='Away Goals')

    # Many2many relationship with Player
    player_ids = fields.Many2many('football.player', string='Players')
