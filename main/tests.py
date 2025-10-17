from django.test import TestCase


class IndexViewTests(TestCase):

    def test_index_page_displays_welcome_message(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the Happinometer")
