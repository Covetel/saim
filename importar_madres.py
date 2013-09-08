# *-* coding=utf-8 *-* 
import xmlrpclib

username = 'admin' #the user
#pwd = '123'      #the password of the user
#dbname = 'Covetel7'    #the database
pwd = '123'      #the password of the user
dbname = 'SAIM'    #the database

# Get the uid
sock_common = xmlrpclib.ServerProxy ('http://localhost:8069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)
print uid

#replace localhost with the address of the server
sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
print sock

def mayus(cadena):
    return " ".join([each.capitalize() for each in cadena.split(" ")])

source_table = open("madres.csv")
bandera = True 

errores = open("errores_madres","a+")

buscar = [("name","=","Madres del Barrio")]
mision_id = sock.execute(dbname, uid, pwd, 'saim.mision', 'search', buscar)

if len(mision_id)==0:
    mision = {
       'name': 'Madres del Barrio',
    }
    mision_id= sock.execute(dbname, uid, pwd, 'saim.mision', 'create', mision)

for line in source_table.readlines()[5:]:
        """
        l[1] #Cedula
        l[2] #Nombres
        l[3] #Apellidos
        l[5] #Sexo "f"
        l[8] #Estado
        l[9] #Municipio
        l[10] #Parroquia
        l[12] #Dirección
        """
        l = line.split(",")
        print "Procesando: ",l

        try:
            if numero_identidad.find("6730055")>0:
                bandera = True
        except:
            pass

        try:

            beneficiario = {
               'numero_identidad': "V-"+l[1],
               'nombres': mayus(l[2]),
               'apellidos': mayus(l[3]),
               'sexo': l[5],
               'direccion_habitacion': l[12],
               'mision_id': mision_id[0]
            }


            if bandera:
                buscar = [("name","=",mayus(l[8]))]
                try:
                    estado_id = sock.execute(dbname, uid, pwd, 'saim.estados', 'search', buscar)[0]
                    beneficiario.update({'estado': estado_id})
                    print "estado: ",estado_id
                except:
                    pass 

                buscar = [("name","=",mayus(l[9]))]
                try: 
                    municipio_id = sock.execute(dbname, uid, pwd, 'saim.municipios', 'search', buscar)[0]
                    beneficiario.update({'municipio': municipio_id})
                    print "municipio: ",municipio_id
                except:
                    pass

                buscar = [("name","=",mayus(l[10]))]
                try:
                    parroquia_id = sock.execute(dbname, uid, pwd, 'saim.parroquias', 'search', buscar)[0]
                    beneficiario.update({'parroquia': parroquia_id})
                    print "parroquia: ",parroquia_id
                except:
                    pass

                partner_id = sock.execute(dbname, uid, pwd, 'saim.beneficiario', 'create', beneficiario)
                print "Creado: "+str(beneficiario)
                print "ID CREADO:",partner_id

        except:
            print  "Problema creando:"+str(beneficiario)
            errores.write("Problema creando:"+str(beneficiario))

