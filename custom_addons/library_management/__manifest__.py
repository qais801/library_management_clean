{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Manage books, authors, and borrowing records.',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/author_views.xml',
        'views/borrowing_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}

