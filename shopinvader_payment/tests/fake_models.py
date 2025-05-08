# Copyright 2025 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import fields, models


class PaymentProvider(models.Model):
    _inherit = "payment.provider"

    code = fields.Selection(
        selection_add=[("shopinvader_payment_test", "shopinvader_payment_test")],
        ondelete={"shopinvader_payment_test": "set default"},
    )
