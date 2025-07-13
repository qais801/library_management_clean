from odoo import models, fields, api
from datetime import timedelta

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author_id = fields.Many2one('library.author', string='Author')
    description = fields.Text()
    publish_date = fields.Date()
    available = fields.Boolean(default=True)


class LibraryBorrowing(models.Model):
    _name = 'library.borrowing'
    _description = 'Book Borrowing Record'

    book_id = fields.Many2one('library.book', string='Book', required=True)
    partner_id = fields.Many2one('res.partner', string='Borrower', required=True)
    borrow_date = fields.Date(default=fields.Date.today)
    return_date = fields.Date()
    returned = fields.Boolean(default=False)

    @api.onchange('borrow_date')
    def _onchange_borrow_date(self):
        if self.borrow_date:
            self.return_date = self.borrow_date + timedelta(days=7)

    def action_mark_returned(self):
        self.returned = True
        self.book_id.available = True
