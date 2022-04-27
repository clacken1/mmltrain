# -*- coding: utf-8 -*-
from odoo import fields, models


class DynamicChequeTemplate(models.AbstractModel):
    _name = 'report.dynamic_cheque_print.report_dynamic_check_print'
    _description = 'Dynamic Cheque Print Report'

    def _get_report_values(self, docids, data=None):
        wizard = self.env['dynamic.cheque.wizard'].browse(docids)

        return {
            'doc_model': 'dynamic.cheque',
            'cheque_format': wizard.cheque_format,
            'payment_id': wizard.payment_id,
        }


class ReportPaperformat(models.Model):
    _inherit = "report.paperformat"

    custom_report = fields.Boolean('Temp Formats', default=False)
