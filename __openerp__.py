# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Modulo Documentos del Empleado',
    'version': '1.0',
    'author': 'Pablo Osorio Gama',
    'category': 'Tools',
    'summary': 'Documentación de empleados',
    'website': '',
    'description': """
Documentación entregada de manera fisica.
    """,
    'depends': ['hr_applicant_recruitment'],
    'data': [
        'views/hr_documents_employee_view.xml',
    ],
    'installable': True,
    'auto_install': True,
}