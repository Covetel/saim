#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from osv import osv, fields
import time

class saim_beneficiario(osv.osv):
    _name = 'saim.beneficiario' 

    def _nombre_beneficiario(self,cr,uid,ids,field,arg,context=False):
        seleccionados = self.pool.get('saim.beneficiario').browse(cr,uid,ids,context=context)
        result = {}
        for each in seleccionados:
            result[each.id] = str(each.nombres)+" "+str(each.apellidos)+" ("+str(each.numero_identidad)+")"
        return result



    _columns = {
       'name': fields.function(_nombre_beneficiario,
                            method=True,type='str', string="Nombre del objeto"),
       'fecha_registro': fields.date("Fecha de Registro"),
       'fecha_nacimiento': fields.date("Fecha de Nacimiento"),
       'numero_expediente': fields.char("Nro. Expediente",size=128),
       'apellidos': fields.char("Apellidos",size=128),
       'nombres': fields.char("Nombres",size=128),
       'numero_identidad': fields.char("Numero Doc. Identidad:",size=128),
       'tipo_documento': fields.selection(( 
			 ("cedulav","Cédula Venezolana"),
			 ("cedulae","Cédula Extranjero"),
			 ("pasaporte","Pasaporte"),
			 ("dni","DNI"),
			 ("otro","Otro")
			),"Tipo de Documento"),
       'nacionalidad': fields.selection(( 
			 ("venezolano","Venezolano"),
			 ("extranjero","Extranjero"),
			),"Nacionalidad"),
       'edad': fields.integer("Edad"),
       'estado_civil': fields.selection(( 
			 ("soltero","Soltero"),
			 ("casado","Casado"),
			 ("otro","Otro"),
			),"Estado Civil"),
       'genero': fields.selection(( 
			 ("f","Femenino"),
			 ("m","Masculino"),
			),"Género"),
       'telefono': fields.char("Teléfono",size=128),
       'descripcion_solicitud': fields.text("Descripción solicitud",size=128),
       'direccion_habitacion': fields.char("Dirección Habitación",size=256),
       'estado': fields.char("Estado",size=128),
       'municipio': fields.char("Municipio",size=128),
       'parroquia': fields.char("Parroquia",size=128),
       'actividad_actual': fields.char("Actividad Laboral Actual",size=128),
       'profesion': fields.char("Profesión y oficio",size=128),
       'lugar_de_trabajo': fields.char("Lugar de trabajo",size=128),
       'actividad_comercial': fields.selection(( 
			 ("s","Si"),
			 ("n","No"),
			),"Realiza alguna Actividad Comercial"),
       'actividad_comercial_detalle': fields.char("Cual",size=128),
       'tipo_ingreso': fields.selection(( 
			 ("d","Diario"),
			 ("s","Semanal"),
			 ("q","Quincenal"),
			 ("m","Mensual"),
			 ("d","A Destajo"),
			 ("n","Ninguno"),
			),"Tipo de Ingreso"),
       'bono_alimentacion': fields.selection(( 
			 ("t","Ticket"),
			 ("j","Tarjeta"),
			),"Bono Alimentación"),
       'monto_alimentacion': fields.float("Monto del Bono Alimentación"),
       'asignacion_economica': fields.boolean("Recibe alguna asignación ecnómica por parte del Estado o institución privada."),
       'fuente_asignacion_economica': fields.char("Especifique fuente de la asignación económica.",size=128),
       ## todo: GRUPO FAMILIAR
       'instruccion_basica': fields.selection(( 
			 ("n","Ninguna"),
			 ("i","Incompleta"),
			 ("c","Completa"),
			),"Básica"),      
       'instruccion_media': fields.selection(( 
			 ("n","Ninguna"),
			 ("i","Incompleta"),
			 ("c","Completa"),
			),"Media"),      
       'instruccion_universitaria': fields.selection(( 
			 ("n","Ninguna"),
			 ("i","Incompleta"),
			 ("c","Completa"),
			),"Universitarios"),      
       'discapacidad': fields.selection(( 
			 ("s","Si"),
			 ("n","No"),
			),"Presenta o Padece alguna Enfermedad o discapacidad."),      
       'discapacidad_detalle': fields.char("Especifique",size=128),      
       'requiere_tratamiento': fields.selection(( 
			 ("s","Si"),
			 ("n","No"),
			),"Requiere de tratamiento permanente"),      
       'tratamiento_detalle': fields.char("Especifique",size=128),
	#todo: Falta area habitacional, 
       'familiares_ids': fields.one2many('saim.familiar','beneficiario_id',"Grupo Familiar",required=True)
    }

    _defaults = {
        "fecha_registro": lambda *a: time.strftime('%Y-%m-%d'),
    }

