import unittest
from city_functions import get_formatted_name


class NameTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_name = get_formatted_name("santiago", "chile")
        self.assertEqual(formatted_name, "Santiago, Chile - Population X")

    def test_city_country_population(self):
        formatted_name = get_formatted_name("santiago", "chile", "50000000")
        self.assertEqual(formatted_name, "Santiago, Chile - Population 50000000")


if __name__ == '__main__':
    unittest.main()
