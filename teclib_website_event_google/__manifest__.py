{
    'name': 'Teclib Website Events Google',
    'version': '1.1',
    'author': 'Teclib ERP',
    'website': 'https://www.teclib-erp.com',
    'sequence': 0,
    'certificate': '',
    'license': 'LGPL-3',
    'description': """
    This module makes Odoo events templates compatible with Google Indexation requirements
    """,
    'category': 'Specific Modules/Events',
    'depends': [
        'website_event_sale',
    ],
    'data': [
        'views/website_event_templates.xml',
        'views/website_event_registration_templates.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
