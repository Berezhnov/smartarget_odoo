# Copyright 2021 Smartarget <https://smartarget.onkune>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    has_smartarget_facebook_messenger_contact_us = fields.Boolean("Smartarget Facebook Messenger - Contact Us")

    smartarget_user_id = fields.Char(
        "Smartarget User ID", help="Smartarget User ID (not the entire js code). You can get user ID on smartarget.online"
    )

    facebook_messenger = fields.Char(
        "Facebook Messenger",
    )
