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
       'familiares_ids': fields.one2many('saim.familiar','beneficiario_id',"Grupo Familiar",required=True),
       #area habitacional
       'tipo_vivienda': fields.selection((
			 ("c","Casa"),
			 ("a","Apartamento"),
			 ("r","Rancho"),
			 ("h","Habitación"),
			 ("s","Situación de Calle"),
			 ("o","Otro"),
			),"Tipo de vivienda"),
       'condicion_tenencia': fields.selection((
			 ("p","Propia"),
			 ("a","Alquilada"),
			 ("c","Compartida"),
			 ("pr","Prestada"),
			 ("i","Invadida"),
			 ("o","Otro"),
			),"Condiciones de tenencia"),
       'tipo_pared': fields.selection((
			 ("f","Frisada"),
			 ("z","Zinc"),
			 ("m","Madera"),
			 ("o","Otro"),
			),"Tipo de pared"),
       'tipo_piso': fields.selection((
			 ("t","Tierra"),
			 ("c","Cemento"),
			 ("ca","Ceramica"),
			 ("o","Otro"),
			),"Tipo de piso"),
       'tipo_techo': fields.selection((
			 ("p","Platabanda"),
			 ("a","Asbesto"),
			 ("ac","Acerolit"),
			 ("z","Zinc"),
			 ("o","Otro"),
			),"Tipo de techo"),
        #Área físico ambiental
       'sala': fields.boolean("Sala"),
       'cocina': fields.boolean("Cocina"),
       'comedor': fields.boolean("Comedor"),
       'sala_comedor': fields.boolean("Sala-Comedor"),
       'habitacion': fields.boolean("Habitación"),
       'bano': fields.boolean("Baño"),
       'garaje': fields.boolean("Garaje"),
       'o_ambiental': fields.boolean("Otro"),
        #Enseres en la vivienda
       'nevera': fields.boolean("Nevera"),
       'cocina': fields.boolean("Cocina"),
       'camas': fields.boolean("Camas"),
       'tv': fields.boolean("TV"),
       'tv_cable': fields.boolean("TV por cable"),
       'muebles': fields.boolean("Muebles"),
       'compu': fields.boolean("Computadora"),
       'aire': fields.boolean("Aire acondicionado"),
       'radio': fields.boolean("Radio"),
       'o_enseres': fields.boolean("Otro"),
       'status_terreno': fields.selection((
			 ("p","Propio"),
			 ("i","Invadido"),
			 ("pri","Privado"),
			 ("pre","Prestado"),
			 ("o","Otro"),
			),"Estatus del terreno"),
       'doc_propiedad': fields.selection((
			 ("su","Título supletorio"),
			 ("pro","Título de propiedad"),
			 ("n","No tiene"),
			 ("o","Otro"),
			),"Documento de propiedad"),
       #características servicios públicos
       'basura': fields.selection((
			 ("c","Container"),
			 ("au","Aseo urbano"),
			 ("al","Aire libre"),
			 ("q","Quemada"),
			 ("o","Otro"),
			),"Recolección de basura"),
       'electrico': fields.selection((
			 ("e","Electricidad"),
			 ("pe","Planta eléctrica"),
			 ("a","Alambrado público"),
			 ("ss","Sin servicio"),
			 ("o","Otro"),
			),"Servicio electrico"),
       'gas': fields.selection((
			 ("d","Gas directo"),
			 ("b","Bombona"),
			 ("l","Leña"),
			 ("o","Otro"),
			),"Gas domestico"),
       'agua_blancas': fields.selection((
			 ("t","Tuberías"),
			 ("ll","Lluvia"),
			 ("r","Rio"),
			 ("c","Cisterna"),
			 ("o","Otro"),
			),"Aguas blancas"),
       'telefono': fields.selection((
			 ("c","Celular"),
			 ("d","Domiciliaria"),
			 ("i","Internet"),
			 ("s","Sin servicio"),
			),"Teléfono"),
       'transporte': fields.selection((
			 ("pro","Propio"),
			 ("pri","Privado"),
			 ("pu","Público"),
			 ("o","Otro"),
			),"Transporte"),
       'aguas_servidas': fields.selection((
			 ("c","Cloaca"),
			 ("al","Aire Libre"),
			 ("l","Letrina"),
			 ("p","Pozo Séptico"),
			 ("o","Otro"),
			),"Aguas servidas"),
       #Participación socio-comunitaria
        #Organizaciones poulares dentro de la comunidad
       'comite_salud': fields.boolean("Comité de salud"),
       'club_abuelo': fields.boolean("Club de abuelo"),
       'partidos_politicos': fields.boolean("Partidos políticos"),
       'casa_alimentacion': fields.boolean("Casa de alimentación"),
       'mesa_tecnica_agua': fields.boolean("Mesa técnica de agua"),
       'consejo_comunal': fields.boolean("Consejos comunales"),
       'ctu': fields.boolean("CTU"),
       'o_organizaciones': fields.char("Otros",size=128),
       'pertenece_organizaciones': fields.selection((
            ("s","Si"),
            ("n","No"),
           ),"Pertenece a alguna de estas organizaciones"),
       'organizacion_pertenece': fields.char("A cual organización pertenece",size=128),
       'misiones_ids': fields.one2many('saim.misiones','beneficiario_id',"Misiones en la comunidad",required=True),
       'reg_cne': fields.selection((
            ("s","Si"),
            ("n","No"),
           ),"Se encuentra registrado en el CNE"),
       'militante_politico': fields.selection((
            ("s","Si"),
            ("n","No"),
           ),"Es militante de alguna organización política"),
       'diagnostico_caso': fields.text("Diagnóstico del caso",size=128),
       'recomendaciones': fields.text("Recomendaciones",size=128),
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
       'beneficiario_id': fields.many2one('saim.beneficiario',"Beneficiario",required=True)
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
