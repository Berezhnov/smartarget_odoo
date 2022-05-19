# Copyright 2022 Smartarget <https://smartarget.onkune>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    has_smartarget_lucky_wheel = fields.Boolean(
        "Smartarget Lucky Wheel", related="website_id.has_smartarget_lucky_wheel", readonly=False
    )

    smartarget_user_id = fields.Char(
        related="website_id.smartarget_user_id", readonly=False
    )
