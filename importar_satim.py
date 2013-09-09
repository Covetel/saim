# *-* coding=utf-8 *-* 
import xmlrpclib

username = 'admin' #the user
pwd = '123'      #the password of the user
dbname = 'SAIM'    #the database
#pwd = '123321...'      #the password of the user
#dbname = 'SAIM'    #the database

# Get the uid
sock_common = xmlrpclib.ServerProxy ('http://localhost:8069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)
print uid

#replace localhost with the address of the server
sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
print sock

def mayus(cadena):
    return " ".join([each.capitalize() for each in cadena.split(" ")])

error = open("errores_satim.log","a+")

source_table = open("satim.csv")

buscar = [("name","=","Satim")]
mision_id = sock.execute(dbname, uid, pwd, 'saim.mision', 'search', buscar)

if len(mision_id)==0:
    mision = {
       'name': 'Satim',
    }
    mision_id= sock.execute(dbname, uid, pwd, 'saim.mision', 'create', mision) 

for line in source_table.readlines()[5:]:
    #cedula;nombres;apellidos;genero;nacionalidad;Estado;ayuda
        """
        l[0] #Cedula
        l[1] #Nombres
        l[2] #Apellidos
        l[3] #genero (f,m)
        l[4] #nacionalidad (v,e)
        l[5] #estado
        l[6] #ingreso mensual familiar

        """

        try:
        #if True:

            l = line.split(";")
            print "Procesando: ",l
            
            #fecha_original = l[4].split("/")
            #fecha_nacimiento = fecha_original[1]+"/"+fecha_original[0]+"/"+fecha_original[2]

            print "diccionario beneficiario, creado"
            beneficiario = {
               'numero_identidad': "V-"+l[0],
               'nombres': mayus(l[1]),
               'apellidos': mayus(l[2]),
               'sexo': l[3],
               'mision_id': mision_id[0],
            }

            print "diccionario beneficiario, creado"

            try:
                if len(l[6])>0:
                    beneficiario.update({'ayuda':l[6]})
                    print "Ingresos, definidos"
            except:
                pass

            try:
                if cmp(l[7],'v')==0:
                    beneficiario.update({'nacionalidad':'venezolano'})
                if cmp(l[7],'e')==0:
                    beneficiario.update({'nacionalidad':'extranjero'})
            except:
                print "Error con nacionalidad"
                pass
            print "nacionalidad"

            buscar = [("name","=",mayus(l[5]))]
            try:
                estado_id = sock.execute(dbname, uid, pwd, 'saim.estados', 'search', buscar)[0]
                beneficiario.update({'estado': estado_id})
                print "estado: ",estado_id
            except:
                pass 

            print "A crear: "+str(beneficiario)
            partner_id = sock.execute(dbname, uid, pwd, 'saim.beneficiario', 'create', beneficiario)
            print "Creado: "+str(partner_id)


        except:
            error.write("Error creando: "+str(l))

