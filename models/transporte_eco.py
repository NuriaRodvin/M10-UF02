from odoo import models, fields, api

class TransporteEco(models.Model):
    _name = 'transporte.eco'
    _description = 'Transporte Ecológico'
    _rec_name = 'transporte'

    transporte = fields.Selection([
        ('bicicleta', 'Bicicleta'),
        ('patinete', 'Patinete Eléctrico'),
        ('monopatin', 'Monopatín'),
        ('apie', 'A pie'),
    ], string="Transporte", required=True)
    
    descripcion = fields.Text(string="Descripción", required=True)
    
    envio_ids = fields.One2many(
        'envio.eco', 
        'transporte_id', 
        string="Envíos"
    )

    _sql_constraints = [
        ('transporte_unique', 'UNIQUE(transporte)', 'El transporte debe ser único.')
    ]
