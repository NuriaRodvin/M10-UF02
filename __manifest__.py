{
    'name': 'ecodelivery',
    'version': '12.0.1.0.0',
    'category': 'Sales',
    'summary': 'Gestión ecológica de entregas por Nuria',
    'author': 'Nuria Rodriguez',
    'depends': ['sale'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/transporte_eco_views.xml',
        'views/envio_eco_views.xml',
        'views/eco_delivery_menu.xml',
    ],
    'images': ['static/description/icon.png'],
   


    'installable': True,
    'application': True,
}
