

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        # seq = self.env['ir.sequence'].next_by_code('project.issue')
        if res.company_id.name == 'My Company (San Francisco)':
            seq = self.env['ir.sequence'].search([('prefix','=','SCF')])._next()
            res.name = seq
        elif res.company_id.name == 'My Company (Chicago)':
            seq = self.env['ir.sequence'].search([('prefix','=','CHI')])._next()
            res.name = seq
        return res