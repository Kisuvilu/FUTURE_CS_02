import sys
from utils.validator import validate_rule
from utils.logger import setup_logger

logger = setup_logger("firewall.log")

def add_rule(rule):
    if validate_rule(rule):
        # Command to add rule using `ufw`
        logger.info(f"Rule added: {rule}")
    else:
        logger.error("Invalid rule format.")

if __name__ == "__main__":
    rule = sys.argv[1]
    add_rule(rule)