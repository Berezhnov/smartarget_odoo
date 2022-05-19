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
    'name': 'Smartarget Lucky Wheel',
    'summary': 'Allow customers to spin the lucky wheel and convert them to leads',
    'version': '1.0',
    "license": "AGPL-3",
    'description': "Lucky Wheel is the ultimate way to make customers happier and much more engaged. Lucky Wheel for Odoo can give the users the opportunity to get a discount code from you which obviously increases the chance to buy in 15%. But that’s not the end, because using the Lucky Wheel app for Odoo also collects emails of your customers, which is simply allows you to send them a newsletter in the future and making sure they will come back to your Odoo website again.",
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
