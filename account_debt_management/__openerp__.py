# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Account Debt Management',
    'version': '8.0.0.6.0',
    'category': 'Account Reporting',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'depends': [
        'account_voucher_payline',
        # en v9 no depender de este y copiar algunas cosas
        'account_followup',
        'report_aeroo',
    ],
    'data': [
        'report/account_debt_report.xml',
        'report/account_debt_line_view.xml',
        'data/mail_data.xml',
        'wizard/account_debt_report_wizard_view.xml',
        'views/account_move_line_view.xml',
        'views/res_partner_view.xml',
        'views/account_voucher_view.xml',
        'res_config_view.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
