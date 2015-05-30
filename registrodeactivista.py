# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
# Generated by the Odoo plugin for Dia !
from openerp import models, fields, api

class Activista(models.Model):
    """Registro de Activista de Bachaco-ve"""
    _name = 'activista'
    _rec_name = 'nombres'
    nombres = fields.Char('Nombre',size=30,required=True, help='Nombre del Activista')
    apellidos = fields.Char('Apellidos',size=30,required=True, help='Apellidos del Activista')
    cedula = fields.Char('Cédula',size=10,required=True, help='Cédula del Activista')
    telefono_ids = fields.One2many('telefonoactivista','activista_id','Telefono',required=True, help='Telefono(s) del Activista')
    correo = fields.Char('Correo Electrónico',size=30,required=True, help='Correo Electrónico del Activista')
    dom_estado_id = fields.Many2one('estado','Estado', help='Estado de Domicilio del Asistente')
    dom_municipio_id = fields.Many2one('municipio','Municipio', help='Municipio de Domicilio del Asistente')
    dom_parroquia_id = fields.Many2one('parroquia','Parroquia', help='Parroquia de Domicilio del Asistente')
    proyectos_ids = fields.One2many('proyectostrabajados','activista_id','Proyectos en los que ha trabajado', help='Proyectos en los que ha trabajado')
    trab_estado_id = fields.Many2one('estado','Estado', help='Estado del lugar de trabajo')
    trab_municipio_id = fields.Many2one('municipio','Municipio')
    trab_parroquia_id = fields.Many2one('parroquia','Parroquia', help='Parroquia del lugar de trabajo')
    repositorio_tipo = fields.Selection([('B','Bitbucket'),('G','GitHub')],'Tipo de Repositorio',required=True, help='Tipo de Repositorio ')
    repositorio_url = fields.Char('URL de la Cuenta',size=50, help='URL de la Cuenta del Repositorio')
    
    @api.onchange('dom_estado_id')
    def _on_change_limpiar_dom(self):
        self.dom_municipio_id = '' 
        self.dom_parroquia_id = ''

    @api.onchange('dom_municipio_id')
    def _on_change_limpiar_dom_parroquia(self):
        self.dom_parroquia_id = ''
        
    @api.onchange('trab_estado_id')
    def _on_change_limpiar_trab(self):
        self.trab_municipio_id = '' 
        self.trab_parroquia_id = ''

    @api.onchange('trab_municipio_id')
    def _on_change_limpiar_trab_parroquia(self):
        self.trab_parroquia_id = ''

class TelefonoActivista(models.Model):
    """Telefono del Activista"""
    _name = 'telefonoactivista'
    _rec_name = 'telefono'
    telefono = fields.Char('Telefono',size=12,required=True, help='Número de telefono del Activista')
    activista_id = fields.Many2one('activista','Activista', help='Relacion entre el numero de telefono y el activista')


class Estado(models.Model):
    """Estados de Venezuela"""
    _name = 'estado'
    _rec_name = 'estado'
    codigo = fields.Char('Código', size=3, required=True, help='Código del Estado')
    estado = fields.Char('Estado',size=30,required=True, help='Nombre del Estado')


class Municipio(models.Model):
    """Municipios de los Estados de Venezuela"""
    _name = 'municipio'
    _rec_name = 'municipio'
    codigo = fields.Char('Código',size=3,required=True, help='Código del Municipio')
    municipio = fields.Char('Municipio',size=30,required=True, help='Código del Municipio')
    estado_id = fields.Many2one('estado','Estado', help='Nombre del Estado al cual pertenece el municipio')


class Parroquia(models.Model):
    """Parroquia de los Estados de Venezuela"""
    _name = 'parroquia'
    _rec_name = 'parroquia'
    codigo = fields.Char('Código',size=3,required=True, help='Código de Identificación de la Parroquia')
    parroquia = fields.Char('Parroquia',size=30,required=True, help='Nombre de la Parroquia')
    municipio_id = fields.Many2one('municipio', 'Municipio', help='Municipio al cual pertenece la Parroquia')


class ProyectosTrabajados(models.Model):
    """Proyectos en los que ha trabajado el Activista"""
    _name = 'proyectostrabajados'
    _rec_name = 'proyecto'
    proyecto = fields.Char('Proyecto',size=50,required=True, help='Nombre del Proyecto en el que ha trabajado')
    activista_id = fields.Many2one('activista','Activista')


