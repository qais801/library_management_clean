from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_library_member = fields.Boolean(string="Library Member", default=False)
    library_card_id = fields.Char(string="Card ID", readonly=True)
