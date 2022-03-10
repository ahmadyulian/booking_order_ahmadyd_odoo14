# -*- coding: utf-8 -*-
{
    'name': "booking_order_ahmadyd_odoo14",

    'summary': """
        Test Booking Order Odoo14""",

    'description': """
        Test Booking Order Odoo14
    """,

    'author': "Ahmad Yulian Dinata",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',
    'application':True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/service_team_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
