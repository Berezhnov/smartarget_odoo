# Copyright 2021 Smartarget <https://smartarget.onkune>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    has_smartarget_email_contact_us = fields.Boolean(
        "Smartarget Email - Contact Us", related="website_id.has_smartarget_email_contact_us", readonly=False
    )

    smartarget_user_id = fields.Char(
        related="website_id.smartarget_user_id", readonly=False
    )

    email = fields.Char(
        related="website_id.email", readonly=False
    )
