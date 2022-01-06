
from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit='product.product'

    product_popup = fields.Boolean("Show on popup")


class ProductProduct(models.Model):
    _inherit='product.template'

    product_popup = fields.Boolean("Show on popup")
