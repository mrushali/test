# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'POS Print Receipt',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Print Receipt extensions for the Point of Sale ',
    'description': "POS Print Receipt : For that you have to enable_order_note from the pos_config and then visible in pos module",

    'depends': ['point_of_sale'],
    'author': "Sismatix",
    'website': "http://www.yourcompany.com",
    'data': [
        'views/assets.xml',
    ],
    'qweb': [
        'static/src/xml/print_receipt.xml',
    ],
}
