# Copyright 2021 Smartarget <https://smartarget.onkune>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    has_smartarget_information_message = fields.Boolean(
        "Smartarget Information Message", related="website_id.has_smartarget_information_message", readonly=False
    )

    smartarget_user_id = fields.Char(related="website_id.smartarget_user_id", readonly=False)
    information_message_title = fields.Char(related="website_id.information_message_title", readonly=False)
    information_message_text = fields.Char(related="website_id.information_message_text", readonly=False)
    information_message_button_text = fields.Char(related="website_id.information_message_button_text", readonly=False)
    information_message_button_link = fields.Char(related="website_id.information_message_button_link", readonly=False)


