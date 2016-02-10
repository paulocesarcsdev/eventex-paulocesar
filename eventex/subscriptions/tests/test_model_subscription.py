from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
           name='Paulo Cesar',
           cpf='12345678901',
           email='paulocesarcs.info@gmail.com',
           phone='62-94130086'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test(self):
        """Subscription must have auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Paulo Cesar', str(self.obj))