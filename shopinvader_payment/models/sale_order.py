# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _invader_prepare_payment_transaction_data(self, provider):
        allowed_providers = self.shopinvader_backend_id.payment_method_ids.provider_id
        if provider not in allowed_providers:
            raise UserError(
                _(
                    "Provider %(provider)s is not allowed on backend %(backend)s",
                    provider=provider.name,
                    backend=self.shopinvader_backend_id.name,
                )
            )
        data = super()._invader_prepare_payment_transaction_data(provider)
        allowed_shop_methods = self.shopinvader_backend_id.payment_method_ids
        # TODO: this should probably come from the frontend
        selected = allowed_shop_methods.filtered(lambda m: m.provider_id == provider)
        data["payment_method_id"] = selected.method_id.id
        return data
