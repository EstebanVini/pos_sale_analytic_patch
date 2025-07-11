{
    'name': "POS Analytic in Sale Report",
    'version': '15.0.1.0.0',
    'summary': 'Transfiere la cuenta analítica del POS a los reportes de ventas.',
    'author': 'Tu nombre',
    'license': 'AGPL-3',
    'website': '',
    'depends': [
        'pos_sale',
        'pos_analytic_by_config',
    ],
    'data': [
        'views/sale_report_patch.xml',
    ],
    'installable': True,
    'auto_install': False,
}
