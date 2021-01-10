# Copyright 2021 Smartarget <https://smartarget.onkune>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    has_smartarget_exit_popup = fields.Boolean("Smartarget Exit Popup")

    smartarget_user_id = fields.Char(
        "Smartarget User ID", help="Smartarget User ID (not the entire js code). You can get user ID on smartarget.online"
    )

    exit_popup_header = fields.Char("Exit Popup Header")
    exit_popup_text = fields.Char("Exit Popup Text")
    exit_popup_button_text = fields.Char("Exit Popup Button Text")
    exit_popup_button_link = fields.Char("Exit Popup Button Link")
