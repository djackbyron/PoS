
from odoo import api, fields, models, _


class Company(models.Model):
    _inherit='res.company'

    product_popup = fields.Boolean("Show Product Popup")

