# Copyright 2021 Smartarget <https://smartarget.onkune>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    has_smartarget_information_message = fields.Boolean("Smartarget Information Message")

    smartarget_user_id = fields.Char(
        "Smartarget User ID", help="Smartarget User ID (not the entire js code). You can get user ID on smartarget.online"
    )

    information_message_title = fields.Char("Title")
    information_message_text = fields.Char("Text")
    information_message_button_text = fields.Char("Button Text")
    information_message_button_link = fields.Char("Button Link")

