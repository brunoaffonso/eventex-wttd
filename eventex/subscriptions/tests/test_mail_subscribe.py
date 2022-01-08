from django.test import TestCase
from django.core import mail


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Bruno Teixeira', cpf='12345678901',
                    email='bruno@teixeira.com', phone='21-99999-9999')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'brunoaffonso27@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['brunoaffonso27@gmail.com', 'bruno@teixeira.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Bruno Teixeira',
            '12345678901',
            'bruno@teixeira.com',
            '21-99999-9999',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
