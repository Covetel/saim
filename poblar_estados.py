# *-* coding=utf-8 *-*
import xmlrpclib
from geo import geo

username = 'admin' #the user
pwd = '123'      #the password of the user
dbname = 'Covetel'    #the database

# Get the uid
sock_common = xmlrpclib.ServerProxy ('http://localhost:8069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)
print uid

#replace localhost with the address of the server
sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
print sock

for estado in geo["República Bolivariana de Venezuela"].keys():
        data = {
	   'name': estado 
        }
        print "Creando: "+str(data)
        estado_id = sock.execute(dbname, uid, pwd, 'saim.estados', 'create', data)
        print "Creado: "+str(data)
        for municipio in geo["República Bolivariana de Venezuela"][estado].keys():
            data = {
                    'name': municipio, 
                    'padre': estado_id 
		}
            print "Creando: "+str(data)
            municipio_id = sock.execute(dbname, uid, pwd, 'saim.municipios', 'create', data)
            print "Creado: "+str(data),municipio_id
	    for parroquia in geo["República Bolivariana de Venezuela"][estado][municipio].keys():
		    data = {
                        'name': parroquia, 
                        'padre': municipio_id 
		    }
		    print "Creando: "+str(data)
		    parroquia_id = sock.execute(dbname, uid, pwd, 'saim.parroquias', 'create', data)
		    print "Creado: "+str(data)


