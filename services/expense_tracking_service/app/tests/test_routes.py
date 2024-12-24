import unittest
from services.expense_tracking_service.app import create_app
from services.expense_tracking_service.app.utils.db import db
from services.expense_tracking_service.app.models.jar import Jar
from flask import json

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_jar(self):
        response = self.client.post('/jars/', json={'name': 'Emergency Fund', 'category': 'Savings', 'balance': 1000.0})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', data)
        self.assertEqual(data['name'], 'Emergency Fund')

    def test_get_all_jars(self):
        self.client.post('/jars/', json={'name': 'Emergency Fund', 'category': 'Savings', 'balance': 1000.0})
        response = self.client.get('/jars/')
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
