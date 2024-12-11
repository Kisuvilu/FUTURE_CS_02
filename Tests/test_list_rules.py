import unittest
from scripts.list_rules import list_rules

class TestListRules(unittest.TestCase):
    def test_list_rules_non_empty(self):
        # Test listing rules when there are existing rules
        # Assume some rules have already been added
        rules = list_rules()
        self.assertGreater(len(rules), 0, "Rules list should not be empty.")

    def test_list_rules_empty(self):
        # Test listing rules when no rules are present
        # Assume all rules have been cleared
        # (Clear rules via another function or setup step)
        rules = list_rules()
        self.assertEqual(len(rules), 0, "Rules list should be empty.")

    def test_list_rules_format(self):
        # Test that listed rules have the correct format
        rules = list_rules()
        for rule in rules:
            self.assertIn("action", rule, "Rule should have 'action' field.")
            self.assertIn("port", rule, "Rule should have 'port' field.")
            self.assertIn("protocol", rule, "Rule should have 'protocol' field.")

if __name__ == "__main__":
    unittest.main()