# *-* coding=utf-8 *-* 
import xmlrpclib

import settings

username = settings.username
pwd = settings.pwd
dbname = settings.dbname



# Get the uid
sock_common = xmlrpclib.ServerProxy ('http://localhost:8069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)
print uid

#replace localhost with the address of the server
sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
print sock

def mayus(cadena):
    return " ".join([each.capitalize() for each in cadena.split(" ")])

nombre_mision = "Robinson"

buscar = [("name","=",nombre_mision)]
mision_id = sock.execute(dbname, uid, pwd, 'saim.mision', 'search', buscar)

if len(mision_id)==0:
    mision = {
       'name': nombre_mision,
    }
    mision_id= sock.execute(dbname, uid, pwd, 'saim.mision', 'create', mision) 


error = open("errores_"+nombre_mision+".log","a+")

import glob
print "Going to import ",glob.glob("robinson*")
for each_origin_file in glob.glob("robinson*"): #(a repetirse para todos los tabs del archivo, exportados en csv: ['sucre_coordinadores.csv', 'sucre_docentes.csv', 'sucre_operativo.csv', 'sucre_triunfadores.csv']
    source_table = open(each_origin_file)
    print "opened: ",each_origin_file
    
    for line in source_table.readlines()[5:]:
            print line
            """
            l[0] #Expediente (no confirmado)
            l[1] #Cedula
            l[2] #Nombres
            l[3] #Apellidos
            l[4] #Fecha de nacimiento dd/mm/aaaa
            l[5] #genero (f,m)
            l[6] #estado civil (c,s)
            l[7] #nacionalidad (v,e)
            l[8] #estado
            l[9] #municipio 
            l[10] #parroquia 
            l[12] #direccion
            l[13] #caracteristicas de la vivienda (propia,alquilada)
            l[14] #telefono
            l[15] #celular
            l[16] #indígena (0=si,1=no)
            l[17] #descripcion discapacidad o enfermedad
            l[18] #adquirida = 0 , congenita = 1 #NO EN MODELOS
            l[19] #primaria ("primaria completa", "primaria incompleta") #NO EN MODELOS 
            l[20] #secundaria ("secundaria completa", "secundaria incompleta") #NO EN MODELOS
            l[21] #universitaria ("universitario") #NO EN MODELOS
            l[22] #habilidades #NO EN MODELOS
            l[23] #trabajo fijo = 0 , trabajo temporal = 1 #NO EN MODELOS
            l[24] #Privada = 0 , publico = 1 #NO EN MODELOS
            l[26] #"negocio propio" #NO EN MODELOS
            l[27] #ingreso mensual familiar

            """

            try:
            #if True:

                l = line.split(",")
                print "Procesando: ",l
                
                fecha_original = l[4].split("/")
                fecha_nacimiento = fecha_original[1]+"/"+fecha_original[0]+"/"+fecha_original[2]

                print "diccionario beneficiario, creado"
                beneficiario = {
                   #'numero_expediente': l[0],
                   'numero_identidad': "V-"+l[1],
                   'nombres': mayus(l[2]),
                   'apellidos': mayus(l[3]),
                   'sexo': l[5].lower(),
                   'direccion_habitacion': l[12],
                   'fecha_nacimiento': fecha_nacimiento,
                   'numero_telefono': l[14],
                   'tipo_discapacidad': l[18],
                   'habilidades': l[22],
                   'mision_id': mision_id[0],
                }

                print "diccionario beneficiario, creado2"

                try:
                    if len(l[27])>0:
                        beneficiario.update({'ingresos':float(l[27])})
                        print "Ingresos, definidos"
                except:
                    pass

                try:
                    if len(l[26])>0:
                        beneficiario.update({'ingresos':float(l[26])})
                        print "Ingresos, definidos"
                except:
                    pass



                if len(l[17])>0:
                    beneficiario.update({'discapacidad':'s'})
                    beneficiario.update({'discapacidad_detalle':l[17]})
                else:
                    beneficiario.update({'discapacidad':'n'})
                print "discapacidad"

                try:
                    if cmp(l[26],'negocio propio')==0 or cmp(l[27],'negocio propio')==0:
                        beneficiario.update({'negocio_propio':'1'})
                except:
                    print "Error con negocio_propio"
                    pass

                print "negocio_propio"


                try:
                    if cmp(l[24],'0')==0:
                        beneficiario.update({'fuente_trabajo':'0'})
                    if cmp(l[24],'1')==0:
                        beneficiario.update({'fuente_trabajo':'1'})
                except:
                    print "Error con fuente_trabajo"
                    pass



                try:
                    if cmp(l[24],'0')==0:
                        beneficiario.update({'fuente_trabajo':'0'})
                    if cmp(l[24],'1')==0:
                        beneficiario.update({'fuente_trabajo':'1'})
                except:
                    print "Error con fuente_trabajo"
                    pass

                try:
                    if cmp(l[23],'0')==0:
                        beneficiario.update({'duracion_trabajo':'0'})
                    if cmp(l[23],'1')==0:
                        beneficiario.update({'duracion_trabajo':'1'})
                except:
                    print "Error con primaria"
                    pass



                try:
                    if cmp(l[19],'primaria completa')==0:
                        beneficiario.update({'primaria':'1'})
                    if cmp(l[19],'primaria incompleta')==0:
                        beneficiario.update({'primaria':'0'})
                except:
                    print "Error con primaria"
                    pass

                try:
                    if cmp(l[20],'secundaria completa')==0:
                        beneficiario.update({'secundaria':'1'})
                    if cmp(l[20],'secundaria incompleta')==0:
                        beneficiario.update({'secundaria':'0'})
                except:
                    print "Error con secundaria"
                    pass

                try:
                    if cmp(l[21],'universitario')==0:
                        beneficiario.update({'universitario':'1'})
                except:
                    print "Error con universitario"
                    pass


                try:
                    if cmp(l[6].lower(),'c')==0:
                        beneficiario.update({'estado_civil':'casado'})
                    if cmp(l[6].lower(),'s')==0:
                        beneficiario.update({'estado_civil':'soltero'})
                except:
                    print "Error con estado_civil"
                    pass

                try:
                    if cmp(l[7].lower(),'v')==0:
                        beneficiario.update({'nacionalidad':'venezolano'})
                    if cmp(l[7].lower(),'e')==0:
                        beneficiario.update({'nacionalidad':'extranjero'})
                except:
                    print "Error con nacionalidad"
                    pass
                print "nacionalidad"

                try:
                    if cmp(l[6],'propia')==0:
                        beneficiario.update({'condicion_tenencia':'p'})
                    if cmp(l[6],'alquilada')==0:
                        beneficiario.update({'condicion_tenencia':'a'})
                except:
                    print "Error con condicion_Tenencia"
                    pass

                try:
                    if cmp(l[16],'0')==0:
                        beneficiario.update({'indigena':'s'})
                    if cmp(l[16],'1')==0:
                        beneficiario.update({'indigena':'n'})
                except:
                    print "Error con indigena"
                    pass



                if len(l[8])>0:
                    buscar = [("name","=",mayus(l[8]))]
                    try:
                        estado_id = sock.execute(dbname, uid, pwd, 'saim.estados', 'search', buscar)[0]
                        beneficiario.update({'estado': estado_id})
                        print "estado: ",estado_id
                    except:
                        pass 

                if len(l[9])>0:
                    buscar = [("name","=",mayus(l[9]))]
                    try: 
                        municipio_id = sock.execute(dbname, uid, pwd, 'saim.municipios', 'search', buscar)[0]
                        beneficiario.update({'municipio': municipio_id})
                        print "municipio: ",municipio_id
                    except:
                        pass

                if len(l[10])>0:
                    buscar = [("name","=",mayus(l[10]))]
                    try:
                        parroquia_id = sock.execute(dbname, uid, pwd, 'saim.parroquias', 'search', buscar)[0]
                        beneficiario.update({'parroquia': parroquia_id})
                        print "parroquia: ",parroquia_id
                    except:
                        pass
                    print "parroquia"

                print "A crear: "+str(beneficiario)
                partner_id = sock.execute(dbname, uid, pwd, 'saim.beneficiario', 'create', beneficiario)
                print "Creado: "+str(partner_id)


            except:
                error.write("\nError creando: "+str(l))

