import sys
from utils.logger import setup_logger

logger = setup_logger("firewall.log")

def remove_rule(rule_id):
    # Command to remove rule using `ufw`
    logger.info(f"Rule removed: {rule_id}")

if __name__ == "__main__":
    rule_id = sys.argv[1]
    remove_rule(rule_id)