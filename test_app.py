import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json, jsonify, request
from bson import ObjectId
from app import app  # Ajusta la importación según tu estructura de proyecto

class TestUsuarioRegistro(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    @patch('app.usuarios')  # Ajusta esta línea según la ubicación de 'usuarios' en tu código
    def test_registrar_usuario_nuevo(self, mock_usuarios):
        mock_insert_one = MagicMock()
        mock_usuarios.insert_one = mock_insert_one
        mock_find = MagicMock(return_value=[])
        mock_usuarios.find = mock_find

        data = {
            "nombreUsuario": "testuser",
            "nombre": "Test",
            "apellido": "User",
            "dni": "12345678",
            "correoElectronico": "testuser@example.com",
            "contrasenaHash": "hashedpassword",
            "fechaRegistro": "2024-05-26",
            "roles": ["user"],
            "activo": True
        }

        response = self.client.post('/api/usuarios2', data=json.dumps(data), content_type='application/json')
        response_data = json.loads(response.data.decode('utf-8'))
        
        self.assertEqual(response.status_code, 201)
        self.assertIn('mensaje', response_data)
        self.assertEqual(response_data['mensaje'], 'Usuario registrado exitosamente')
        self.assertIn('usuarios', response_data)
        self.assertEqual(len(response_data['usuarios']), 0)

    @patch('app.usuarios')  # Ajusta esta línea según la ubicación de 'usuarios' en tu código
    def test_actualizar_usuario_existente(self, mock_usuarios):
        usuario_id = ObjectId()
        mock_update_one = MagicMock(return_value=MagicMock(modified_count=1))
        mock_usuarios.update_one = mock_update_one
        mock_find = MagicMock(return_value=[{
            "_id": usuario_id,
            "nombreUsuario": "updateduser",
            "nombre": "Updated",
            "apellido": "User",
            "dni": "87654321",
            "correoElectronico": "updateduser@example.com",
            "contrasenaHash": "newhashedpassword",
            "fechaRegistro": "2024-05-26",
            "roles": ["admin"],
            "activo": False
        }])
        mock_usuarios.find = mock_find

        data = {
            "_id": str(usuario_id),
            "nombreUsuario": "updateduser",
            "nombre": "Updated",
            "apellido": "User",
            "dni": "87654321",
            "correoElectronico": "updateduser@example.com",
            "contrasenaHash": "newhashedpassword",
            "fechaRegistro": "2024-05-26",
            "roles": ["admin"],
            "activo": False
        }

        response = self.client.post('/api/usuarios2', data=json.dumps(data), content_type='application/json')
        response_data = json.loads(response.data.decode('utf-8'))
        
        self.assertEqual(response.status_code, 201)
        self.assertIn('mensaje', response_data)
        self.assertEqual(response_data['mensaje'], 'Usuario actualizado exitosamente')
        self.assertIn('usuarios', response_data)
        self.assertEqual(len(response_data['usuarios']), 1)
        self.assertEqual(response_data['usuarios'][0]['nombreUsuario'], 'updateduser')

if __name__ == '__main__':
    unittest.main()

