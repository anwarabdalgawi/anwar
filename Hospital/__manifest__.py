# -*- coding: utf-8 -*-
{
    'name': 'Hospital management',
    'version': '2.0.0',
    'summary': 'Hospital Management',
    'description': """Odoo 15 Development Tutorials""",
    'category': 'Tutorials',
    'author': 'Anwar Abdelgawi',
    'maintainer': 'Odoo Mates',
    'website': 'https://www.odoomates.tech',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'mail',
        'website_slides',
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/doctor.xml',
        'views/patient.xml',

      
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}