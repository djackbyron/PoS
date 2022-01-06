
from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit='product.product'

    # show_qty_on_hand = fields.Boolean("Show qty on hand",default=False,compute="compute_rights")
    show_qty_on_hand = fields.Boolean("Show qty on hand")
    show_neg = fields.Boolean("Show 0 or negative amount")
    can_still_sold_neg = fields.Boolean("Can still be sold when 0 or negative")

    def compute_rights(self):
        self.show_qty_on_hand = self.env.user.has_group('pos_smart.group_cf')


class ProductProduct(models.Model):
    _inherit='product.template'

    # show_qty_on_hand = fields.Boolean("Show qty on hand",default=False,compute="compute_rights")
    show_qty_on_hand = fields.Boolean("Show qty on hand")
    show_neg = fields.Boolean("Show 0 or negative amount")
    can_still_sold_neg = fields.Boolean("Can still be sold when 0 or negative")

    def compute_rights(self):
        self.show_qty_on_hand = self.env.user.has_group('pos_smart.group_cf')
