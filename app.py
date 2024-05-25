from flask import Flask, render_template, request, jsonify, make_response, redirect, url_for, session, abort

from decimal import Decimal
from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
import google.auth.transport.requests
from pip._vendor import cachecontrol
import requests
from flask_paginate import Pagination, get_page_args
import json

from flask_sqlalchemy import SQLAlchemy
import datetime
import os
import pathlib
from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from werkzeug.security import check_password_hash
from flask_session import Session

import mysql.connector

db_config = {
    'user': 'uxo2ihlb0xdfqqsl',
    'password': 'hxrJaC3zfpXk8yVJ9iAv',
    'host': 'b6l5dugohgvzb9gw6u4o-mysql.services.clever-cloud.com',
    'database': 'b6l5dugohgvzb9gw6u4o',
}

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://admin:upt2023@bdtranferapp.ovcij6h.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

    
client = MongoClient("mongodb+srv://admin:upt2023@bdtranferapp.ovcij6h.mongodb.net/?retryWrites=true&w=majority")

# Selecciona la base de datos
db = client.bd_Transf  # Cambia 'bd_Transf' con el nombre de tu base de datos

# Accede a la colección de usuarios
usuarios = db.usuarios
documentos = db.documentos



# Envía un ping para confirmar la conexión exitosa
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://alxcript_da_use:da*use10@mysql-alxcript.alwaysdata.net/alxcript_depresion_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuración de la aplicación
app.debug = True

# Configura Flask-Session para almacenar sesiones en la subcarpeta 'session_data' de AppTransf.
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = 'AppTransf/session_data'  # Ruta relativa a la carpeta 'AppTransf'.
Session(app)






#Authentication

app.secret_key = "depressionapp"
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
GOOGLE_CLIENT_ID = "871624759111-t7pa90fse2ahr5dg2rrc5hh576rc91rh.apps.googleusercontent.com"

client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file = client_secrets_file, 
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="https://5000-alxcript-depressionapp-1yj4bhu0xju.ws-us101.gitpod.io/callback"
    )


# Configura la carpeta de carga
import os
UPLOAD_FOLDER = os.path.join(app.root_path,"static", "archivos_analisis")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER





@app.route('/api/usuarios2', methods=['POST'])
def registrar_usuario2():
    data = request.get_json()

    if data:
        usuario_id = data.get("_id")
        usuario_data = {
            "nombreUsuario": data.get("nombreUsuario"),
            "nombre": data.get("nombre"),
            "apellido": data.get("apellido"),
            "dni": data.get("dni"),
            "correoElectronico": data.get("correoElectronico"),
            "contrasenaHash": data.get("contrasenaHash"),
            "fechaRegistro": data.get("fechaRegistro"),
            "roles": data.get("roles"),
            "activo": data.get("activo"),
        }

        if usuario_id:
            # Si existe _id, actualizar el documento existente
            result = usuarios.update_one(
                {"_id": ObjectId(usuario_id)},
                {"$set": usuario_data},
                upsert=True
            )
            mensaje = "Usuario actualizado exitosamente" if result.modified_count > 0 else "Usuario creado exitosamente"
        else:
            # Si no existe _id, crear un nuevo documento
            result = usuarios.insert_one(usuario_data)
            mensaje = "Usuario registrado exitosamente"

        # Obtener todos los usuarios actuales después de la operación
        usuarios_actuales = list(usuarios.find({}))
        usuarios_json = json.loads(json_util.dumps(usuarios_actuales))

        return jsonify({"mensaje": mensaje, "usuarios": usuarios_json}), 201

    return jsonify({"mensaje": "Error al registrar usuario"}), 400


#Importar datos 

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Guarda el archivo en la carpeta UPLOAD_FOLDER
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Guarda filename en la sesión
        session['uploaded_filename'] = filename

        # Intenta cargar el archivo CSV o Excel
        try:
            if filename.endswith('.csv'):
                df = pd.read_csv(filename)
            elif filename.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(filename)
            else:
                return jsonify({'error': 'Formato de archivo no admitido'})
        except Exception as e:
            return jsonify({'error': 'Error al cargar el archivo'})

        # Inserta los datos en MongoDB si es un DataFrame válido
        if not df.empty:
            # Conecta con la base de datos MongoDB Atlas
            
            # Inserta los datos en la colección 'documentos'
            documentos.insert_many(df.to_dict(orient='records'))

        # Devuelve los datos procesados en formato JSON
        data_json = df.to_json(orient='split')
        return jsonify({'data': data_json})

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401) # Authorization required
        else:
            return function()
    # Renaming the function name:
    wrapper.__name__ = function.__name__
    return wrapper


@app.errorhandler(401)
def custom_401(error):
    return render_template("exceptions/401.html")


@app.route("/authenticate-google")
def authenticateGoogle():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

