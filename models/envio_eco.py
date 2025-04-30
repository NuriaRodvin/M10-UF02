from odoo import models, fields, api, exceptions

class EnvioEco(models.Model):
    _name = 'envio.eco'
    _description = 'Envío Ecológico'
    _rec_name = 'pedido_id'

    pedido_id = fields.Many2one(
        'sale.order', 
        string="Pedido", 
        required=True
    )
    direccion_entrega = fields.Char(string="Dirección de entrega", required=True)
    fecha_solicitud = fields.Datetime(string="Fecha solicitud", required=True, default=fields.Datetime.now)
    transporte_id = fields.Many2one(
        'transporte.eco', 
        string="Tipo de transporte"
    )
    fecha_entrega_prevista = fields.Datetime(string="Fecha entrega prevista", required=True)
    estado = fields.Selection(
        selection=[
            ('pendiente', 'Pendiente de envío'),
            ('reparto', 'En reparto'),
            ('entregado', 'Entregado'),
            ('no_entregado', 'No entregado'),
        ],
        string="Estado",
        default='pendiente'
    )
    fecha_entrega = fields.Datetime(string="Fecha entrega")

    @api.constrains('fecha_solicitud', 'fecha_entrega_prevista')
    def _check_fechas(self):
        for envio in self:
            if envio.fecha_solicitud > envio.fecha_entrega_prevista:
                raise exceptions.ValidationError(
                    "La fecha de solicitud no puede ser posterior a la fecha de entrega prevista."
                )