# -*- coding: utf-8 -*-
{
    "name": "Odoo Clarity",
    "summary": "Odoo Clarity: is a free, easy-to-use tool that captures how real people actually use your site. Setup is easy and you'll start getting data in minutes.",
    "version": "15.0.0.2",
    "category": "Extra tools",
    "license": "LGPL-3",
    "author": "Vu Nguyen",
    "website": "",
    "price": 0,
    "sequence": 10,
    "contributors": [
    ],
    "depends": [
        'web',
    ],
    "data": [
        'views/clarity_views.xml',
        'views/inherited_res_config_settings_view.xml',
    ],
    "qweb": [
    ],
    "images": [
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "assets": {
        "web.assets_backend": [
        ],
        "web.assets_qweb": [
        ],
    },
    "application": False,
    "installable": True,
    "auto_install": False,
    "images": ['static/description/banner.png'],
}