@app.route("/login-comun", methods=['POST'])
def login_comun():
    dni = request.form.get("dni")
    password = request.form.get("password")

    # Verifica si los datos no están vacíos
    if not dni or not password:
        print("Datos de entrada incompletos")
        return "Datos de entrada incompletos", 400  # Devuelve el mensaje de error con código de estado 400

    user = usuarios.find_one({"dni": dni})

    if user:
        if user["contrasenaHash"] == password:  # Verifica si la contraseña es correcta
            session["user_id"] = str(user["_id"])
            print("Inicio de sesión exitoso")  # Imprime el mensaje de éxito
            return redirect(url_for('admin_home'))

        else:
            print("Contraseña incorrecta")  # Imprime el mensaje de contraseña incorrecta
            return "Contraseña incorrecta", 400  # Devuelve el mensaje de error con código de estado 400
    else:
        print("Usuario no encontrado")  # Imprime el mensaje de usuario no encontrado
        return "Usuario no encontrado", 404  # Devuelve el mensaje de error con código de estado 404




@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)
    if not session["state"] == request.args["state"]:
        abort(500) # State does not match
    
    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_token(
        id_token = credentials.id_token,
        request = token_request,
        audience=GOOGLE_CLIENT_ID
        )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    session["email"] = id_info.get("email")
    session["picture"] = id_info.get("picture")

    if(userNotExist(id_info.get("sub"))):
        registrarUsuarioNuevo(id_info.get("name"), 'usuario_google', id_info.get("at_hash"), id_info.get("picture"), id_info.get("sub"))

    usuarioId_DiagnosticoId = getUsuarioIdAndDiagnosticoIdByGoogleId(id_info.get("sub"))
    session["usuario_actual_id"] = usuarioId_DiagnosticoId[0]['usuarioId']
    session["id_diagnostico"] = usuarioId_DiagnosticoId[0]['diagnosticoId']
    session["chat_activado"] = isChatActivado(session["id_diagnostico"])

    return redirect("/usuario")

def isChatActivado(id_diagnostico):

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM DETALLES_DIAGNOSTICO WHERE id_diagnostico = %s", (id_diagnostico,))
    modoDelaUltimaEtapa = "noregistrado"
    listaEtapasDelUsuario = cursor.fetchall()
    if(len(listaEtapasDelUsuario) > 0):
        modoDelaUltimaEtapa = listaEtapasDelUsuario.pop()[3].lower()
    print("modoDelaUltimaEtapa:", modoDelaUltimaEtapa)
    cursor.close()
    connection.close()

    isChatActivado = "no"
    if(modoDelaUltimaEtapa in ['moderado', 'alto', 'muy alto']):
        isChatActivado = "yes"
    
    return isChatActivado

