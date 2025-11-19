from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    external_image_url = fields.Char("External Image URL")

    def action_fetch_missing_images(self):
        """Search manufacturer site for missing images and store link"""
        for product in self:
            if not product.image_1920:
                # TODO: implement web search for image; placeholder
                # Set external_image_url or image_1920 accordingly
                pass
