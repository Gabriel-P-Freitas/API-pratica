from flask import Flask, request, Response
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

db = SQLAlchemy()

api = Flask(__name__)
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.sqlite"

class Phone(db.Model):
     __tablename__ = "phones"
     
     name = Column(String(20), primary_key=True)
     ram_memory = Column(Integer)
     storage = Column(Integer)
     chipset = Column(String(20))
     battery = Column(Integer)
     
     def __init__(self, name: str, ram_memory: int, storage: int, chipset: str, battery: int):
          self.name = name
          self.ram_memory = ram_memory
          self.storage = storage
          self.chipset = chipset
          self.battery = battery

db.init_app(api)
migrate = Migrate(api, db)

@api.route("/phones", methods=['GET', 'POST', 'PATCH', 'DELETE'])
def phones():
     if request.method == "GET":
          def dictionary_to_json(phones):
               telefones = {}
               for phone in phones:
                    telefones[phone.name] = {}
                    telefones[phone.name]['ram_memory'] = phone.ram_memory
                    telefones[phone.name]['storage'] = phone.storage
                    telefones[phone.name]['chipset'] = phone.chipset
                    telefones[phone.name]['battery'] = phone.battery
               return telefones
          try:
               phone = dictionary_to_json(Phone.query.filter(Phone.name == request.json['name']).all())
               return Response(json.dumps(phone), 200)
          except:
               phones = dictionary_to_json(Phone.query.all())
               return Response(json.dumps(phones), 200)
     
     elif request.method == "POST":
          db.session.add(Phone(request.json['name'], request.json['ram_memory'], request.json['storage'], request.json['chipset'], request.json['battery']))
          db.session.commit()
          return Response("Telefone criado com sucesso!", 201)

     elif request.method == "PATCH":
          telefone = Phone.query.filter(Phone.name == request.json['name']).first()
          if(telefone != None):
               telefone.ram_memory = request.json['ram_memory']
               telefone.storage = request.json['storage']
               telefone.battery = request.json['battery']
               db.session.add(telefone)
               db.session.commit()
               return Response("Telefone "+telefone.name+" teve seus atributos modificados com sucesso!", 200)
          return Response("O telefone especificado não existe na base de dados.", 404)
     
     elif request.method == "DELETE":
          telefone = Phone.query.filter(Phone.name == request.json['name']).first()
          if(telefone != None):
               nome_telefone = telefone.name
               db.session.delete(telefone)
               db.session.commit()
               return Response("O telefone "+nome_telefone+" foi deletado com sucesso!", 200)
          return Response("O telefone especificado não existe na base de dados.", 404)

api.run("0.0.0.0", debug=True)
