def validate_rule(rule):
    required_keys = {"action", "port", "protocol"}
    return all(key in rule for key in required_keys)