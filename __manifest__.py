# -*- coding: utf-8 -*-
{
    'name': "lsi_report_custom",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "zoovasoup",
    'website': "https://www.github.com/zoovasoup",

    'category': 'Theme',
    'version': '0.1.0',

    'depends': ['base'],

    'data': [
        'views/report_template.xml',
        'data/report_layout.xml',
        'views/sale_template.xml',
    ],

    'installable': True,
    'application' : False,
    'license': 'GPL-3',
}

