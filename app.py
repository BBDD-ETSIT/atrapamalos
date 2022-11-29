from flask import Flask, render_template,request,redirect,url_for
from flask_mongoengine import MongoEngine
from vigenere import encrypt, decrypt, random_key

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost/twitter'
}

db = MongoEngine()
db.init_app(app)

cipher_key:str = "keyword"

#No hago from model import Todo que da referencia circular
import model

@app.route("/")
def index ():
	#variable "tweets" tiene que filtrar los mensajes de un username, campo username dentro del subdocumento user
	#IMPORTANTE: recuerda escribir el username con la primera letra mayúscula
	#CAMBIAR en la siguiente línea "REEMPLAZAR_POR_QUERY" POR LA QUERY del ODM ADECUADA PARA GUARDAR EN LA VARIABLE "tweets" LOS MENSAJES DEL USUARIO
	tweets = "REEMPLAZAR_POR_QUERY"
	if len(tweets)!=34:
		print(f"LA VARIABLE TWEETS NO ES CORRECTA, COMPRUEBE LA QUERY DEL ODM")
	else:
		print(f"LA VARIABLE TWEETS CONTIENE {len(tweets)} MENSAJES. LOS PROCESAMOS.")
	return render_template('index.html',tweets=tweets)

@app.route("/process",methods=['POST'])
def process ():
	print("El SERVIDOR RECIBE UNA LLAMADA A PROCESAR LOS MENSAJES RECUPERADOS")
	print("EL SERVIDOR RECIBE COMO USERNAME: " + request.values.get("username"))
	code=""
	if encrypt(request.values.get("username"), cipher_key) == 'wq7DmsOOw5rDj8Odw5TDl8Oa':
		print("EL USERNAME ES CORRECTO Y TODO ESTÁ OK. PROCEDEMOS A PROCESAR CON IA")
		code = decrypt('wrjDjMOdw5TDmsKLwrfDmsObw5DDpcKLwrvDoMOXw5TDj8Oa', cipher_key)
	return render_template('code.html', code=code)


if __name__ == "__main__":
	env = 'development'
	port = 8001
	app.run(host='0.0.0.0', port=port, debug=True)
