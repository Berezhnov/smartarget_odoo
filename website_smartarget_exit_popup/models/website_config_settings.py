# Copyright 2021 Smartarget <https://smartarget.onkune>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    has_smartarget_exit_popup = fields.Boolean(
        "Smartarget Exit Popup", related="website_id.has_smartarget_exit_popup", readonly=False
    )

    smartarget_user_id = fields.Char(
        related="website_id.smartarget_user_id", readonly=False
    )

    exit_popup_header = fields.Char(related="website_id.exit_popup_header", readonly=False)
    exit_popup_text = fields.Char(related="website_id.exit_popup_text", readonly=False)
    exit_popup_button_text = fields.Char(related="website_id.exit_popup_button_text", readonly=False)
    exit_popup_button_link = fields.Char(related="website_id.exit_popup_button_link", readonly=False)
