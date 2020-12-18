# @author Aashim Bajracharya <ashimbazracharya@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, api, _
from odoo.exceptions import Warning, ValidationError, UserError

import logging

_logger = logging.getLogger(__name__)


class UpdateProductPrice(models.TransientModel):
    _name = 'update.product.price'

    # todo
    # list out the products to update from the context

    # @api.multi
    # def update_price(self):
        # todo
        # method to update the price of the list of the products
