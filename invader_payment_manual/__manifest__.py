# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Invader Payment Manual",
    "summary": """
        REST Services for manual payment like bank transfer,
        check ... (base module)""",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV, Camptocamp",
    "website": "https://github.com/camptocamp/odoo-shopinvader-payment-v1",
    "depends": ["invader_payment", "base_rest", "payment_custom"],
    "external_dependencies": {"python": ["cerberus"]},
    "installable": True,
}
