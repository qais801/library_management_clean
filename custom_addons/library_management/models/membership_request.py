from odoo import models, fields, api
import random

class LibraryMembershipRequest(models.Model):
    _name = 'library.membership.request'
    _description = 'Library Membership Request'

    partner_id = fields.Many2one('res.partner', string="Member", required=True)
    registration_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date()
    card_id = fields.Char(string="Card ID", readonly=True)
    payment_terms = fields.Selection([('monthly', 'Monthly'), ('yearly', 'Yearly')])
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid'),
        ('active', 'Active')
    ], default='draft')

    membership_lines = fields.One2many('library.membership.line', 'request_id', string="Membership Line")
    invoice_id = fields.Many2one('account.move', string="Invoice", readonly=True)

    def action_confirm(self):
        invoice_lines = [(0, 0, {
            'product_id': line.product_id.id,
            'quantity': 1,
            'price_unit': line.fee,
        }) for line in self.membership_lines]

        invoice = self.env['account.move'].create({
            'partner_id': self.partner_id.id,
            'move_type': 'out_invoice',
            'invoice_line_ids': invoice_lines,
        })
        self.invoice_id = invoice.id
        self.state = 'confirmed'

    def action_mark_paid(self):
        self.state = 'paid'
        card_id = f"LIB-{random.randint(100000, 999999)}"
        self.card_id = card_id
        self.partner_id.library_card_id = card_id
        self.partner_id.is_library_member = True
        self.state = 'active'
