import xmlrpclib

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

source_table = open("origen.csv")
for in_each_line in source_table.readlines()[1:]:
        each_line = in_each_line.split(";")
        beneficiario = {
	   'nombres': each_line[4]+" "+each_line[5],
	   'apellidos': each_line[2]+" "+each_line[3],
           'numero_identidad': each_line[0]+"-"+each_line[1]
        }

        partner_id = sock.execute(dbname, uid, pwd, 'saim.beneficiario', 'create', beneficiario)
        print "Creado: "+str(beneficiario)

