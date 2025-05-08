# Copyright 2025 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.component.core import Component


class InvaderPaymentService(Component):
    _inherit = "invader.payment.service"

    def _check_provider(self, provider, given_code):
        provider = provider.sudo()
        # Validate custom code
        if provider.code == "custom":
            return self._check_provider_code(provider.custom_code, given_code)
        return super()._check_provider(provider, given_code)
