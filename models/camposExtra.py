# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import fields, models

class Employee(models.Model):
    _inherit = "hr.employee"

    account_id = fields.Many2one(
        'account.account',
        string='Account'
    )

    x_nationality = fields.Text(string='Nacionalidad')
    rfc_id = fields.Char(string='RFC')
    curp_id = fields.Char(string='CURP')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: