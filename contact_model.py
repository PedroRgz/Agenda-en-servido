from google.appengine.ext import ndb

#se heredan metodos de 'ndb'que es una libreria para
#guardar objetos a manera de base de datos
class Contact(ndb.Model):
    name = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()
