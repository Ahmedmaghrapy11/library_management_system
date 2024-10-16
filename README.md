# Library Management Web Application - MVT Project

## Introduction
This project is a **Library Management Web Application** built as a back-end project using **Python** and the **Django Web Framework**. It provides basic library management functionalities, such as managing books, authors, and library members. The front-end is developed using **HTML**, **CSS**, **JavaScript**, and **jQuery**, while the back-end is powered by **Django** to handle server-side logic and data storage.

## Technologies
- **Python**: 3.9
- **Django**: 4.1 (Web framework)
- **HTML**: Front-end structure
- **CSS**: Styling the front-end
- **JavaScript**:  ES6 for client-side interactions
- **jQuery**: Simplified JavaScript operations and DOM manipulation
- **SQLite3**: Default database for Django

## Features
- **Book Management**: Add, edit, delete, and view books in the library.
- **Author Management**: Manage information about book authors.
- **Library Members**: Manage library members and their borrowing status.
- **Book Borrowing**: Track which members have borrowed which books.
- **Search Functionality**: Search for books by title or author.
- **Responsive Design**: Simple and responsive UI built with HTML, CSS, and jQuery.

## Setup

### 1. Clone the Repository
To start, clone this repository to your local machine:
```bash
git clone https://github.com/Ahmedmaghrapy11/library_management_system.git
cd library_management_system/lms/
```

### 2. Install Dependencies

- Create virtual environment
```bash
python3 -m venv env
```

- Activate virtual environment
 
  **On macOS/Linux**:
```bash
source env/bin/activate
```
  **On Windows**:
```bash
.\env\Scripts\activate
```

- Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Run the Development Server
```bash
python manage.py runserver
```
