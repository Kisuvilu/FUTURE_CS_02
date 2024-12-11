import unittest
from scripts.configure_firewall import configure_firewall

class TestConfigureFirewall(unittest.TestCase):
    def test_configuration(self):
        result = configure_firewall()
        self.assertTrue(result)