def userNotExist(google_id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM USUARIO WHERE id_google = %s", (google_id,))
    usuariosCoincidentes = cursor.fetchall()

    cursor.close()
    connection.close()

    return len(usuariosCoincidentes) == 0

def registrarUsuarioNuevo(nombre, dni, contrasena, imagen, id_google):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    add_usuario = ("INSERT INTO USUARIO "
               "(nombre, dni, contrasena, imagen, id_google, estado, tipo) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")

    data_usuario = (nombre, dni, contrasena, imagen, id_google, 'Activo', 'Paciente')
    cursor.execute(add_usuario, data_usuario)
    usuarioRegistradoId = cursor.lastrowid


    add_diagnostico = ("INSERT INTO DIAGNOSTICO "
                "(id_usuario) "
                "VALUES (%s)")
    data_diagnostico = (usuarioRegistradoId,)

    cursor.execute(add_diagnostico, data_diagnostico)

    connection.commit()
    cursor.close()
    connection.close()

def getUsuarioIdAndDiagnosticoIdByGoogleId(id_google):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    query = ("SELECT USUARIO.id, DIAGNOSTICO.id FROM USUARIO INNER JOIN DIAGNOSTICO ON USUARIO.id = DIAGNOSTICO.id_usuario WHERE id_google = %s")
    cursor.execute(query, (id_google,))

    values = []
    for row in cursor:
        values.append({'usuarioId': row[0], 'diagnosticoId': row[1]})

    cursor.close()
    connection.close()

    return values

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/registro")
def registro():
    return render_template('registro.html')

@app.route("/protected_area")
@login_is_required
def protected_area():
    return "Protected page! hi " + session["name"] + " <a href='/logout'><button>Logout</button></a><p><img src='" + session["picture"] + "  ' /></p>"

#Administracion

@app.route("/")
def home():
    return render_template("login.html")





# IA UNIDAD2 - VERSION 1.0
'''
@app.route("/admin/ResultadosAnalisis")
def admin_ResultadosAnalisis():
    uploaded_filename = session.get('uploaded_filename')
    if uploaded_filename is not None:
        # Cargar los datos desde el archivo cargado y realizar el análisis

        # Carga tus datos de compras en un DataFrame de pandas
        data = pd.read_excel(uploaded_filename)

        # Aplicar codificación one-hot a las características categóricas (CATEGORIA y MARCA)
        encoder = OneHotEncoder(sparse=False, drop='first', handle_unknown='ignore')

        X_encoded = encoder.fit_transform(data[['CATEGORIA', 'MARCA']])

        X_numeric = data[['PRECIO_UNITARIO']].values
        X_final = np.hstack((X_encoded, X_numeric))

        media_precios_unitarios = data['PRECIO_UNITARIO'].mean()
        desviacion_estandar_precios_unitarios = data['PRECIO_UNITARIO'].std()
        umbral_superior = media_precios_unitarios + 2 * desviacion_estandar_precios_unitarios
        umbral_inferior = media_precios_unitarios - 2 * desviacion_estandar_precios_unitarios

        data['anomalia_etiqueta'] = [1 if precio_unitario > umbral_superior or precio_unitario < umbral_inferior else 0 for precio_unitario in data['PRECIO_UNITARIO']]

        X = X_final

        y = data['anomalia_etiqueta'].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LogisticRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        indices_anomalias = [i for i, anomalia in enumerate(y_pred) if anomalia == 1]

        anomalies = data.iloc[indices_anomalias]
        print("Filas consideradas anomalías:")
        print(anomalies)

        # Convertir el DataFrame 'data' a formato JSON
        data_json = data.to_json(orient='split')

        print(data_json)

        # Finalmente, pasar los datos JSON directamente a la plantilla HTML
        return render_template("admin/charts.html", filename=uploaded_filename, data_json=json.dumps(data_json), anomalies=anomalies)
    else:
        return jsonify({'error': 'No se ha cargado ningún archivo'})
'''




# IA UNIDAD2 - VERSION 2.0

def find_price_column(data):
    possible_price_columns = ["precio_unitario", "precio_unidad", "precio", "precio c/u"]

    for column in data.columns:
        if any(keyword in column.lower() for keyword in possible_price_columns):
            return column

    return None



'''
@app.route("/admin/ResultadosAnalisis")
def admin_ResultadosAnalisis():
    uploaded_filename = session.get('uploaded_filename')
    if uploaded_filename is not None:
        if uploaded_filename.endswith(('.csv', '.xls', '.xlsx')):
            data = pd.read_csv(uploaded_filename) if uploaded_filename.endswith('.csv') else pd.read_excel(uploaded_filename)
        else:
            return jsonify({'error': 'Formato de archivo no admitido. Cargue un archivo CSV o Excel.'})

        data.columns = [col.lower() for col in data.columns]  # Convertir a minúsculas
        categorias_column = next((col for col in data.columns if 'nombre' in col), None)
        marcas_column = next((col for col in data.columns if 'marca' in col), None)
        precio_unitario_column = find_price_column(data)

        if categorias_column and marcas_column and precio_unitario_column:
            encoder = OneHotEncoder(sparse=False, drop='first', handle_unknown='ignore')
            X_encoded = encoder.fit_transform(data[[categorias_column, marcas_column]])

            X_numeric = data[precio_unitario_column].values
            X_final = np.column_stack((X_encoded, X_numeric))

            # Calcula umbrales separados para cada categoría y marca
            unique_categories = data[categorias_column].unique()
            unique_brands = data[marcas_column].unique()
            
            thresholds = {}

            for category in unique_categories:
                for brand in unique_brands:
                    subset = data[(data[categorias_column] == category) & (data[marcas_column] == brand)]
                    mean = subset[precio_unitario_column].mean()
                    std = subset[precio_unitario_column].std()
                    upper_threshold = mean + 2 * std
                    lower_threshold = mean - 2 * std
                    thresholds[(category, brand)] = (upper_threshold, lower_threshold)

            data['anomalia_etiqueta'] = [1 if (row[precio_unitario_column] > thresholds[(row[categorias_column], row[marcas_column])][0] or row[precio_unitario_column] < thresholds[(row[categorias_column], row[marcas_column])][1]) else 0 for _, row in data.iterrows()]

            X = X_final
            y = data['anomalia_etiqueta'].values
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = LogisticRegression()
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)

            indices_anomalías = [i for i, anomalía in enumerate(y_pred) if anomalía == 1]

            anomalías = data.iloc[indices_anomalías]

            data.columns = [col.upper() if col != 'anomalia_etiqueta' else col for col in data.columns]  # Convertir a mayúsculas

            data_json = data.to_json(orient='split')

            return render_template("admin/charts.html", filename=uploaded_filename, data_json=json.dumps(data_json), anomalies=anomalías)
        else:
            return jsonify({'error': 'No se encontraron columnas relacionadas a CATEGORIA, MARCA y PRECIO'})
    else:
        return jsonify({'error': 'No se ha cargado ningún archivo'})
'''


from sklearn.ensemble import IsolationForest

'''

@app.route("/admin/ResultadosAnalisis")
def admin_ResultadosAnalisis():
    uploaded_filename = session.get('uploaded_filename')
    if uploaded_filename is not None:
        if uploaded_filename.endswith(('.csv', '.xls', '.xlsx')):
            data = pd.read_csv(uploaded_filename) if uploaded_filename.endswith('.csv') else pd.read_excel(uploaded_filename)
        else:
            return jsonify({'error': 'Formato de archivo no admitido. Cargue un archivo CSV o Excel.'})

        data.columns = [col.lower() for col in data.columns]  # Convertir a minúsculas
        categorias_column = next((col for col in data.columns if 'nombre' in col), None)
        marcas_column = next((col for col in data.columns if 'marca' in col), None)
        precio_unitario_column = find_price_column(data)

        if categorias_column and marcas_column and precio_unitario_column:
            encoder = OneHotEncoder(sparse=False, drop='first', handle_unknown='ignore')

            

            X_encoded = encoder.fit_transform(data[[categorias_column, marcas_column]])

            X_numeric = data[precio_unitario_column].values
            X_final = np.column_stack((X_encoded, X_numeric))

            # Calcula umbrales separados para cada categoría y marca
            unique_categories = data[categorias_column].unique()
            unique_brands = data[marcas_column].unique()
            
            thresholds = {}

            for category in unique_categories:
                for brand in unique_brands:
                    subset = data[(data[categorias_column] == category) & (data[marcas_column] == brand)]
                    mean = subset[precio_unitario_column].mean()
                    std = subset[precio_unitario_column].std()
                    upper_threshold = mean + 2 * std
                    lower_threshold = mean - 2 * std
                    thresholds[(category, brand)] = (upper_threshold, lower_threshold)

            data['anomalia_etiqueta'] = [1 if (row[precio_unitario_column] > thresholds[(row[categorias_column], row[marcas_column])][0] or row[precio_unitario_column] < thresholds[(row[categorias_column], row[marcas_column])][1]) else 0 for _, row in data.iterrows()]

            X = X_final
            y = data['anomalia_etiqueta'].values
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = IsolationForest(contamination=0.1, random_state=42)
            model.fit(X_train)

            y_pred = model.predict(X_test)

            indices_anomalías = [i for i, anomalía in enumerate(y_pred) if anomalía == 1]

            anomalías = data.iloc[indices_anomalías]

            data.columns = [col.upper() if col != 'anomalia_etiqueta' else col for col in data.columns]  # Convertir a mayúsculas

            data_json = data.to_json(orient='split')

            return render_template("admin/charts.html", filename=uploaded_filename, data_json=json.dumps(data_json), anomalies=anomalías)
        else:
            return jsonify({'error': 'No se encontraron columnas relacionadas a CATEGORIA, MARCA y PRECIO'})
    else:
        return jsonify({'error': 'No se ha cargado ningún archivo'})

'''










# IA UNIDAD3 - VERSION 3.0


def find_price_column(data):
    possible_price_columns = ["precio_unitario", "precio_unidad", "precio", "precio c/u"]

    for column in data.columns:
        if any(keyword in column.lower() for keyword in possible_price_columns):
            return column

    return None

def find_brand_column(data):
    possible_brand_columns = ["marca", "fabricante", "proveedor"]  # Agrega otras palabras clave según tus datos

    for column in data.columns:
        if any(keyword in column.lower() for keyword in possible_brand_columns):
            return column

    return None

def find_category_column(data):
    possible_category_columns = ["categoria", "tipo", "clase"]  # Agrega otras palabras clave según tus datos

    for column in data.columns:
        if any(keyword in column.lower() for keyword in possible_category_columns):
            return column

    return None
def find_name_column(data):
    possible_name_columns = ["nombre", "producto"]  # Agrega otras palabras clave según tus datos

    for column in data.columns:
        if any(keyword in column.lower() for keyword in possible_name_columns):
            return column

    return None

@app.route("/admin/ResultadosAnalisis")
def admin_ResultadosAnalisis():
    uploaded_filename = session.get('uploaded_filename')
    if uploaded_filename is not None:
        if uploaded_filename.endswith(('.csv', '.xls', '.xlsx')):
            data = pd.read_csv(uploaded_filename) if uploaded_filename.endswith('.csv') else pd.read_excel(uploaded_filename)
        else:
            return jsonify({'error': 'Formato de archivo no admitido. Cargue un archivo CSV o Excel.'})

        data.columns = [col.lower() for col in data.columns]  
        categorias_column = find_category_column(data)
        marcas_column = find_brand_column(data)
        precio_unitario_column = find_price_column(data)
        nombre_column = find_name_column(data)  

        if categorias_column and marcas_column and precio_unitario_column and nombre_column:
            encoder = OneHotEncoder(drop='first', handle_unknown='ignore')
            X_encoded = encoder.fit_transform(data[[categorias_column, marcas_column, nombre_column]])  

            X_numeric = data[precio_unitario_column].values
            X_final = np.column_stack((X_encoded.toarray(), X_numeric))

            unique_categories = data[categorias_column].unique()
            unique_brands = data[marcas_column].unique()
            unique_names = data[nombre_column].unique()
            
            thresholds = {}

            for category in unique_categories:
                for brand in unique_brands:
                    for name in unique_names:
                        subset = data[(data[categorias_column] == category) & (data[marcas_column] == brand) & (data[nombre_column] == name)]  
                        mean = subset[precio_unitario_column].mean()
                        std = subset[precio_unitario_column].std()
                        upper_threshold = mean + 2 * std
                        lower_threshold = mean - 2 * std
                        thresholds[(category, brand, name)] = (upper_threshold, lower_threshold)

            data['anomalia_etiqueta'] = [1 if (row[precio_unitario_column] > thresholds[(row[categorias_column], row[marcas_column], row[nombre_column])][0] or row[precio_unitario_column] < thresholds[(row[categorias_column], row[marcas_column], row[nombre_column])][1]) else 0 for _, row in data.iterrows()]

            X = X_final
            y = data['anomalia_etiqueta'].values
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = LogisticRegression()
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)

            indices_anomalías = [i for i, anomalía in enumerate(y_pred) if anomalía == 1]

            anomalías = data.iloc[indices_anomalías]

            data.columns = [col.upper() if col != 'anomalia_etiqueta' else col for col in data.columns]  

            data_json = data.to_json(orient='split')

            return render_template("admin/charts.html", filename=uploaded_filename, data_json=json.dumps(data_json), anomalies=anomalías)
        else:
            return jsonify({'error': 'No se encontraron columnas relacionadas a CATEGORIA, MARCA, NOMBRE y PRECIO'})
    else:
        return jsonify({'error': 'No se ha cargado ningún archivo'})



