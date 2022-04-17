# Copyright 2021 Smartarget <https://smartarget.onkune>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    has_smartarget_corner_ribbon = fields.Boolean(
        "Smartarget Corner Ribbon", related="website_id.has_smartarget_corner_ribbon", readonly=False
    )

    smartarget_user_id = fields.Char(
        related="website_id.smartarget_user_id", readonly=False
    )

    corner_ribbon_text = fields.Char(
        related="website_id.corner_ribbon_text", readonly=False
    )

    corner_ribbon_link = fields.Char(
            related="website_id.corner_ribbon_link", readonly=False
        )
