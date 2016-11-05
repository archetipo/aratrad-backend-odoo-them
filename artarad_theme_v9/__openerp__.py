# -*- coding: utf-8 -*-
# Copyright 2016 Openworx, LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "artarad_theme_v9",
    "summary": "artarad_theme_v9 community backend theme",
    "version": "1.0",
    "category": "Themes/Backend",
    "website": "http://www.artarad.com",
	"description": """
		artarad_theme_v9 community edition.
		The app dashboard is based on the module web_responsive from LasLabs Inc and the theme on Bootstrap United.
    """,
	'images':[
        'images/screen.png'
	],
    "author": "artarad",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
    ],
    "data": [
        'views/assets.xml',
        'views/web.xml',
    ],
}

