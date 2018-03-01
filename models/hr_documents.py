# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import fields, models

class Employee(models.Model):
    _inherit = "hr.employee"
    hr_doc_rfc = fields.Boolean(string='RFC')
    hr_doc_curp = fields.Boolean(string='CURP')
    hr_doc_nss = fields.Boolean(string='No. del seguro social')
    hr_doc_acta = fields.Boolean(string='Acta de nacimiento')
    hr_doc_comp_dom = fields.Boolean(string='Comprobante de domicilio')
    hr_doc_canp = fields.Boolean(string='Carta de antecedentes no penales')
    hr_doc_cv = fields.Boolean(string='Curriculum Vitae')
    hr_doc_comp_est = fields.Boolean(string='Comprobante de estudios')
    hr_doc_car_reco = fields.Boolean(string='Carta de recomendación')
    hr_doc_reg_induc = fields.Boolean(string='Registro de inducción')
    hr_doc_req_per = fields.Boolean(string='Requisición de personal')
    hr_doc_diplo = fields.Boolean(string='Diplomado/Constancias... etc.')
    hr_doc_ife = fields.Boolean(string='IFE')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: