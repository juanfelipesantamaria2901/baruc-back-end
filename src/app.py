from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson import ObjectId

# Instancias necesarias para funcionamiento
app = Flask(__name__)
app.config['MONGO_URI']='mongodb+srv://root:root@cluster0.m9zp4.mongodb.net/Matricula?retryWrites=true&w=majority'
mongo = PyMongo(app)

#Evitamos cortos con otro servidor 
CORS(app)

#Database
db = mongo.db.jovenes
pb = mongo.db.padres
md = mongo.db.madres
ad = mongo.db.acudientes


#Rutas empleadas para las peticiones 

# Creacion de objetos en la coleccion jovenes
@app.route('/jovenes', methods=['POST'])
def createJoven():
    id = db.insert(
  {
   'Nombre': request.json['Nombre'],
   'Apellido': request.json['Apellido'],
    'Sangre': request.json['Sangre'],
    'RH':request.json['RH'],
    'Sexo':request.json['Sexo'],
    'Hermanos':request.json['Hermanos'],
    'Asma':request.json['Asma'],
    'Identificacion': request.json['Identificacion'],
    'Email': request.json['Email'],
    'Direccion': request.json['Direccion'],
    'NumDoc': request.json['NumDoc'],
    'FechaNacimiento': request.json['FechaNacimiento'],
    'Cel': request.json['Cel'],
    'LugDoc': request.json['LugDoc'],
    'CityNa': request.json['CityNa'],
    'CityRE': request.json['CityRE'],
    'Tel': request.json['Tel'],
    'Altura': request.json['Altura'],
    'Eps': request.json['Eps'],
    'Alergias': request.json['Alergias'],
    'Lesiones': request.json['Lesiones'],
    'Responsable_contrato': request.json['Responsable_contrato'],
    'Peso': request.json['Peso'],
    'Prepagada': request.json['Prepagada'],
    'Medicamentos': request.json['Medicamentos'],
    'Enfermedades': request.json['Enfermedades'],
    'Talla': request.json['Talla'],
    'Intervensiones_quirurgicas': request.json['Intervensiones_quirurgicas'],
    'Medicamentos_quirujicos': request.json['Medicamentos_quirujicos'],
    'Recomendaciones': request.json['Recomendaciones']
    }
      ) 
    return jsonify(str(ObjectId(id)))

# Consulta de objetos almacenados en la coleccion jovenes
@app.route('/jovenes', methods=['GET'])
def getJovenes():
    jovenes = []
    for doc in db.find():
          jovenes.append({
             '_id': str(ObjectId(doc['_id'])),
             'Nombre': doc['Nombre'],
             'Apellido': doc['Apellido'],
             'Sangre': doc['Sangre'],
             'RH':doc['RH'],
             'Sexo':doc['Sexo'],
             'Hermanos':doc['Hermanos'],
             'Asma':doc['Asma'],
             'Identificacion': doc['Identificacion'],
             'Email': doc['Email'],
             'Direccion': doc['Direccion'],
             'NumDoc': doc['NumDoc'],
             'FechaNacimiento': doc['FechaNacimiento'],
             'Cel': doc['Cel'],
             'LugDoc': doc['LugDoc'],
             'CityNa': doc['CityNa'],
             'CityRE': doc['CityRE'],
             'Tel': doc['Tel'],
             'Altura': doc['Altura'],
             'Eps': doc['Eps'],
             'Alergias': doc['Alergias'],
             'Lesiones': doc['Lesiones'],
             'Responsable_contrato': doc['Responsable_contrato'],
             'Peso': doc['Peso'],
             'Prepagada': doc['Prepagada'],
             'Medicamentos': doc['Medicamentos'],
             'Enfermedades': doc['Enfermedades'],
             'Talla': doc['Talla'],
             'Intervensiones_quirurgicas': doc['Intervensiones_quirurgicas'],
             'Medicamentos_quirujicos': doc['Medicamentos_quirujicos'],
             'Recomendaciones': doc['Recomendaciones']
        }) 
    return jsonify(jovenes)
        
# Creacion de objetos en la coleccion padres
@app.route('/padres', methods=['POST'])
def CreatePadre():
     id = pb.insert({
         'Nombre_Padre' : request.json['Nombre_Padre'],
         'Apellido_Padre' : request.json['Apellido_Padre'],
         'Email_Padre': request.json['Email_Padre'],
         'Direccion_Padre' : request.json['Direccion_Padre'],
         'Indentificacion_Padre' : request.json['Indentificacion_Padre'],
         'NumDoc_Padre': request.json['NumDoc_Padre'],
         'FechaNacimiento_Padre' : request.json['FechaNacimiento_Padre'],
         'Cel_Padre' : request.json['Cel_Padre'],
         'LugDoc_Padre' : request.json['LugDoc_Padre'],
         'CityNa_Padre' :request.json['CityNa_Padre'],
         'CityRE_Padre' : request.json['CityRE_Padre'],
         'Tel_Padre' :request.json['Tel_Padre'],
         'Ocupacion': request.json['Ocupacion'],
         'Tel_Oficina' : request.json['Tel_Oficina'],
         'Cargo' : request.json['Cargo']
     })
     return jsonify(str(ObjectId(id)))


# Creacion de objetos en la coleccion madres
@app.route('/madres', methods=['POST'])
def CreateMadres():
     id = md.insert({
    'Nombre_Madre': request.json['Nombre_Madre'],
    'Apellido_Madre': request.json['Apellido_Madre'],
    'Email_Madre' : request.json['Email_Madre'],
    'Direccion_Madre' : request.json['Direccion_Madre'],
    'Indentificacion_Madre' : request.json['Indentificacion_Madre'],
    'NumDoc_Madre' : request.json['NumDoc_Madre'],
    'FechaNacimiento_Madre' : request.json['FechaNacimiento_Madre'],
    'Cel_Madre' : request.json['Cel_Madre'],
    'LugDoc_Madre' : request.json['LugDoc_Madre'],
    'CityNa_Madre' : request.json['CityNa_Madre'],
    'CityRE_Madre' : request.json['CityRE_Madre'],
    'Tel_Madre' : request.json['Tel_Madre'],
    'Ocupacion_Madre' : request.json['Ocupacion_Madre'],
    'TelOdiciona_Madre' : request.json['TelOdiciona_Madre'],
    'Cargo_Madre': request.json['Cargo_Madre']
     })
     return  jsonify(str(ObjectId(id))) 



# Creacion de objetos en la coleccion Acudientes
@app.route('/acudientes', methods=['POST'])
def CreateAcudiente():
     id = ad.insert({
         'Nombre_Acudiente' : request.json['Nombre_Padre'],
         'Apellido_Acudiente' : request.json['Apellido_Padre'],
         'Email_Acudiente': request.json['Email_Padre'],
         'Direccion_Acudiente' : request.json['Direccion_Padre'],
         'Indentificacion_Acudiente' : request.json['Indentificacion_Padre'],
         'NumDoc_Acudiente': request.json['NumDoc_Padre'],
         'FechaNacimiento_Acudiente' : request.json['FechaNacimiento_Padre'],
         'Cel_Acudiente' : request.json['Cel_Padre'],
         'LugDoc_Acudiente' : request.json['LugDoc_Padre'],
         'CityNa_Acudiente' :request.json['CityNa_Padre'],
         'CityRE_Acudiente' : request.json['CityRE_Padre'],
         'Tel_Acudiente' :request.json['Tel_Padre'],
         'Ocupacion': request.json['Ocupacion'],
         'Tel_Oficina' : request.json['Tel_Oficina'],
         'Cargo' : request.json['Cargo']
     })
     return jsonify(str(ObjectId(id)))


# Funcion para actulaizar 
@app.route('/jovenes', methods=['PUT'])
def updateJoven():
    return 'received'

# Recargar servidor 
if __name__ == "__main__":
   app.run(debug=True)
