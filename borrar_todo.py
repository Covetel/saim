# *-* coding=utf-8 *-* 
import traceback
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

source_table = open("madres.csv")
bandera = False 

errores = open("errores_madres.log","a+")

buscar = [("name","=","Madres del Barrio")]
mision_id = sock.execute(dbname, uid, pwd, 'saim.mision', 'search', buscar)

if len(mision_id)==0:
    mision = {
       'name': 'Madres del Barrio',
    }
    mision_id= sock.execute(dbname, uid, pwd, 'saim.mision', 'create', mision)


beneficiarios = sock.execute(dbname, uid, pwd, 'saim.beneficiario', 'search',[] )
print beneficiarios
for each in beneficiarios:
  try:
    result = sock.execute(dbname, uid, pwd, 'saim.beneficiario', 'unlink',each)
  except:
    print "Problema con id:",each 