import joblib
from flask import Flask, render_template, redirect, url_for, request


model_filename = 'AppTransf/static/modelo/linear_regression_model.joblib'
encoder_filename = 'AppTransf/static/modelo/one_hot_encoder.joblib'
model = joblib.load(model_filename)
encoder = joblib.load(encoder_filename)

# Aquí está tu vista original
@app.route('/admin/destino', methods=['POST'])
def destino():
    print("Llegó a destino")
    data = request.get_json()
    

    # Accede a la fila seleccionada y al conjunto completo de datos
    selected_row = data.get('selectedRow', {})
    all_data = data.get('allData', {})

    # Almacena los datos en la sesión del usuario
    session['selected_row'] = selected_row
    session['all_data'] = all_data


    

    

    return "Datos almacenados en la sesión"





from datetime import datetime

@app.route('/admin/destino', methods=['GET'])  
def admin_destino():
    # Recupera los datos almacenados en la sesión
    selected_row = session.pop('selected_row', {})
    all_data = session.pop('all_data', {})

    marca_index = 13  # Ajusta el índice según la posición real de 'marca' en tu lista
    nombre_index = 12  # Ajusta el índice según la posición real de 'nombre' en tu lista
    fecha_compra_index = 7  # Ajusta el índice según la posición real de 'fecha_compra' en tu lista
    precio_unitario_index = 14  # Ajusta el índice según la posición real de 'precio_unitario' en tu lista

    # Obtén los valores directamente de selected_row
    marca = selected_row[marca_index] if len(selected_row) > marca_index else ''
    nombre = selected_row[nombre_index] if len(selected_row) > nombre_index else ''
    fecha_compra = selected_row[fecha_compra_index] if len(selected_row) > fecha_compra_index else ''

    # Obtén el mes de compra a partir de la fecha de compra
    fecha_compra_obj = datetime.strptime(fecha_compra, '%Y-%m-%d') if fecha_compra else None
    mes_compra = fecha_compra_obj.month if fecha_compra_obj else None

    # Convierte 'precio_unitario' a float
    precio_unitario = float(selected_row[precio_unitario_index]) if len(selected_row) > precio_unitario_index else 0.0

    # Codificar variables categóricas
    encoded_features = encoder.transform([[marca, nombre, mes_compra]])

    # Combinar características codificadas y precio unitario para realizar la predicción
    X = np.column_stack((encoded_features, precio_unitario))
    price_prediction = model.predict(X)

    # Tu lógica para renderizar la plantilla
    return render_template('admin/destino.html', selected_row=selected_row, all_data=all_data, prediction=price_prediction[0])



