from odoo import api, fields, models

class SaleOrderListView(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('dispatch', 'Dispatch')])
    order_create_date = fields.Datetime('Create Date')
    expect_date = fields.Date('Expected Date')

    def action_dispatch(self):
        self.state = 'dispatch'

    @api.model
    def create(self, vals_list):
        vals_list['create_date'] = vals_list['order_create_date']
        res = super(SaleOrderListView, self).create(vals_list)
        return res

    @api.model
    def write(self, vals):
        vals['create_date'] = vals['order_create_date']
        res = super(SaleOrderListView, self).write(vals)
        return res

