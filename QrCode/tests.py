from django.test import TestCase, Client
from django.urls import reverse

class GenerateQRCodeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.generate_url = reverse("qrcode:generate")

    def test_generate_qr_code_default(self):
        """
        Test generating a QR code without providing the 'data' parameter.
        """
        response = self.client.get(self.generate_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "image/png")
        # Ensure the response content is not empty
        self.assertTrue(response.content)

    def test_generate_qr_code_with_data(self):
        """
        Test generating a QR code when passing a specific 'data' parameter.
        """
        test_data = "https://example.com"
        response = self.client.get(self.generate_url, {"data": test_data})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "image/png")
        self.assertTrue(response.content)


class QRCodeHomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse("qrcode:home")

    def test_home_view_loads_correct_template(self):
        """
        Test that the home view loads the template correctly.
        """
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        # Check that the response contains key HTML elements like the form and heading
        self.assertContains(response, "<form")
        self.assertContains(response, "QR Code Generator")
