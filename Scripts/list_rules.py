from utils.logger import setup_logger

logger = setup_logger("firewall.log")

def list_rules():
    # Command to list rules using `ufw`
    logger.info("Fetching list of firewall rules...")
    # Logic to fetch and display rules
    return []

if __name__ == "__main__":
    print(list_rules())