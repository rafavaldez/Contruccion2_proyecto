import unittest
from unittest.mock import patch
from flask import session, json
import pandas as pd
from app import app

class TestAdminResultadosAnalisis(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'secret_key_for_testing'
        self.client = app.test_client()
        self.client.testing = True

    @patch('pandas.read_csv')
    @patch('pandas.read_excel')
    def test_admin_ResultadosAnalisis_csv(self, mock_read_excel, mock_read_csv):
        # Mock the CSV data
        mock_data = pd.DataFrame({
            'precio_unitario': [10, 20, 30, 100, 200, 300, 500, 700, 900, 1200],
            'marca': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A'],
            'categoria': ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z', 'X'],
            'nombre': ['prod1', 'prod2', 'prod3', 'prod1', 'prod2', 'prod3', 'prod1', 'prod2', 'prod3', 'prod1']
        })
        mock_read_csv.return_value = mock_data

        # Setup the session
        with self.client.session_transaction() as sess:
            sess['uploaded_filename'] = 'test.csv'

        # Perform the request
        response = self.client.get('/admin/ResultadosAnalisis')
        self.assertEqual(response.status_code, 200)

    @patch('pandas.read_csv')
    @patch('pandas.read_excel')
    def test_admin_ResultadosAnalisis_excel(self, mock_read_excel, mock_read_csv):
        # Mock the Excel data
        mock_data = pd.DataFrame({
            'precio_unitario': [10, 20, 30, 100, 200, 300, 500, 700, 900, 1200],
            'marca': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A'],
            'categoria': ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z', 'X'],
            'nombre': ['prod1', 'prod2', 'prod3', 'prod1', 'prod2', 'prod3', 'prod1', 'prod2', 'prod3', 'prod1']
        })
        mock_read_excel.return_value = mock_data

        # Setup the session
        with self.client.session_transaction() as sess:
            sess['uploaded_filename'] = 'test.xlsx'

        # Perform the request
        response = self.client.get('/admin/ResultadosAnalisis')
        self.assertEqual(response.status_code, 200)

    def test_admin_ResultadosAnalisis_no_file(self):
        response = self.client.get('/admin/ResultadosAnalisis')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn('error', response_data)
        self.assertEqual(response_data['error'], 'No se ha cargado ningún archivo')

    @patch('pandas.read_csv')
    @patch('pandas.read_excel')
    def test_admin_ResultadosAnalisis_invalid_file(self, mock_read_excel, mock_read_csv):
        # Setup the session with an invalid file type
        with self.client.session_transaction() as sess:
            sess['uploaded_filename'] = 'test.txt'

        # Perform the request
        response = self.client.get('/admin/ResultadosAnalisis')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn('error', response_data)
        self.assertEqual(response_data['error'], 'Formato de archivo no admitido. Cargue un archivo CSV o Excel.')

if __name__ == '__main__':
    unittest.main()