saim_beneficiario()

class saim_familiar(osv.osv):
    _name = "saim.familiar"


    def _nombre_familiar(self,cr,uid,ids,field,arg,context=False):
        seleccionados = self.pool.get('saim.familiar').browse(cr,uid,ids,context=context)
        result = {}
        for each in seleccionados:
            result[each.id] = str(each.nombre)+" "+str(each.apellido)+" ("+str(each.cedula)+")"
        return result



    _columns = {
       'name': fields.function(_nombre_familiar,
                            method=True,type='str', string="Nombre del objeto"),
       'nombre': fields.char("Nombre",size=128),
       'apellido': fields.char("Apellido",size=128),
       'cedula': fields.char("Cedula Identidad",size=128),
       'edad': fields.char("Edad",size=128),
       'genero': fields.selection(( 
			 ("f","Femenino"),
			 ("m","Masculino"),
			),"Género"),
       'parentesco': fields.selection(( 
			 ("p","Padre"),
			 ("m","Madre"),
			 ("h","Hijo"),
			),"Género"),
       'ocupacion': fields.char("Ocupación",size=128),
       'edad': fields.integer("Edad"),
       'ingresos': fields.float("Ingresos"),
       'beneficiario_id': fields.many2one('saim.beneficiario',"Beneficiario",required=True)
    }

saim_familiar()

class saim_mision(osv.osv):
    _name = 'saim.mision'

    _columns = {
       'nombre': fields.char("Nombre",size=128),
       'descripcion': fields.text("Descripción",size=256),
       'edad': fields.char("Edad",size=128),
       'beneficio_economico': fields.selection((
			 ("s","Si"),
			 ("n","No"),
			),"Brinda beneficio económico"),
    }

saim_mision()

"""
class vehiculos_vehiculo(osv.osv):
    _name = 'vehiculos.vehiculo'

    def _nombre_vehiculo(self,cr,uid,ids,field,arg,context=False):
        seleccionados = self.pool.get('vehiculos.vehiculo').browse(cr,uid,ids,context=context)
        result = {}
        for each in seleccionados:
            result[each.id] = str(each.placa)+" "+str(each.marca)+" "+str(each.modelo)
        return result

    def _recorrido_vehiculo(self,cr,uid,ids,field,arg,context=False):
        seleccionados = self.pool.get('vehiculos.vehiculo').browse(cr,uid,ids,context=context)
        result = {}
        for each in seleccionados:
            try:
                result[each.id] = each.registro_ids[-1].kms
            except:
                result[each.id] = 0
        return result



    _columns = {
            'name': fields.function(_nombre_vehiculo,
                            method=True,type='str', string="Nombre"),
            'placa': fields.char('Placa', size=128, required=True),
            #'tu': fields.integer('TU'),
            'marca': fields.char('Marca', size=128),
            'modelo': fields.char('Modelo', size=128),
            'tipo': fields.char('Tipo', size=128),
            'color': fields.char('Color', size=128),
            'ano': fields.integer('Año'),
            'registro_ids': fields.one2many('vehiculos.registro', 'vehiculo_id',string="Registros de recorrido"),
            'odometro': fields.function(_recorrido_vehiculo,
                            method=True,type='float', string="Kms Recorridos"),
            #'company_id': fields.many2one('res.company', 'Empresa'),
            }

    _default = {
            'company_id': lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid, 'vehiculos.vehiculo', context=c), 
            }

vehiculos_vehiculo()


class vehiculo_registro(osv.osv):
    _name = 'vehiculos.registro'

    def _nombre_registro(self,cr,uid,ids,field,arg,context=False):
        seleccionados = self.pool.get('vehiculos.registro').browse(cr,uid,ids,context=context)
        result = {}
        for each in seleccionados:
            result[each.id] = str(each.fecha)+" "+str(each.kms)
        return result



    _columns = {
            'name': fields.function(_nombre_registro,
                            method=True, string="Nombre"),
            'vehiculo_id': fields.many2one('vehiculos.vehiculo',string='Vehiculo',required=True,ondelete='cascade'),
            'fecha': fields.date('Fecha del registro'),
            'kms': fields.float('Medicion del Odometro'),
            }

    _defaults = {
            'fecha': lambda *a: time.strftime('%Y-%m-%d'),
            }

vehiculo_registro()
"""
