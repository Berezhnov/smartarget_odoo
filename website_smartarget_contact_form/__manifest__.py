# -*- coding: utf-8 -*-
#################################################################################
# Author      : Smartarget (<smartarget.online>)
# Copyright(c): 2022-Present Smartarget Inc.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

{
    'name': 'Smartarget Contact Form',
    'summary': 'Allow users to contact you by filling a form',
    'version': '1.0',
    "license": "AGPL-3",
    'description': "The modern shopper has a lot of options to choose from which increases the likelihood of them bouncing off if they don’t find what they need. Since the needs of customers are . One of the ways business owners can improve their Odoo website is by utilising the Contact Form app to encourage website visitors to let merchants know what they need. The contact form can also be used to direct customers to a different section of your website where customers may find exactly what they need.",
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
