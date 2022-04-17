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
    'name': 'Smartarget Information Message',
    'summary': 'Show important updates and information on your site',
    'version': '1.0',
    "license": "AGPL-3",
    'description': "Information Message - The right way to communicate information with users. Smartarget developed a plugin for Cloudflare so you can communicate information to users in a visible way, yet not intrusive. The Information Message will be shown to users on all pages, both on desktop and mobile, and will allow you to communicate with them relevant information that you believe is important for them to know.",
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
