# GoNZ Tours Project

## Overview

This project is a Django-based web application for managing and viewing tours and agents for a fictional tourism service, GoNZ Tours. The application provides functionality for user authentication, managing tours, and viewing agent details.

## Features

- User authentication (signup, login, logout, profile management).
- Management of tours and agents through the Django admin interface.
- Frontend pages for listing tours and agents with detailed views.
- Bootstrap integration for responsive design.

## Prerequisites

To run this project locally, you will need the following installed on your system:

- Python 3.11+
- pip (Python package installer)
- virtualenv (recommended for creating isolated Python environments)

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/gonztours.git
   cd gonztours
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     env\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source env/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations to set up the SQLite database:**

   ```bash
   python manage.py migrate
   ```

6. **Populate the database with initial tour data:**

   If you want to populate the database with sample data, run the `populate_tours.py` script:

   ```bash
   python populate_tours.py
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

8. **Access the application:**

   Open your web browser and navigate to `http://127.0.0.1:8000/` to view the home page.

   To access the Django admin interface, navigate to `http://127.0.0.1:8000/admin/` and log in with the admin credentials you set up.

## Notes

- **.gitignore**: This project uses a `.gitignore` file to exclude unnecessary files from the repository, such as the `env` directory (which contains your virtual environment) and other temporary files. Ensure your `.gitignore` is properly configured to prevent these files from being tracked in version control.

- **Admin Interface**: The Django admin interface is available to manage users, tours, and agents. Ensure you have the proper permissions when accessing this interface.

---

This `README.md` should provide clear guidance to users on how to set up and run the project locally. If there are any specific configurations or additional instructions needed, you can add those as well.