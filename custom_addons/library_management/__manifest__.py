{
    'name': 'Library_Management',
    'version': '1.0',
    'summary': 'Manage books, authors, borrowing records, and memberships.',
    'depends': ['base', 'account', 'contacts'],  # إضافة contacts
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/product_data.xml',
        'views/menu_views.xml',
        'views/res_partner_view.xml',
        'views/book_views.xml',
        'views/author_views.xml',
        'views/borrowing_views.xml',
        'views/membership_request_views.xml',
        'views/library_menu.xml',            
        'views/library_actions.xml',
        'views/library_invoice_menu.xml',

        'reports/membership_request_report.xml',
        'reports/membership_request_report_template.xml',
        'reports/membership_requests_report_template.xml',
    ],
    'i18n': [
        'i18n/ar.po',
    ],
    'installable': True,
    'application': True,
}
