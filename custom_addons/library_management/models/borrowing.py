from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class LibraryBorrowing(models.Model):
    _name = 'library.borrowing'
    _description = 'Book Borrowing Record'

    book_id = fields.Many2one('library.book', string='Book', required=True)
    partner_id = fields.Many2one('res.partner', string='Borrower', required=True)
    borrow_date = fields.Date(string='Borrow Date', required=True, default=fields.Date.context_today)
    return_date = fields.Date(string='Return Date')
    returned = fields.Boolean(string='Returned', default=False)

    @api.onchange('borrow_date')
    def _onchange_borrow_date(self):
        if self.borrow_date:
            self.return_date = self.borrow_date + timedelta(days=7)

    @api.model
    def create(self, vals):
        book = self.env['library.book'].browse(vals.get('book_id'))
        if not book.available:
            raise ValidationError("This book is currently not available for borrowing.")
        book.available = False
        return super().create(vals)

    def action_mark_returned(self):
        self.returned = True
        self.book_id.available = True