@app.route("/api/usuarios/editar", methods=["POST"])
def editar_usuario():
    data = request.get_json()

    if data:
        document_id = data.get("document_id")
        nuevos_datos = {
            "nombreUsuario": data.get("nombreUsuario"),
            "nombre": data.get("nombre"),
            "apellido": data.get("apellido"),
            "dni": data.get("dni"),
            "correoElectronico": data.get("correoElectronico"),
            "contrasenaHash": data.get("contrasenaHash"),
            "fechaRegistro": data.get("fechaRegistro"),
            "roles": data.get("roles"),
        }

        # Llama a la función de edición del documento que proporcioné antes
        editar_documento(document_id, nuevos_datos)

        return jsonify({"mensaje": "Usuario editado exitosamente"}), 200

    return jsonify({"mensaje": "Error al editar usuario"}), 400

    
from bson.objectid import ObjectId
@app.route("/api/usuarios2/eliminar/<string:document_id>", methods=["DELETE"])
def eliminar_usuario(document_id):
    try:
        # Convierte el string document_id en un ObjectId válido
        obj_id = ObjectId(document_id)
        
        # Elimina el documento con el ObjectId proporcionado
        result = usuarios.delete_one({"_id": obj_id})
        
        if result.deleted_count > 0:
            usuarios_actuales = list(usuarios.find({}))
            usuarios_json = json.loads(json_util.dumps(usuarios_actuales))
            return jsonify({"mensaje": "Usuario eliminado exitosamente", "usuarios": usuarios_json}), 201
        else:
            return jsonify({"mensaje": "Usuario no encontrado"}), 404
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 500



from bson import json_util
from flask import json

@app.route('/admin')
def admin_home():
    detalles_list = list(usuarios.find({}))  # Incluimos el campo _id
    detalles_list_json = json.dumps(detalles_list, default=json_util.default)
    return render_template('admin/index.html', detalles_list=detalles_list, detalles_list_json=detalles_list_json)


