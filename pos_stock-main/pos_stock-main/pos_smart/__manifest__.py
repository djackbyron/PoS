# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Point of Sale customization',
    'version': '1.0.2',
    'category': 'Point Of Sale',
    'sequence': 20,
    'summary': 'Add Qty on hand, pop up error for out of stock',
    'description': "",
    'depends': ['base','point_of_sale'],
    'data': [
        'security/pos_security.xml',
        'views/pos_demo.xml',
        'views/product.xml',
        'report/report.xml'
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'qweb': ['static/src/xml/pos_demo.xml'],
    'website': '',
}
