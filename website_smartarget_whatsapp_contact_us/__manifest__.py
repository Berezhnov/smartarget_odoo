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
    'name': 'Smartarget Whatsapp - Contact Us',
    'summary': 'Allow customers to contact you using Whatsapp',
    'version': '1.0',
    "license": "AGPL-3",
    'description': "Let's make it easier for your customers to contact you! Probably most of your users are using Whatsapp, so its time to give them the option to contact you by using Whatsapp. With 'Whatsapp - Contact Us' you can add a small icon on the bottom-right corner with you phone number and short message as 'Contact us' or 'message us' etc. When user click on the icon - new tab will be pop with Whatsapp for web and chat window with you.",
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
