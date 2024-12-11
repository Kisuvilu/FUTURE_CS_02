import unittest
from scripts.add_rules import add_rule

class TestAddRules(unittest.TestCase):
    def test_add_valid_rule(self):
        # Test adding a valid rule
        rule = {"action": "allow", "port": 80, "protocol": "tcp"}
        result = add_rule(rule)
        self.assertTrue(result, "Failed to add a valid rule.")

    def test_add_invalid_rule(self):
        # Test adding a rule with missing information
        rule = {"action": "allow", "port": 80}  # Missing protocol
        result = add_rule(rule)
        self.assertFalse(result, "Invalid rule should not be added.")

    def test_add_duplicate_rule(self):
        # Test adding a duplicate rule
        rule = {"action": "allow", "port": 80, "protocol": "tcp"}
        add_rule(rule)  # Add once
        result = add_rule(rule)  # Try adding again
        self.assertFalse(result, "Duplicate rule should not be added.")

if __name__ == "__main__":
    unittest.main()