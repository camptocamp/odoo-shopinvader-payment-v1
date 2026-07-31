# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_test_helper import FakeModelLoader

from odoo.addons.shopinvader.tests.test_cart import CommonConnectedCartCase


class ShopinvaderPaymentCase(CommonConnectedCartCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.cart = cls.env.ref("shopinvader.sale_order_2")
        cls.shopinvader_session = {"cart_id": cls.cart.id}

        with cls.work_on_services(
            cls, partner=None, shopinvader_session=cls.shopinvader_session
        ) as work:
            cls.cart_service = work.component(usage="cart")

        cls.loader = FakeModelLoader(cls.env, cls.__module__)
        cls.loader.backup_registry()
        from .fake_models import PaymentProvider

        cls.loader.update_registry((PaymentProvider,))

        cls._setup_payment()

    @classmethod
    def tearDownClass(cls):
        cls.loader.restore_registry()
        super().tearDownClass()

    @classmethod
    def _setup_payment(cls):
        vals = {"name": "Fake Provider", "code": "shopinvader_payment_test"}
        cls.payment_provider = cls.env["payment.provider"].create(vals)
        vals = {"name": "Fake Provider", "code": "shopinvader_payment_test"}
        cls.payment_method = cls.env["payment.method"].create(vals)
        vals = {
            "provider_id": cls.payment_provider.id,
            "backend_id": cls.backend.id,
            "method_id": cls.payment_method.id,
        }
        cls.shop_payment = cls.env["shopinvader.payment"].create(vals)

    def _set_transaction(self):
        self.transaction = self.env["payment.transaction"].create(
            {
                "provider_id": self.shop_payment.provider_id.id,
                "payment_method_id": self.shop_payment.method_id.id,
                "partner_id": self.cart.partner_id.id,
                "amount": self.cart.amount_total,
                "currency_id": self.cart.currency_id.id,
                "sale_order_ids": [(6, 0, self.cart.ids)],
            }
        )

    def test_no_provider(self):
        self.shop_payment.unlink()
        response = self.cart_service.dispatch("search", params={"id": self.cart.id})
        self.assertEqual(
            response.get("data").get("payment").get("available_methods").get("count"),
            0,
        )

    def test_provider(self):
        response = self.cart_service.dispatch("search", params={"id": self.cart.id})
        self.assertEqual(
            response.get("data").get("payment").get("available_methods").get("count"),
            1,
        )
        items = (
            response.get("data").get("payment").get("available_methods").get("items")
        )
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].get("name"), "Fake Provider")

    def test_transactions(self):
        self._set_transaction()
        response = self.cart_service.dispatch("search", params={"id": self.cart.id})
        transactions = response.get("data").get("transactions")
        transaction = transactions[0]
        self.assertEqual(transaction.get("state"), "draft")
