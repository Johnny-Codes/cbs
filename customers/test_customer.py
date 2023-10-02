from django.test import TestCase
from customers.models import Customers


class CustomersModelTestCase(TestCase):
    def setUp(self):
        self.customer = Customers.objects.create(
            username="testuser",
            email="test@example.com",
            phone_number="1234567890",
            address_1="123 Main St",
            city="Sample City",
            state="CA",
            zip_code="12345",
        )

    def test_customer_fields(self):
        customer_from_db = Customers.objects.get(pk=self.customer.pk)

        self.assertEqual(customer_from_db.username, "testuser")
        self.assertEqual(customer_from_db.email, "test@example.com")
        self.assertEqual(customer_from_db.phone_number, "1234567890")
        self.assertEqual(customer_from_db.address_1, "123 Main St")
        self.assertEqual(customer_from_db.city, "Sample City")
        self.assertEqual(customer_from_db.state, "CA")
        self.assertEqual(customer_from_db.zip_code, "12345")

    def test_soft_delete(self):
        self.customer.soft_delete()

        customer_from_db = Customers.objects.get(pk=self.customer.pk)
        self.assertTrue(customer_from_db.is_deleted)

    def test_restore(self):
        self.customer.restore()

        customer_from_db = Customers.objects.get(pk=self.customer.pk)
        self.assertFalse(customer_from_db.is_deleted)
