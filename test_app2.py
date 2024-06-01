import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, session, request, redirect, url_for
from bson import ObjectId  # Asegúrate de importar ObjectId
from app import app  # Ajusta la importación según tu estructura de proyecto

class TestLoginComun(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'secret_key_for_testing'  # Necesario para la sesión
        app.config['SERVER_NAME'] = 'localhost'  # Configurar SERVER_NAME para pruebas
        self.client = app.test_client()
        self.client.testing = True

    @patch('app.usuarios')  # Ajusta esta línea según la ubicación de 'usuarios' en tu código
    def test_login_comun_exitoso(self, mock_usuarios):
        # Mock del método find_one para devolver un usuario válido
        mock_user = {
            "_id": ObjectId(),
            "dni": "12345678",
            "contrasenaHash": "hashedpassword"
        }
        mock_usuarios.find_one = MagicMock(return_value=mock_user)

        # Datos de entrada del formulario
        data = {
            "dni": "12345678",
            "password": "hashedpassword"
        }

        # Envío de la solicitud POST para iniciar sesión
        response = self.client.post('/login-comun', data=data)

        # Verificaciones
        self.assertEqual(response.status_code, 302)  # Verifica si la respuesta es una redirección
        
        with app.app_context():
            expected_url = url_for('admin_home', _external=False)  # Cambiar a _external=False
            self.assertEqual(response.location, expected_url)
        
        with self.client.session_transaction() as sess:
            self.assertEqual(sess['user_id'], str(mock_user["_id"]))

    @patch('app.usuarios')
    def test_login_comun_usuario_no_encontrado(self, mock_usuarios):
        # Mock del método find_one para devolver None (usuario no encontrado)
        mock_usuarios.find_one = MagicMock(return_value=None)

        data = {
            "dni": "12345678",
            "password": "hashedpassword"
        }

        response = self.client.post('/login-comun', data=data)
        
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data.decode(), "Usuario no encontrado")

    @patch('app.usuarios')
    def test_login_comun_contrasena_incorrecta(self, mock_usuarios):
        # Mock del método find_one para devolver un usuario con contraseña incorrecta
        mock_user = {
            "_id": ObjectId(),
            "dni": "12345678",
            "contrasenaHash": "otherpassword"
        }
        mock_usuarios.find_one = MagicMock(return_value=mock_user)

        data = {
            "dni": "12345678",
            "password": "wrongpassword"
        }

        response = self.client.post('/login-comun', data=data)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), "Contraseña incorrecta")

    def test_login_comun_datos_incompletos(self):
        # Envío de la solicitud POST sin datos
        response = self.client.post('/login-comun', data={})
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), "Datos de entrada incompletos")

if __name__ == '__main__':
    unittest.main()
