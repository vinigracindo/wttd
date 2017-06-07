from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Vicente Marçal',
            cpf = '1234567899',
            email = 'vicente.marcal@gmail.com',
            phone = '69-981146191'
        )
        self.obj.save()

    def test_create(self):

        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr. """
        self.assertIsInstance(self.obj.created_at, datetime)