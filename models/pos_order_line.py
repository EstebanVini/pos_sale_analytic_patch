from odoo import models, fields, api

class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    analytic_account_id = fields.Many2one(
        'account.analytic.account',
        string='Cuenta analítica',
        readonly=True
    )

    @api.model
    def create(self, vals):
        if 'order_id' in vals and not vals.get('analytic_account_id'):
            order = self.env['pos.order'].browse(vals['order_id'])
            if order.session_id.config_id.account_analytic_id:
                vals['analytic_account_id'] = order.session_id.config_id.account_analytic_id.id
        return super().create(vals)
