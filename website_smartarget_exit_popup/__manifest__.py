# -*- coding: utf-8 -*-
#################################################################################
# Author      : Smartarget (<smartarget.online>)
# Copyright(c): 2021-Present Smartarget Inc.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

{
    'name': 'Smartarget Exit Popup',
    'summary': 'Show users special offer before they leave your website',
    'version': '1.0',
    "license": "AGPL-3",
    'description': "Exit Popup allowning you to show a message to users who move their mouse courser in attention to close your website tab. With Exit Popup you can design your popup message and call-to-action to attrack the user and prevent his leaving.",
    'author': 'smartarget.online',
    'support': 'support@smartarget.online',
    'category': 'Website',
    'website': "https://smartarget.online",
    'depends': ['website'],
    'data': [
         "views/website_config_settings.xml",
		"views/website.xml",
		"views/templates.xml",
    ],
    'images' : ['images/cover.png'],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
