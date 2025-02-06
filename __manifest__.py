# -*- coding: utf-8 -*-
{
    'name': "my_custom",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "zvasoup",
    'website': "https://www.github.com/zoovasoup",

    'category': 'Theme',
    'version': '0.0.1',

    'depends': ['base'],

    'data': [
        'views/report_template.xml',
        'data/report_layout.xml',
    ],

    'installable': True,
    'application' : False,
    'license': 'AGPL-3',
}

