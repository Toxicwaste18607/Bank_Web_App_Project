# Bank_Web_App_Project

Personal Banking App
Overview
The Personal Banking App is a web-based banking simulation built using Python and Streamlit. The application allows users to create accounts, log in securely, deposit and withdraw money, and manage account balances through an interactive interface.
The project was designed to demonstrate object-oriented programming, file handling, session management, and basic financial operations in a realistic banking environment.

Features
User account creation
User login system
Deposit functionality
Withdrawal functionality
Balance management
Session state handling
JSON-based data storage
User role support
Streamlit web interface
Technologies Used
Python
Streamlit
JSON
Object-Oriented Programming (OOP)

Installation
Install the required dependencies:
pip install streamlit
Running the Application
Run the application using:
streamlit run src/main.py
How the Application Works
Users create or log into an account.
User information is loaded from a JSON file.
The application stores user session data using Streamlit session state.
Deposits and withdrawals update the user balance.
Updated account information is saved back into the JSON storage file.
Data Storage
The application uses a JSON file to store user information and balances. Data is loaded when the application starts and saved whenever account changes occur.
Example stored data includes:

User ID
Username
Email
Account balance
User role
Future Improvements
Potential future upgrades include:
Transfer money between accounts
Transaction history tracking
Password hashing and encryption
Database integration
Improved UI design
Admin management tools
Multi-factor authentication
Educational Purpose
This project was created as a learning experience to improve understanding of:
Python programming
Object-oriented design
Web application development
Data persistence
User authentication systems
Application structure and organization


AI Assistance
Artificial intelligence tools were used during the development of this project as a learning and debugging resource. AI assistance was primarily used to help identify coding errors, explain programming concepts, assist with troubleshooting, and provide guidance on improving project structure and organization.
All core implementation, project design decisions, and final code integration were completed by the developer as part of the learning process.
