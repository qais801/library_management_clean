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

    # ✅ من Task 5: إظهار رقم بطاقة العضو
    card_id = fields.Char(string="Card ID", readonly=True)

    # ✅ تحديث تاريخ الإرجاع تلقائياً بعد 7 أيام
    @api.onchange('borrow_date')
    def _onchange_borrow_date(self):
        if self.borrow_date:
            self.return_date = self.borrow_date + timedelta(days=7)

    # ✅ من Task 5: عند تغيير العضو، يتم تعبئة Card ID تلقائيًا
    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        self.card_id = self.partner_id.library_card_id

    # ✅ من Task 4: منع استعارة كتاب غير متاح
    @api.model
    def create(self, vals):
        book = self.env['library.book'].browse(vals.get('book_id'))
        if not book.available:
            raise ValidationError("This book is currently not available for borrowing.")
        book.available = False
        return super().create(vals)

    # ✅ من Task 4: عند إرجاع الكتاب
    def action_mark_returned(self):
        self.returned = True
        self.book_id.available = True

    # ✅ من Task 5: التأكد من صلاحية العضوية
    @api.constrains('partner_id', 'borrow_date')
    def _check_membership_validity(self):
        for rec in self:
            membership = self.env['library.membership.request'].search([
                ('partner_id', '=', rec.partner_id.id),
                ('state', '=', 'active'),
                ('registration_date', '<=', rec.borrow_date),
                ('end_date', '>=', rec.borrow_date),
            ], limit=1)
            if not membership:
                raise ValidationError("This member must have an active membership during the borrowing period.")
