# -*- coding: utf-8 -*-

from odoo import models, fields

class Match(models.Model):
    _name = 'football.match'
    _description = 'Football Match'

    # Campos básicos basados en el diagrama
    match_id = fields.Integer(string='Match ID')
    matchday = fields.Char(string='Matchday') # "Jornada" en tu diagrama
    date = fields.Datetime(string='Date') # "Fecha" en tu diagrama
   
    # Relaciones Many2one con Equipos (Local y Visitante)
    home_team_id = fields.Many2one('football.team', string='Home Team')
    away_team_id = fields.Many2one('football.team', string='Away Team')

    # Relación Many2many con Jugador (jugadores y suplentes que jugaron el partido)
    player_ids = fields.Many2many('football.player', string='Players') 
#
     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100