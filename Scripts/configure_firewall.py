from utils.config_loader import load_config
from utils.logger import setup_logger

logger = setup_logger("firewall.log")

def configure_firewall():
    config = load_config("configs/firewall_settings.yaml")
    logger.info("Configuring firewall...")
    # Logic to apply default or custom configurations
    logger.info("Firewall configuration applied successfully.")

if __name__ == "__main__":
    configure_firewall()
