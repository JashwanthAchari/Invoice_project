from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(APITestCase):
    def setUp(self):
        self.invoice = Invoice.objects.create(date='2024-01-20', customer_name='Test Customer')
        self.detail_data = {'description': 'Test Description', 'quantity': 2, 'unit_price': 10.0, 'price': 20.0}

    def test_create_invoice(self):
        data = {'date': '2024-01-20', 'customer_name': 'Test Customer'}
        response = self.client.post('/api/invoices/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_invoices(self):
        response = self.client.get('/api/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invoice_details(self):
        response = self.client.get(f'/api/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invoice(self):
        data = {'date': '2024-01-21', 'customer_name': 'Updated Customer'}
        response = self.client.put(f'/api/invoices/{self.invoice.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_invoice(self):
        response = self.client.delete(f'/api/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_invoice_detail(self):
        response = self.client.post(f'/api/invoices/{self.invoice.id}/', self.detail_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
