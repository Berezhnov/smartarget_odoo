# Copyright 2021 Smartarget <https://smartarget.onkune>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    has_smartarget_whatsapp_contact_us = fields.Boolean("Smartarget Whatsapp - Contact Us")

    smartarget_user_id = fields.Char(
        "Smartarget User ID", help="Smartarget User ID (not the entire js code). You can get user ID <a href='https://app.smartarget.online/#/integration'>here</a>"
    )

    phone_number = fields.Char(
        "Whatsapp Phone Number",
    )
