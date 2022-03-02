{
    'name': 'Teclib Website Event Google',
    'version': '1.1',
    'author': 'Teclib Group',
    'description': """
    This module makes events indexed by Google.
    """,
    'category': 'Marketing/Events',
    'website': 'https://www.teclib-group.com/',
    'depends': [
        'website_event_sale',
    ],
    'data': [
       # 'views/website_templates.xml',
        'views/website_event_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
}
