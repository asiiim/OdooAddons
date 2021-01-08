# @author Aashim Bajracharya <ashimbazracharya@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import api, fields, models, tools, _

import logging

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = "product.template"
