from werkzeug.utils import html
from app import app
from unittest import TestCase

app.config["TESTING"] = True
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]


class FlaskConverterRoutes(TestCase):
    def test_base(self):
        """Testing base route works correctly"""

        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<title>Currency Converter</title>", html)

    def test_post_request(self):
        """Test to check that post request is returning correct information."""
        with app.test_client() as client:
            resp = client.post(
                "/", data={"from-currency": "USD", "to-currency": "USD", "amount": "10"}
            )
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("$10.00", html)

    def test_invalid_post_request(self):
        """Catch the redirect when an invalid code is returned"""

        with app.test_client() as client:
            resp = client.post(
                "/", data={"from-currency": "ZZZ", "to-currency": "USD", "amount": "10"}
            )

            self.assertEqual(resp.status_code, 302)

    def test_flash_message_response(self):
        """Testing flash message response"""

        with app.test_client() as client:
            resp = client.post(
                "/",
                data={"from-currency": "ZZZ", "to-currency": "USD", "amount": "10"},
                follow_redirects=True,
            )

            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("not a valid currency code.", html)

    def test_invalid_amount(self):
        """Testing flash message when incorrect number amount is provided"""

        with app.test_client() as client:
            resp = client.post(
                "/",
                data={"from-currency": "USD", "to-currency": "USD", "amount": "five"},
                follow_redirects=True,
            )

            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("not enter a valid number", html)

    def test_empty_field(self):
        """Testing redirect when a field is left empty"""

        with app.test_client() as client:
            resp = client.post(
                "/",
                data={"from-currency": "None", "to-currency": "USD", "amount": "10"},
                follow_redirects=True,
            )

            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("currency not a valid currency code.", html)
