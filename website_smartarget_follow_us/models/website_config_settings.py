# Copyright 2021 Smartarget <https://smartarget.onkune>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    has_smartarget_follow_us = fields.Boolean(
        "Smartarget Follow Us", related="website_id.has_smartarget_follow_us", readonly=False
    )

    smartarget_user_id = fields.Char(
        related="website_id.smartarget_user_id", readonly=False
    )

    social_facebook = fields.Char(
        related="website_id.social_facebook", readonly=False
    )

    social_instagram = fields.Char(
        related="website_id.social_instagram", readonly=False
    )

    social_twitter = fields.Char(
        related="website_id.social_twitter", readonly=False
    )

    social_linkedin = fields.Char(
        related="website_id.social_linkedin", readonly=False
    )

    social_pinterest = fields.Char(
        related="website_id.social_pinterest", readonly=False
    )

    social_youtube = fields.Char(
        related="website_id.social_youtube", readonly=False
    )


