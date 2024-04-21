# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
	'name': "Product Image On Picking",
	'version': "13.0.0.0",
	'category': "Warehouse",
	'summary': "Display product image on picking print product image on delivery order report print image on receipt product image print product image on picking product image in delivery order line print Product image on picking order",
	'description': """
						Display product image on picking(receipt/delivery) and print product image on delivery slip report. 
					""",
	'author': "BrowseInfo",
	"website" : "https://www.browseinfo.com",
    'depends': ['base', 'sale_management', 'purchase','stock'],
	'data': [
			'report/delivery_slip_report.xml',
			'views/view_stock_picking.xml',
			],
	'demo': [],
	'installable': True,
	'auto_install': False,
	'application': False,
	"live_test_url":'https://youtu.be/CPqoiMhhh1g',
	"images":['static/description/Banner.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
