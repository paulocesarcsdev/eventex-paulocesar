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