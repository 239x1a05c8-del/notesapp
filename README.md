FLASK NOTES APP~
Simple Notes Management Application using Flask

DESCRIPTION~

This is a simple web-based Notes application built with Flask.
The app allows users to:

Add notes

Edit notes

Delete notes

Add two numbers using a JSON API endpoint

All notes are stored in memory using a Python list.

FEATURES~

Add new notes

Edit existing notes

Delete notes

JSON API endpoint to add two numbers

Beginner-friendly Flask structure

TECH STACK~

Backend: Python
Framework: Flask
Frontend: HTML (Jinja2 Templates)
API Testing: Postman

PROJECT STRUCTURE~

project-folder/

app.py
templates/
index.html
edit.html
README.txt

INSTALLATION & SETUP~

Clone the repository

git clone https://github.com/your-username/your-repo-name.git

cd your-repo-name

(Optional) Create virtual environment

python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

Install Flask

pip install flask

RUNNING THE APPLICATION~

python app.py

The application will run at:

http://127.0.0.1:5000/

AVAILABLE ROUTES

Home Page
GET /
Displays all notes.

Add Note
POST /add
Adds a new note via form submission.

Delete Note
GET /delete/<index>
Deletes a note by index.

Edit Note
GET /edit/<index>
POST /edit/<index>
Edits a note by index.

Add Numbers API (JSON)
POST /addNum
Content-Type: application/json

Example Request:

{
"num1": 10,
"num2": 5
}

Example Response:

{
"num1": 10,
"num2": 5,
"sum": 15
}

IMPORTANT NOTES~

Notes are stored in memory only.

Data will be lost when the server restarts.

This project is intended for learning purposes.

FUTURE IMPROVEMENTS~

Add database support (SQLite or PostgreSQL)

Add user authentication

Improve UI design

Add persistent storage

LICENSE

Free to use for educational purposes.


<img width="548" height="379" alt="image" src="https://github.com/user-attachments/assets/76d77a5d-7278-4b87-8c31-eca8e0ad30d3" />

<img width="513" height="330" alt="image" src="https://github.com/user-attachments/assets/d395533b-f665-4f2e-b834-f42b05bc5ac6" />