@app.route('/admin/resultado/<int:usuario_id>')
def resultado(usuario_id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Obtener los datos del paciente, el score final y la clasificación final de diagnóstico
    query_datos_paciente = """
        SELECT U.nombre, D.score_final, D.estado_final
        FROM USUARIO U
        JOIN DIAGNOSTICO D ON U.id = D.id_usuario
        WHERE U.id = %s
    """
    cursor.execute(query_datos_paciente, (usuario_id,))
    datos_paciente = cursor.fetchone()

    # Obtener los datos del diagnóstico y los detalles del diagnóstico
    query_diagnostico = """
        SELECT DD.id_etapa, E.tema, DD.score_etapa, DD.estado_etapa
        FROM DIAGNOSTICO D
        JOIN DETALLES_DIAGNOSTICO DD ON D.id = DD.id_diagnostico
        JOIN ETAPA E ON DD.id_etapa = E.id
        WHERE D.id_usuario = %s
        ORDER BY DD.id_etapa
    """
    cursor.execute(query_diagnostico, (usuario_id,))
    resultados = cursor.fetchall()

    # Cerrar la conexión a la base de datos
    cursor.close()
    connection.close()

    return render_template('admin/resultado.html', datos_paciente=datos_paciente, resultados=resultados)
@app.route('/admin/RegistroPacientes')
def admin_RegistroPacientes():
    return render_template('admin/forms.html')

@app.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():

 # Obtén los datos enviados desde el formulario
    nombre = request.form['nombres']
    apellido = request.form['apellidos']
    dni = request.form['dni']
    contrasena = request.form['contrasena']
    imagen = request.form['imagen']
    tipo="Paciente"
    estado="Activo"
    nombres=nombre+apellido

    # Realiza la inserción en la base de datos
    try:
        # Establece la conexión a la base de datos
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Inserta los datos en la tabla USUARIO
        query = "INSERT INTO USUARIO (nombre, dni, contrasena, imagen,tipo,estado) VALUES (%s,%s, %s, %s, %s, %s)"
        values = (nombres, dni, contrasena, imagen,tipo,estado)
        cursor.execute(query, values)
        
        # Guarda los cambios en la base de datos
        connection.commit()

        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        connection.close()

        # Devuelve una respuesta JSON para indicar el éxito del registro
        response = {'success': True, 'message': 'Registro exitoso'}
        return jsonify(response)

    except Exception as e:
        # En caso de error, devuelve una respuesta JSON con el mensaje de error
        response = {'success': False, 'message': str(e)}
        return jsonify(response)


@app.route('/admin/GestionarPacientes')
def admin_GestionarPacientes():
    # Establecer la conexión a la base de datos
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Ejecutar la consulta SQL
    query = "SELECT u.*, d.score_final, d.estado_final FROM USUARIO u JOIN DIAGNOSTICO d ON u.id = d.id_usuario WHERE u.tipo = 'Paciente'"
    cursor.execute(query)
    usuario_list = cursor.fetchall()

    # Cerrar el cursor y la conexión a la base de datos
    cursor.close()
    connection.close()
    return render_template('admin/tables.html', usuario_list=usuario_list)


@app.route("/usuario")
@login_is_required
def usuario():
    return render_template('usuario/etapa.html')

@app.route('/chat')
def chat():
    return render_template('usuario/chat.html')

@app.route('/etapa')
def etapa():

    id_usuario=int(session["usuario_actual_id"])

    prediction = request.args.get('prediction')
    porcentaje_cercania = request.args.get('porcentaje_cercania')
    score_final = request.args.get('score_final')
    
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    query_etapas_asignadas = "SELECT COALESCE((SELECT MAX(id_etapa) + 1 FROM DETALLES_DIAGNOSTICO WHERE id_diagnostico IN (SELECT id FROM DIAGNOSTICO WHERE id_usuario = %s)), 1) AS next_id_etapa;"
    
    cursor.execute(query_etapas_asignadas, (id_usuario,))
    etapas_asignadas = [row[0] for row in cursor.fetchall()]

    # Consultar todas las etapas en la tabla ETAPA
    query_etapas = "SELECT id, tema, imagen FROM ETAPA"
    cursor.execute(query_etapas)
    etapa_list = cursor.fetchall()
    completadas_count = int(etapas_asignadas[0])
    # Cerrar la conexión a la base de datos
    cursor.close()
    connection.close()

    return render_template('usuario/etapa.html', etapa_list=etapa_list, etapas_asignadas=etapas_asignadas, completadas_count=completadas_count,prediction=prediction, porcentaje_cercania=porcentaje_cercania, score_final=score_final)

@app.route('/quiz')
def quiz():
    return render_template('quiz/index.php')

@app.route('/etapa/<int:numero>')
def etapaQz(numero):
    # Realizar la consulta a la base de datos para obtener las preguntas de la etapa
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    query = "SELECT P.pregunta_descripcion, E.tema, P.id FROM PREGUNTA AS P INNER JOIN ETAPA AS E ON P.id_etapa = E.id WHERE E.id = %s"
    cursor.execute(query, (numero,))
    results = cursor.fetchall()

    # Obtener los IDs de las preguntas de la etapa 1
    preguntas_etapa_1_ids = [row[2] for row in results]

    # Obtener la estructura de calificación correspondiente a los IDs de las preguntas de la etapa 1
    estructura_calificacion = []
    for pregunta_id in preguntas_etapa_1_ids:
        cursor.execute("SELECT nombre, puntaje FROM ESTRUCTURA_CALIFICACION WHERE id_pregunta = %s", (pregunta_id,))
        calificaciones = cursor.fetchall()
        estructura_calificacion.extend(calificaciones)

    # Cerrar la conexión a la base de datos
    cursor.close()
    connection.close()

    return render_template('usuario/cuestionario.html', results=results, estructura_calificacion=estructura_calificacion, numero=numero)



@app.route('/submit', methods=['POST'])
def submit():
    # Obtener los valores de las respuestas del formulario
    numero = int(request.form.get('numero'))
    respuestas = []
    for i in range(1, 6):  # Reemplaza 5 por el número de preguntas que tengas
        respuesta = request.form.get(f'pregunta{i}')
        respuestas.append(int(respuesta))

    # Calcular el puntaje total
    score = sum(respuestas)

    # Guardar el puntaje en la base de datos
    id=int(session["id_diagnostico"])
    id_usuario = session["usuario_actual_id"]
    score = sum(respuestas)

    if score <= 7:
        clasificacion = "Muy bajo"
    elif score <= 11:
        clasificacion = "Bajo"
    elif score <= 15:
        clasificacion = "Moderado"
    elif score <= 19:
        clasificacion = "Alto"
    else:
        clasificacion = "Muy alto"

    
    # Guardar los detalles del diagnóstico en la base de datos
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    query = "INSERT INTO DETALLES_DIAGNOSTICO (id_diagnostico, id_etapa, score_etapa, estado_etapa) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id, numero, score, clasificacion))
    connection.commit()

    # Cerrar la conexión a la base de datos
    cursor.close()
    connection.close()


    if numero==10:
        

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Consulta para calcular el score_final
        query = """
            SELECT SUM(dd.score_etapa * e.ponderacion) AS score_final
            FROM DETALLES_DIAGNOSTICO dd
            INNER JOIN ETAPA e ON dd.id_etapa = e.id
            WHERE dd.id_diagnostico = %s
        """

        cursor.execute(query, (id,))
        score_final = cursor.fetchone()[0]

        if score_final >= 17:
            clasificacion_final = "Muy alto riesgo de depresión"
        elif score_final >= 13:
            clasificacion_final = "Alto riesgo de depresión"
        elif score_final >= 9:
            clasificacion_final = "Moderado riesgo de depresión"
        elif score_final >= 5:
            clasificacion_final = "Bajo riesgo de depresión"
        else:
            clasificacion_final = "Muy bajo riesgo de depresión"

        # Actualizar el score_final en la tabla DIAGNOSTICO
        update_query = "UPDATE DIAGNOSTICO SET score_final = %s, estado_final = %s WHERE id = %s AND id_usuario = %s"
        cursor.execute(update_query, (score_final, clasificacion_final, id, id_usuario))
        connection.commit()

        # Cerrar la conexión a la base de datos
        cursor.close()
        connection.close()
        csv_path = os.path.join(app.root_path, 'static', 'datos.csv')
        # Cargar los datos del archivo CSV
        df = pd.read_csv(csv_path, encoding='ISO-8859-1')

        # Dividir los datos en características (X) y etiquetas (y)
        X = df.drop('Score Final', axis=1)
        y = df['Score Final']

        # Dividir los datos en conjuntos de entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Crear un objeto de regresión lineal
        model = LinearRegression()

        # Entrenar el modelo con los datos de entrenamiento
        model.fit(X_train, y_train)

        # Conectar a la base de datos
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecutar la consulta SQL para obtener los datos del usuario
        query = """
        SELECT
        U.id AS id_usuario,
        D.score_final,
        DD.score_etapa AS etapa_1,
        DD2.score_etapa AS etapa_2,
        DD3.score_etapa AS etapa_3,
        DD4.score_etapa AS etapa_4,
        DD5.score_etapa AS etapa_5,
        DD6.score_etapa AS etapa_6,
        DD7.score_etapa AS etapa_7,
        DD8.score_etapa AS etapa_8,
        DD9.score_etapa AS etapa_9,
        DD10.score_etapa AS etapa_10
        FROM
        USUARIO U
        JOIN DIAGNOSTICO D ON U.id = D.id_usuario
        LEFT JOIN DETALLES_DIAGNOSTICO DD ON D.id = DD.id_diagnostico AND DD.id_etapa = 1
        LEFT JOIN DETALLES_DIAGNOSTICO DD2 ON D.id = DD2.id_diagnostico AND DD2.id_etapa = 2
        LEFT JOIN DETALLES_DIAGNOSTICO DD3 ON D.id = DD3.id_diagnostico AND DD3.id_etapa = 3
        LEFT JOIN DETALLES_DIAGNOSTICO DD4 ON D.id = DD4.id_diagnostico AND DD4.id_etapa = 4
        LEFT JOIN DETALLES_DIAGNOSTICO DD5 ON D.id = DD5.id_diagnostico AND DD5.id_etapa = 5
        LEFT JOIN DETALLES_DIAGNOSTICO DD6 ON D.id = DD6.id_diagnostico AND DD6.id_etapa = 6
        LEFT JOIN DETALLES_DIAGNOSTICO DD7 ON D.id = DD7.id_diagnostico AND DD7.id_etapa = 7
        LEFT JOIN DETALLES_DIAGNOSTICO DD8 ON D.id = DD8.id_diagnostico AND DD8.id_etapa = 8
        LEFT JOIN DETALLES_DIAGNOSTICO DD9 ON D.id = DD9.id_diagnostico AND DD9.id_etapa = 9
        LEFT JOIN DETALLES_DIAGNOSTICO DD10 ON D.id = DD10.id_diagnostico AND DD10.id_etapa = 10
        WHERE
        U.id = %s
        """
        cursor.execute(query, (id_usuario,))
        data = cursor.fetchone()

        # Cerrar la conexión a la base de datos
        cursor.close()
        conn.close()

        # Datos de prueba
        X_test = pd.DataFrame({
            'Autoevaluación': [data[2]],
            'Relaciones interpersonales': [data[3]],
            'Actividades diarias': [data[4]],
            'Autoestima': [data[5]],
            'Estrés y afrontamiento': [data[6]],
            'Sueño y descanso': [data[7]],
            'Salud física': [data[8]],
            'Metas y aspiraciones': [data[9]],
            'Resiliencia': [data[10]],
            'Satisfacción con la vida': [data[11]]
        })

        # Realizar predicciones en el conjunto de prueba
        predictions = model.predict(X_test)

        # Valor para comparar
        valor_real = score_final

        # Calcular el porcentaje de cercanía a la realidad
        porcentaje_cercania = (1 - abs(float(predictions) - float(valor_real)) / float(valor_real)) * 100

        # Redondear la predicción y el porcentaje de cercanía a 2 decimales
        prediction = round(predictions[0], 2)
        porcentaje_cercania = round(porcentaje_cercania, 2)
        return redirect(url_for('etapa', prediction=prediction, porcentaje_cercania=porcentaje_cercania,score_final=score_final))




    session["chat_activado"] = isChatActivado(session["id_diagnostico"])

    if(clasificacion not in ["Moderado", "Alto", "Muy alto"]):
        # Redirigir a la página de resultados
        return redirect(url_for('etapa'))

    return render_template('usuario/chat.html', clasificacion=clasificacion)
    


@app.route('/resultados/score=<float:score>&numero=<int:numero>')
def resultados(score, numero):
    return render_template('usuario/resultados.html', score=score, numero=numero)


@app.get("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/search-twitter-accounts", methods=["POST"])
def getUsersByUsername():
    req = request.get_json()
    print(req)
    usuariosEncontrados = searchUserInTwitter(req["username"])
    res = make_response(jsonify({"data": usuariosEncontrados}), 200)
    print(usuariosEncontrados)
    return res

@app.route("/users/create", methods=["GET", "POST"])
def users_create():
    print("creating user..")
    if request.method == "POST":
        consumer_key="0UnkO55lofzPjPtX3zpmd4xRt"
        consumer_secret="ACloPt81xa4USf6PIutsIThrMODZrdA1ytHY55wGYlusDlfiIT"
        access_token="4855557995-NEvKeV12hruDOoLbrn36hAzQL1KWIStWnezLDJE"
        access_token_secret="LmdFUtUjqnI6u7t2aGBtAMa1PfIFK534HloxbPt7XwEu0"
        twitter_manager = TwitterUserManager(api_key=consumer_key, api_secret_key=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
        tweets = twitter_manager.get_tweets(request.form["twitter-screen-name"])
        
        depression_detector = DepressionDetector()
        #depression_detector.predict("bad")
        resultados_analizados = []
        for tweet in tweets:
            analized = depression_detector.predict(tweet["full_text"])
            resultados_analizados.append({'text': tweet["full_text"], 'res': analized})
        
        user = User(
            nickname="MyNick",
            email=request.form["email"],
            password="1234",
            patients=[PatientData(
                fullname = request.form["firstname"],
                gender = request.form["gender"]
            )]
        )
        print("storing user in db")
        print(user)
        db.session.add(user)
        db.session.commit()
        return render_template("resultados.html", len = len(resultados_analizados), TweetsList = resultados_analizados)

    return render_template("formulario.html")

@app.route("/resultados-twitter", methods=["GET"])
def resultados_twitter():
    return render_template("resultados.html")


def searchUserInTwitter(username):
    consumer_key="0UnkO55lofzPjPtX3zpmd4xRt"
    consumer_secret="ACloPt81xa4USf6PIutsIThrMODZrdA1ytHY55wGYlusDlfiIT"
    access_token="4855557995-NEvKeV12hruDOoLbrn36hAzQL1KWIStWnezLDJE"
    access_token_secret="LmdFUtUjqnI6u7t2aGBtAMa1PfIFK534HloxbPt7XwEu0"
    twitter_manager = TwitterUserManager(api_key=consumer_key, api_secret_key=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
    return twitter_manager.search_users(username)



@app.route("/generate-chatbot-response", methods=["POST"])
def generateResponseChatbot():
    chatbot = Chatbot()
    modo = "Muy alto"
    response = chatbot.generateResponse(request.json["query"], modo)
    return jsonify({
        "response": response,
        "datetime": datetime.datetime.now()
    })



import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_curve, roc_curve, auc, f1_score








if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



