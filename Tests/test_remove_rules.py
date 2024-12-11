import unittest
from scripts.remove_rules import remove_rule

class TestRemoveRules(unittest.TestCase):
    def test_remove_existing_rule(self):
        # Test removing an existing rule
        rule = {"action": "allow", "port": 80, "protocol": "tcp"}
        # Assume the rule is already added
        result = remove_rule(rule)
        self.assertTrue(result, "Failed to remove an existing rule.")

    def test_remove_nonexistent_rule(self):
        # Test trying to remove a rule that doesn't exist
        rule = {"action": "allow", "port": 443, "protocol": "tcp"}
        result = remove_rule(rule)
        self.assertFalse(result, "Nonexistent rule should not be removable.")

    def test_remove_invalid_rule(self):
        # Test removing a rule with invalid data
        rule = {"port": 80}  # Missing action and protocol
        result = remove_rule(rule)
        self.assertFalse(result, "Invalid rule should not be removed.")

if __name__ == "__main__":
    unittest.main()