# -*- coding: utf-8 -*-
##############################################################################
#
#    Define Angelapper Project Management Permissions
#    Copyright (C) 2014
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
    'name': 'Angelapper Projects Extensions',
    'version': '1.0',
    'category': 'Project Management',
    'summary': """Enhance Project Permission Control""",
    'description': """
        Enhance Project Permission Control
    """,    
    'author': 'Angelapper',
    'website': "http://www.angelapper.com",
    'category': 'Project',
    'version': '0.1',    
    'images': [
    ],    
    'depends': [
      'project','project_issue'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/project_security.xml',
        'project_view.xml'
        ],
    'demo': [
    ],
    'test': [
    ],        
    'installable': True,
    'auto_install': False,    
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: