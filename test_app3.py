import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, session, request, jsonify
from io import BytesIO
import os
import pandas as pd
from app import app, upload_file  # Asegúrate de ajustar la importación según tu estructura de proyecto

class TestFileUpload(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'secret_key_for_testing'
        app.config['UPLOAD_FOLDER'] = '/tmp'  # Ajusta esto a la carpeta de tu elección
        self.client = app.test_client()
        self.client.testing = True

    @patch('app.documentos')  # Ajusta esta línea según la ubicación de 'documentos' en tu código
    def test_upload_file_successful(self, mock_documentos):
        # Crea un archivo CSV en memoria
        data = b'col1,col2,col3\n1,2,3\n4,5,6'
        data_file = BytesIO(data)
        data_file.filename = 'test.csv'

        # Simula la carga del archivo
        data = {
            'file': (data_file, data_file.filename)
        }
        response = self.client.post('/upload', content_type='multipart/form-data', data=data)
        
        # Verifica que el archivo se haya procesado correctamente
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertIn('data', response_data)

    def test_upload_file_no_file_part(self):
        response = self.client.post('/upload', content_type='multipart/form-data', data={})
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertIn('error', response_data)
        self.assertEqual(response_data['error'], 'No file part')

    def test_upload_file_no_selected_file(self):
        data = {
            'file': (BytesIO(b''), '')
        }
        response = self.client.post('/upload', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertIn('error', response_data)
        self.assertEqual(response_data['error'], 'No selected file')

    @patch('app.documentos')
    def test_upload_file_invalid_format(self, mock_documentos):
        data = b'invalid content'
        data_file = BytesIO(data)
        data_file.filename = 'test.txt'

        data = {
            'file': (data_file, data_file.filename)
        }
        response = self.client.post('/upload', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertIn('error', response_data)
        self.assertEqual(response_data['error'], 'Formato de archivo no admitido')

if __name__ == '__main__':
    unittest.main()
