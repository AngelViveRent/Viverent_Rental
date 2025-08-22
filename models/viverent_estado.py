# -*- coding: utf-8 -*-

from odoo import models, fields

class ViverentEstado(models.Model):
    _name = 'viverent.estado'
    _description = 'Estado del proceso de renta'
    _order = 'sequence'

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)