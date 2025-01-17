# -*- coding: utf-8 -*-
{
    'name': "open_academy",

    'summary': """
        This is the OpenAcademy for beginners""",

    'description': """
        This is the OpenAcademy for beginners under
        https://www.odoo.com/documentation/16.0/developer/tutorials/backend.html#build-an-odoo-module
    """,

    'author': "Ariel Barreiros",
    'website': "https://binhex.cloud",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/course.xml',
        'views/session.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/courses.xml',
    ],
}
