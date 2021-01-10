# Copyright 2021 Smartarget <https://smartarget.onkune>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    has_smartarget_follow_us = fields.Boolean("Smartarget Follow Us")

    smartarget_user_id = fields.Char(
        "Smartarget User ID", help="Smartarget User ID (not the entire js code). You can get user ID on smartarget.online"
    )

    social_facebook = fields.Char(
        "Facebook",
    )

    social_instagram = fields.Char(
        "Instagram",
    )

    social_twitter = fields.Char(
        "Twitter",
    )

    social_linkedin = fields.Char(
        "LinkedIn",
    )

    social_pinterest = fields.Char(
        "Pinterest",
    )

    social_youtube = fields.Char(
        "Youtube",
    )


