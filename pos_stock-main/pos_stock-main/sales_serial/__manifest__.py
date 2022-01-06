# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sales company serial',
    'version': '1.0.1',
    'category': 'Sale ',
    'sequence': 20,
    'summary': 'Places Company prefix with sale order',
    'description': "",
    'depends': ['base','sale'],
    'data': [
        'data/sales_sequence.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'qweb': [],
    'website': '',
}
