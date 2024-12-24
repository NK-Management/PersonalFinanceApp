import unittest
from services.expense_tracking_service.app.services.jar_service import JarService
from services.expense_tracking_service.app.utils.db import db
from services.expense_tracking_service.app import create_app
from services.expense_tracking_service.app.models.jar import Jar

class TestJarService(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_jar(self):
        jar_data = {
            'name': 'Emergency Fund',
            'category': 'Savings',
            'balance': 1000.0
        }
        result = JarService.create_jar(jar_data)
        self.assertIn('id', result)
        self.assertEqual(result['name'], 'Emergency Fund')

    def test_get_all_jars(self):
        self.client.post('/jars/', json={'name': 'Emergency Fund', 'category': 'Savings', 'balance': 1000.0})
        jars = JarService.get_all_jars()
        self.assertEqual(len(jars), 1)
