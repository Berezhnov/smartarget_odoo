# Copyright 2021 Smartarget <https://smartarget.onkune>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    has_smartarget_viber_contact_us = fields.Boolean(
        "Smartarget Viber - Contact Us", related="website_id.has_smartarget_viber_contact_us", readonly=False
    )

    smartarget_user_id = fields.Char(
        related="website_id.smartarget_user_id", readonly=False
    )

    viber_phone_number = fields.Char(
        related="website_id.viber_phone_number", readonly=False
    )
