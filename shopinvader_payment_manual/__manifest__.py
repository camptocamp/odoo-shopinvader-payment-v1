# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Shopinvader Payment Manual",
    "summary": """
        REST Services for manual payment (like bank transfer, check...)""",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV, Camptocamp",
    "website": "https://github.com/camptocamp/odoo-shopinvader-payment-v1",
    "depends": [
        "invader_payment_manual",
        "shopinvader_payment",
        "payment_custom",
    ],
    "demo": ["demo/payment_demo.xml"],
    "autoinstall": True,
    "installable": True,
}
