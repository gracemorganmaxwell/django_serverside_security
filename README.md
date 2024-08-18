# GoNZ Web Application Development Tasks

This README outlines the step-by-step methodology for developing the GoNZ web application. Each task is designed to be completed sequentially, following best practices like shipping one feature at a time, using different branches for development, and coding in public. Additionally, Bootstrap will be integrated to enhance the visual appeal of the application.

## 1. Initial Setup

### 1.1 Set Up the Project Repository
- [x] **Create a new GitHub repository** 
- [x] **Clone the repository** to your local machine.
- [x] **Set up a `.gitignore` file** to exclude unnecessary files (e.g., environment settings, compiled files).
  - Best Practices: Use descriptive commit messages and push commits regularly. Keep the `main` branch clean by only merging well-tested features.

### 1.2 Set Up the Development Environment
- [x] **Set up a virtual environment** using `venv` or `pipenv`.
- [x] **Install Django and other dependencies** using `pip`.
- [x] **Initialize a Django project** and configure settings for local development.
  - Best Practices: Use environment variables for sensitive settings like `SECRET_KEY` and database credentials.

### 1.3 Integrate Bootstrap for Frontend Styling
- [x] **Add Bootstrap to your project** by including the Bootstrap CDN in your base HTML template:
  ```html
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  ```
- [x] **Ensure all views and templates use Bootstrap classes** to create a responsive and visually appealing UI.
  - Best Practices: Customize Bootstrap as needed by overriding its variables or adding custom CSS.

## 2. Create Django Apps for Modular Structure
  
### 2.1 Create the `tours` App
- [x] **Create a Django app named `tours`**:
  ```bash
  python manage.py startapp tours
  ```
  - This app will handle everything related to tours, such as listing all tours, viewing specific tour details, and tour management.

### 2.2 Create the `agents` App
- [x] **Create a Django app named `agents`**:
  ```bash
  python manage.py startapp agents
  ```
  - This app will manage agent-related data, including listing all agents and viewing details about a specific agent.

## 3. Authentication and User Management

### 3.1 Create the Admin Superuser
- [ ] **Run the Django management command** to create an admin superuser:
  ```bash
  python manage.py createsuperuser
  ```
- [ ] **Choose a secure and robust password** following best practices (e.g., at least 12 characters, mix of letters, numbers, and symbols).
  - Best Practices: Use a password manager to store admin credentials securely.

### 3.2 Create Users and User Groups
- [ ] **Define the user roles** (Administrator, Agent, Manager) in the Django admin panel.
- [ ] **Create user groups for each role** and assign appropriate permissions based on the department deputy list.
- [ ] **Create users** (e.g., Haywood Luby, Mariah Schumaker) and assign them to their respective groups.
  - Best Practices: Implement the principle of least privilege by giving each group only the permissions necessary for their role.

### 3.3 Set Up “Signup” and “Login” Views
- [ ] **Create Django views and forms** for user signup and login.
- [ ] **Ensure passwords are hashed** using Django’s built-in `make_password()` function.
- [ ] **Implement form validation** to prevent attacks like SQL injection.
- [ ] **Apply Bootstrap styling** to forms for a clean and user-friendly interface.
  - Best Practices: Use Django’s built-in authentication mechanisms to manage sessions securely.

## 4. URL and Navigation Setup

### 4.1 Define URL Patterns for Each App
- [ ] **Define URLs in each app’s `urls.py`**:
  - `gonztours`: `/` - Home page
  - `tours`: `/tours/` - List all tours, `/tours/<tour_id>/` - View details for a single tour
  - `agents`: `/agents/` - List all agents, `/agents/<agent_id>/` - View details for a single agent
- [ ] **Include the app URLs in the project’s main `urls.py`**.

### 4.2 Create Corresponding Views and Templates
- [ ] **Develop views for each URL** and ensure they render the correct template.
- [ ] **Use HTML templates** with Bootstrap for styling.
  - Best Practices: Reuse components like headers, footers, and navigation bars across templates.

### 4.3 Implement Navigation
- [ ] **Ensure the navigation bar includes links** to all relevant pages (home, tours, agents).
- [ ] **Implement breadcrumbs or a similar feature** to help users understand their location within the application.
- [ ] **Test the navigation** to ensure it is logical and intuitive.
  - Best Practices: Conduct user testing or gather feedback to improve navigation design.

## 5. Authorization and Access Control

### 5.1 Set Up User and Group Permissions
- [ ] **Assign permissions to the Administrator, Agent, and Manager groups** according to the requirements:
  - Administrators: Full permissions, including modifying users and tour data.
  - Agents: Modify their personal information and tours they are responsible for.
  - Managers: Modify the information of all agents and tours.
- [ ] **Use Django’s `UserPassesTestMixin` or `@permission_required` decorators** to enforce these permissions in views.
  - Best Practices: Regularly review and audit permissions to ensure they align with role responsibilities.

### 5.2 Restrict Access Based on Roles
- [ ] **Implement role-based access control (RBAC)** to ensure that only authorized users can access certain pages or perform specific actions.
- [ ] **Test access controls thoroughly** to ensure that unauthorized users cannot bypass restrictions.
  - Best Practices: Log access attempts and monitor for any suspicious activity.

## 6. Finalization and Deployment

### 6.1 Code Review and Merge
- [ ] **Open a pull request for each feature branch** once development is complete.
- [ ] **Conduct code reviews with peers** to ensure code quality and adherence to best practices.
- [ ] **Merge the feature branch into the `main` branch** after passing all tests.
  - Best Practices: Use tools like `pre-commit` hooks and continuous integration (CI) to automate code quality checks.

### 6.2 Deployment
- [ ] **Set up the production environment**, ensuring that settings are configured securely (e.g., `DEBUG=False`, proper database settings).
- [ ] **Deploy the application** using a reliable platform (e.g., Heroku, Vercel, Netlify).
- [ ] **Monitor the application post-deployment** to ensure it runs smoothly.
  - Best Practices: Implement automated deployment pipelines and monitoring tools like Sentry for error tracking.

### 6.3 Documentation
- [ ] **Document the setup, configuration, and deployment process**.
- [ ] **Include instructions for maintaining and updating the application**.
  - Best Practices: Maintain clear and concise documentation that can be easily followed by other developers.
