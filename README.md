# CS340-Module-8-Journal
Project Overview
Grazioso Salvare has requested documentation to accompany the code for your dashboard. This document ensures that they can understand the work that was completed and easily maintain the code for this project.
This README file documents the project and provides instructions for reproducing the project.
Required Functionality
This project implements a dashboard that allows users to filter and analyze animal data based on different rescue types. The dashboard includes the following features:
•	A user interface for selecting different rescue types.
•	A dynamically updated table displaying animal records.
•	A graphical representation of the data through a pie chart.
•	A map that plots the location of selected animals.
Screenshots
Below are placeholders for screenshots demonstrating the functionality of the dashboard under different filter selections:
1.	Water Rescue
  
2.	Mountain or Wilderness Rescue
3.	  Disaster Rescue or Individual Tracking
  
4.	Reset (Unfiltered Data)
 Tools Used & Rationale
MongoDB
MongoDB was used as the database component to store and retrieve animal records. It was chosen due to its flexibility in handling semi-structured data and its seamless integration with Python.
Dash Framework
Dash was used to create the web-based dashboard. It provides an intuitive way to build interactive visualizations and data tables using Python.
Additional Resources
•	MongoDB Documentation: https://www.mongodb.com/docs/
•	Dash Framework: https://dash.plotly.com/
Steps Taken to Complete the Project
1.	Established a connection to the MongoDB database and retrieved the animal data.
2.	Processed the data into a Pandas DataFrame for easy manipulation and filtering.
3.	Created an interactive Dash application with: 
o	A table displaying animal data.
o	A pie chart representing the distribution of breeds.
o	A map displaying the location of selected animals.
4.	Implemented filtering functionality based on different rescue types.
5.	Debugged and ensured that all functionality met the project requirements.
Challenges & Solutions
1.	Filtering Issues: Initially, filtering by rescue type did not return expected results. The issue was resolved by ensuring that the correct field in the database was queried.
2.	No Data Displayed in the Table: The table did not populate correctly at first. This was fixed by checking the connection to MongoDB and ensuring data was successfully retrieved.
3.	Graph and Map Not Updating Properly: The map and pie chart were not updating dynamically. The issue was resolved by correctly linking callbacks in Dash.
Instructions for Running the Project
1.	Ensure you have Python and the required libraries installed: 
2.	pip install pymongo pandas dash plotly dash-leaflet
3.	Ensure you have access to the MongoDB database with the correct credentials.
4.	Run the Dash application using: 
5.	python dashboard.py
6.	Open the provided local URL in your web browser to interact with the dashboard.
________________________________________


Maintaining Readability, Adaptability, and Maintainability
Writing maintainable, readable, and adaptable programs is crucial in software development. In Project Two, we utilized a CRUD Python module to connect dashboard widgets to the MongoDB database. This approach helped in:

Readability: Using clear function names, modular coding practices, and comments made it easier to understand.
Maintainability: Separating concerns between the database operations and the dashboard logic allowed for easier debugging and updates.
Adaptability: The CRUD module can be repurposed or extended for other projects requiring database operations without rewriting major portions of the code.
In the future, this CRUD module could be used for similar applications where user interfaces interact with databases, such as inventory management systems, web dashboards, or analytics tools.

Approaching Problems as a Computer Scientist
When tackling the database and dashboard requirements for Grazioso Salvare, I first analyzed the requirements and identified key components:

Understanding the Data Flow – How the dashboard retrieves and displays data from MongoDB.
Optimizing Queries – Ensuring data retrieval was efficient and structured.
Error Handling – Implementing exception handling to prevent crashes.
Compared to previous assignments, this project required a deeper understanding of NoSQL databases (MongoDB) rather than traditional relational databases (SQL). The project also emphasized real-world application by simulating a company scenario where structured data storage and retrieval are essential.

To meet future client needs, strategies such as:

Indexing for faster queries,
Data validation to prevent inconsistencies, and
Implementing role-based access control (RBAC) for security would enhance database performance.
The Role and Importance of Computer Scientists
Computer scientists develop software solutions that improve efficiency, automate processes, and handle large-scale data management. In this project, the CRUD dashboard system helps Grazioso Salvare:

Improve data management – The dashboard provides easy access to stored animal rescue data.
Enhance decision-making – By visualizing key insights, employees can make informed choices faster.
Streamline operations – Automating data retrieval reduces manual effort and errors.
These contributions highlight the importance of well-structured software in business applications, demonstrating how programming skills translate into impactful, real-world solutions.
