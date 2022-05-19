# Copyright 2022 Smartarget <https://smartarget.onkune>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Website(models.Model):
    _inherit = "website"

    has_smartarget_lucky_wheel = fields.Boolean("Smartarget Lucky Wheel")

    smartarget_user_id = fields.Char(
        "Smartarget User ID", help="Smartarget User ID (not the entire js code). Open and follow instructions: https://app.smartarget.online/#/preview/odoo/lucky_wheel"
    )
