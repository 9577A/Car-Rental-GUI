# Car Rental GUI

## Overview
Car Rental GUI is a fully functional example project that demonstrates the integration of a MySQL database with a graphical user interface (GUI) built using the Tkinter library. 
The project aims to simulate a car rental company's operations by providing features such as user management, car reservation, and reservation management.

## Features
The Car Rental GUI offers the following features:

1. User Management: Users can create new accounts and log in to access the system.
2. Car Reservation: Users can reserve cars for specific dates, ensuring that reservations do not overlap with existing ones. The system checks the availability of cars before allowing reservations.
3. Reservation Management: Users can view and manage their reservations, including removing existing reservations.
4. MySQL Database Integration: The project connects to a MySQL database, allowing seamless storage and retrieval of data related to users, cars, and reservations.

## Goals
The primary goals of this project are to showcase the integration of a MySQL database with a GUI and to demonstrate the implementation of car rental functionalities. 
By providing a user-friendly interface, the project aims to simulate real-world car rental scenarios, ensuring data integrity and preventing conflicting reservations.

## How to Use It

Before using the Car Rental GUI, ensure that you have MySQL database installed on your system. Follow these steps to get started:

1. Edit the `database_setup.py` file: Open the `database_setup.py` file and fill in your MySQL database information, including the host name, username, and password. Save the file after making the necessary changes.

2. Run the `database_setup.py` file: Execute the `database_setup.py` file to create the required database structure and tables. This step will initialize the database for the Car Rental GUI application.

3. Insert car models: As the super user functionality is not implemented, you need to manually insert car models into the "car" table of the database. This step ensures that the available car models are populated in the application.

Register and start using the app: Once the database setup is complete and the car models are inserted, you are ready to register and freely use the Car Rental GUI application. Create a new user account, log in, and begin exploring the features such as reserving cars for specific dates and managing your reservations.
