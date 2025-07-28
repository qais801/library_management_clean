{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Manage books, authors, borrowing records, and memberships.',
    'depends': ['base', 'account'],  # تم إضافة 'account' للفواتير
    'data': [
        # 🔐 ملفات الأمان
        'security/security.xml',
        'security/ir.model.access.csv',

        
        'data/product_data.xml',

        
        'views/res_partner_view.xml',

        
        'views/book_views.xml',
        'views/author_views.xml',
        'views/borrowing_views.xml',

    
        'views/membership_request_views.xml',
        'views/library_menu.xml',
        'views/library_actions.xml',
        'views/library_invoice_menu.xml',
    ],
    'installable': True,
    'application': True,
}


