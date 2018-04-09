from flask import Flask
from flask import request, json, jsonify
from flask import request, url_for
from flask_restful import Resource, Api
from flask import abort
from flaskext.mysql import MySQL
import time

app = Flask(__name__)
api = Api(app)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'ids_admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Idspass123#'
app.config['MYSQL_DATABASE_DB'] = 'ids_database'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

#@app.route("/test123")

def check_user(xapikey):
     user_sql_result = 'test'
     api_sql_result = 'test'
     final_sql_result = 'test'
     conn = mysql.connect()
     cursor = conn.cursor()
     cursor.callproc('spCheckUser',(xapikey,))
     result_sql = cursor.fetchall()
     user_sql_result = result_sql[0]
     #
     cursor.callproc('spCheckUserKey',(user_sql_result,))
     result_sql = cursor.fetchall()
     api_sql_result = result_sql[0]
     #
     final_sql_result=user_sql_result+api_sql_result
     #
     conn.commit()
     if (final_sql_result[0] == 'ERROR!!!' or final_sql_result[1] == 'ERROR!!!'):
         return 0
     else:
         return final_sql_result[0]

def succes_login(result_user,xauth,context):
     conn = mysql.connect()
     cursor = conn.cursor()
     now = time.strftime('%Y-%m-%d %H:%M:%S')
     cursor.callproc('spRegisterAuditTable',(result_user,'succes',now,xauth,'200',context))
     result_sql = cursor.fetchall()
     conn.commit()

def fail_login(xauth,context):
     conn = mysql.connect()
     cursor = conn.cursor()
     now = time.strftime('%Y-%m-%d %H:%M:%S')
     cursor.callproc('spRegisterAuditTable',('anonim','failed',now,xauth,'401',context))
     result_sql = cursor.fetchall()
     conn.commit()

class LastModule(Resource):
      def get(self):
           context = '/LastModule'
           Xa = request.headers.get('X-Api-Key')
           result_user=check_user(Xa)
           #
           if result_user == 0:
               fail_login(Xa,context)
               return abort(401)
           else:
               succes_login(result_user,Xa,context)
               #
               conn = mysql.connect()
               cursor = conn.cursor()
               now = time.strftime('%Y-%m-%d %H:%M:%S')
               cursor.callproc('spCheckULastModule')
               result_sql = cursor.fetchall()
               conn.commit()
               #
               return jsonify(last_module_id = result_sql[0])
               #return 'last_module_id = ' +  str(tuple(result_sql[0]))

class test(Resource):
      def get(self):
           context = '/test123'
           Xa = request.headers.get('X-Api-Key')
           result_user=check_user(Xa)
           if result_user == 0:
               fail_login(Xa,context)
               return abort(401)
           else:
               succes_login(result_user,Xa,context)
               return jsonify("Hello Catalin!")
      def post(self):
           if request.headers.get('X-Api-Key') == '47b9c056-af67-406d-b690-a2840de63779':
               try:
                  #parse the argument
                   parser = reqparse.RequestParser()    #create a parser
                   parser.add_argument('module_id', type=str, required=True,  help='ID of the module. Should be unique!')
                   args = parser.parse_args()
                   _moduleID = args['module_id']
                   return {'Module ID': args['module_id']}
               except Exception as e:
                     return {'error': str(e)}
           else:
               return abort(401)

api.add_resource(test, '/test123')
api.add_resource(LastModule, '/LastModule')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
