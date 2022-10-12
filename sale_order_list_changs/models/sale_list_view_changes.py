from odoo import api, fields, models

class SaleOrderListView(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('dispatch', 'Dispatch')])
    order_create_date = fields.Datetime('Create Date')
    expect_date = fields.Date('Expected Date')

    def action_dispatch(self):
        self.state = 'dispatch'


