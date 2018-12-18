# -*- coding: utf-8 -*-
# Copyright(c): 2019 Freshoo (<www.freshoo.cn>)

{
    'name': 'Backend Theme',
    'version': '12.0.1.0.0',
    'summary': """Community backend theme""",
    'description': """
""",
    'author': 'dong@freshoo.cn',
    'website': 'https://www.freshoo.cn',
    'images': ['static/description/banner.png'],
    'category': 'Hidden',
    'depends': ['web'],
    'data': [
        'views/webclient_templates.xml',
    ],
    'qweb': [
        "static/src/xml/*.xml",
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}