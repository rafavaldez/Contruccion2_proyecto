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

@app.route('/admin/RegistroPacientes')
def admin_RegistroPacientes():
    return render_template('admin/forms.html')

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


#Authentication



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






@app.route("/registro")
def registro():
    return render_template('registro.html')



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


model_filename = 'static/modelo/linear_regression_model.joblib'
encoder_filename = 'static/modelo/one_hot_encoder.joblib'
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
    app.run(port=5001)  # Cambia 5001 por otro puerto que esté libre




