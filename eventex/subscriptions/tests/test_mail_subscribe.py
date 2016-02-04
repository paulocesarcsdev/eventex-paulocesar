from django.core import mail
from django.test import TestCase


class SubscribePostTestValid(TestCase):
    def setUp(self):
        data = dict(name='Paulo César', cpf='12345678901',
                    email='paulocesarcs.info@gmail.com', phone='62-94130086')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'paulocesarcs.info@gmail.com'

        self.assertEqual(expect,self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['paulocesarcs.info@gmail.com', 'paulocesarcs.info@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Paulo César',
            '12345678901',
            'paulocesarcs.info@gmail.com',
            '62-94130086',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)