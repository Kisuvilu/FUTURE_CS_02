# FUTURE_CS_02
Setting Up a Firewall

# Firewall Configuration Project

## Description
This project provides Python-based scripts to manage firewall configurations using `ufw` (Uncomplicated Firewall). It includes functionalities to add, remove, and list firewall rules, as well as automated tests to ensure reliability.  

## Features 
- **Add Rules:** Add new firewall rules (e.g., allow/block ports, protocols).  
- **Remove Rules**: Remove existing firewall rules.  
- **List Rules**: Display the current firewall configuration.  
- **Logging**: Track all operations for auditing and debugging purposes.  
- **Automated Tests** Ensure robust functionality with unit tests.  



## Project Structure

firewall-config/
├── README.md
├── scripts/
│   ├── add_rules.py
│   ├── remove_rules.py
│   ├── list_rules.py
├── tests/
│   ├── test_add_rules.py
│   ├── test_remove_rules.py
│   ├── test_list_rules.py
├── logs/
│   └── firewall.log
└── requirements.txt


### **Folder Overview**  
- **scripts/**: Contains the core functionality for managing firewall rules.  
- **tests/**: Includes unit tests for validating the functionality of the scripts.  
- **logs/**: Stores logs for all operations performed on the firewall.  
- **requirements.txt**: Lists the dependencies required to run the project.
  
## **Prerequisites**  
- Python 3.8+  
- `ufw` installed and configured on the system 

## **Installation**  

1. Clone the repository:  
   git clone https://github.com/yourusername/firewall-config.git
   cd firewall-config


2. Install dependencies:  
   pip install -r requirements.txt
  

## **Usage**  

### **Add a Rule**  
Run the script to add a rule:  
python scripts/add_rules.py --action allow --port 80 --protocol tcp

### **Remove a Rule**  
Run the script to remove a rule:  
python scripts/remove_rules.py --action allow --port 80 --protocol tcp


### **List Rules**  
Run the script to list all firewall rules:  
python scripts/list_rules.py

## **Testing**  

To run all tests: 
python -m unittest discover tests/

## **Logging**
Logs are stored in the `logs/firewall.log` file. Each operation is logged with timestamps for traceability.  

## Contributing  
Contributions are welcome! Please follow these steps:  
1. Fork the repository.  
2. Create a new branch: `git checkout -b feature-name`.  
3. Make your changes and commit: `git commit -m "Add feature"`.  
4. Push to your branch: `git push origin feature-name`.  
5. Open a pull request.  

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

## Acknowledgments
- `ufw` documentation  
- Python's `argparse` and `unittest` libraries  
