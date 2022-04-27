# -*- coding: utf-8 -*-

{
    'name': "Dynamic Cheque Print",
    "author": "",
    'version': "15.0.0.1",
    'summary': "This apps helps to print the cheque and also can configure different bank's cheque formats.",
    'description': """This apps helps to print the cheque and also can configure different bank's cheque formats.""",
    "license": "OPL-1",
    'depends': ['base', 'account', 'account_check_printing'],
    'data': [
        'security/ir.model.access.csv',
        'data/cheque_format_data.xml',
        'reports/dynamic_cheque_report_templete.xml',
        'wizard/print_dynamic_cheque_wizard_view.xml',
        'views/dynamic_cheque_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
