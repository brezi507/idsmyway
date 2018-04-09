#### first python api

import sys
import os
import datetime
import logging
import time
from datetime import datetime
from flask import Flask
from flask import *
from flask_restful import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL

app = Flask(__name__)
api = Api(app)

mysql = MySQL()

# MySQL configurations
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'parola123'
#app.config['MYSQL_DATABASE_DB'] = 'ids_database'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'

#mysql.init_app(app)
#conn = mysql.connect()
#cursor = conn.cursor()

class CreateModule(Resource):
      def post(self):
          try:
             #parse the argument
             parser = reqparse.RequestParser()    #create a parser
             parser.add_argument('module_id', type=str, required=True,  help='ID of the module. Should be unique!')
             parser.add_argument('module_name', type=str, required=True, help='Name of the module.')
             parser.add_argument('owner', type=str, required=True, help='Owner of the module.')
             parser.add_argument('deployed', type=datetime, required=True, help='Date of deployment.')
             parser.add_argument('started', type=datetime, help='Date of starting the module.')
             parser.add_argument('status', type=str, required=True, help='Name of the module.')
             parser.add_argument('details', type=str, help='Details about the module.')
             
             args = parser.parse_args()

             _moduleID = args['module_id']
             _moduleName = args['module_name']
             _moduleOwner = args['owner']
             _moduleDeployed = args['deployed']
             _moduleStarted = args['started']
             _moduleStatus = args['status']
             _moduleDetails = args['details']

             return {'Module ID': args['module_id'], 'Module Name': args['module_name'], 'Owner': args['owner'], 'Date of deployement': args['deployed'], 'Started at': args['started'], 'Status': args['status'], 'Details': args['details']}
             #return {'Module ID': args['module_id'], 'Module Name': args['module_name'], 'Owner': args['owner'], 'Status': args['status'], 'Details': args['details']}
          except Exception as e:
             return {'error': str(e)}
      
      #return {'status':'succes'}
      def get(self):
          return {'status':'succes'}

api.add_resource(CreateModule, '/CreateModule')

if __name__ == '__main__':
     logging.basicConfig(filename='access.log',level=logging.CRITICAL)
     app.run(host='0.0.0.0')
