from odoo import models, fields

class ViverentRenta(models.Model):
    _name = 'viverent.renta'
    _description = 'Renta Viverent'

    name = fields.Char(required=True)
    estado_id = fields.Many2one('viverent.estado', string='Estado')