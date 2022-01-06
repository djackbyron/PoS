# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'POS POPUP',
    'version': '1.0.1',
    'category': 'POS ',
    'sequence': 20,
    'summary': 'Places POP UP on Product',
    'description': "",
    'depends': ['base','point_of_sale'],
    'data': [
        'views/company.xml',
        'views/coupons.xml',
        'views/coupon_config.xml',
        'views/product.xml'
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'qweb': [
        'static/src/xml/CouponButton.xml',
        'static/src/xml/CouponProductsPopup.xml',
        # 'static/src/xml/CouponPopupScreen.xml'
    ],
    'website': '',
}
