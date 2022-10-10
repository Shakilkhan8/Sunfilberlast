from odoo import api, fields, models

class SaleOrderListView(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('dispatch', 'Dispatch')])

    def action_dispatch(self):
        self.state = 'dispatch'