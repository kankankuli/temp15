# -*- coding: utf-8 -*-
{
    'name': "POS Swipe Item to Delete from cart",
    "live_test_url": "https://demo14.odooskillz.com/web?db=pos_slide_to_delete",
    'author': "Odoo Skillz",
    'summary': 'Adds support for deleting order lines in the POS client with a finger touch swipe.',
    'version': '14.0.1.0.0',
    'category': 'Sales/Point of Sale',
    'description':
        """
        Adds support for deleting order lines in the POS client with a finger touch swipe.
        """,
    'support': 'contact@odooskillz.com',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_slide_to_delete/static/src/js/**/*.js',
            'pos_slide_to_delete/static/src/css/OrderLine.scss',
        ],
    },
    'license': 'LGPL-3',

    "images": ["static/description/thumbnail.jpg"],

}
