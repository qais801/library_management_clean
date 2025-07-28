from odoo import models, fields

class LibraryMembershipLine(models.Model):
    _name = 'library.membership.line'
    _description = 'Membership Line'

    request_id = fields.Many2one('library.membership.request', string="Membership Request")
    product_id = fields.Many2one('product.product', string="Product")
    fee = fields.Float(string="Fee")
