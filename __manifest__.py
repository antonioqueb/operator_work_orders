{
    'name': 'Operator Work Orders',
    'version': '1.0',
    'category': 'Manufacturing',
    'summary': 'Group with permissions only for managing work orders',
    'depends': ['base', 'mrp'],
    'data': [
        'security/operator_work_orders_security.xml',
        'security/ir.model.access.csv',
        'views/operator_work_orders_view.xml',
    ],
    'installable': True,
    'application': False,
}
