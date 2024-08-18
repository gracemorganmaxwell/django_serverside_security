# GoNZ Web Application Development Tasks

This README outlines the step-by-step methodology for developing the GoNZ web application based on the assignment outline. Each task is designed to be completed sequentially, following best practices like shipping one feature at a time, using different branches for development, and coding in public.

## 1. Initial Setup

### 1.1 Set Up the Project Repository
- [x] **Create a new GitHub repository**
- [x] **Clone the repository** to my local machine.
- [x] **Set up a `.gitignore` file** to exclude unnecessary files (e.g., environment settings, compiled files).
  - Best Practices: Use descriptive commit messages and push commits regularly. Keep the `main` branch clean by only merging well-tested features.

### 1.2 Set Up the Development Environment
- [ ] **Set up a virtual environment** using `venv`, called env. 
- [ ] **Install Django and other dependencies** using `pip3`.
- [ ] **Initialise a Django project** and configure settings for local development.
  - Best Practices: Use environment variables for sensitive settings like `SECRET_KEY` and database credentials.

### 1.3 Integrate Bootstrap for Frontend Styling (not essential - added bonus)
- [ ] **Add Bootstrap to your project** by including the Bootstrap CDN in your base HTML template:
  ```html
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
- [ ] Make sure all views and templates use Bootstrap classes to create a responsive and visually appealing UI.
- [ ] Best Practices: Customize Bootstrap as needed by overriding its variables or adding custom CSS.

## 2. Authentication and User Management

### 2.1 Create the Admin Superuser
- [ ] **Run the Django management command** to create an admin superuser:
  ```bash
  python manage.py createsuperuser
  ```
- [ ] **Choose a secure and robust password** following best practices (e.g., at least 12 characters, a mix of letters, numbers, and symbols).
  - Best Practices: Use a password manager to store admin credentials securely.

### 2.2 Create Users and User Groups
- [ ] **Define the user roles** (Administrator, Agent, Manager) in the Django admin panel.
- [ ] **Create user groups for each role** and assign appropriate permissions based on the department deputy list.
- [ ] **Create users** (e.g., Haywood Luby, Mariah Schumaker) and assign them to their respective groups.
  - Best Practices: Implement the principle of least privilege by giving each group only the permissions necessary for their role.

### 2.3 Set Up “Signup” and “Login” Views
- [ ] **Create Django views and forms** for user signup and login.
- [ ] **Ensure passwords are hashed** using Django’s built-in `make_password()` function.
- [ ] **Implement form validation** to prevent attacks like SQL injection.
  - Best Practices: Use Django’s built-in authentication mechanisms to manage sessions securely.

## 3. URL and Navigation Setup

### 3.1 Create the Required URLs
- [ ] **Define URLs in `urls.py`** for the following paths:
  - `/` - Home page
  - `/tours/` - List all tours
  - `/tours/<tour_id>/` - View details for a single tour
  - `/agents/` - List all agents
  - `/agents/<agent_id>/` - View details for a single agent
- [ ] **Create corresponding views and templates** for each URL.
  - Best Practices: Follow the DRY (Don't Repeat Yourself) principle by reusing common template components (e.g., navigation bars, footers).

### 3.2 Implement Navigation
- [ ] **Ensure the navigation bar includes links** to all relevant pages (home, tours, agents).
- [ ] **Implement breadcrumbs or a similar feature** to help users understand their location within the application.
- [ ] **Test the navigation** to ensure it is logical and intuitive.
  - Best Practices: Conduct user testing or gather feedback to improve navigation design.

## 4. Authorization and Access Control

### 4.1 Set Up User and Group Permissions
- [ ] **Assign permissions to the Administrator, Agent, and Manager groups** according to the requirements:
  - Administrators: Full permissions, including modifying users and tour data.
  - Agents: Modify the personal information and tours they are responsible for.
  - Managers: Modify the information of all agents and tours.
- [ ] **Use Django’s `UserPassesTestMixin` or `@permission_required` decorators** to enforce these permissions in views.
  - Best Practices: Regularly review and audit permissions to ensure they align with role responsibilities.

### 4.2 Restrict Access Based on Roles
- [ ] **Implement role-based access control (RBAC)** to ensure only authorised users can access certain pages or perform specific actions.
- [ ] **Test access controls thoroughly** to ensure that unauthorized users cannot bypass restrictions.
  - Best Practices: Log access attempts and monitor for any suspicious activity.

## 5. Finalization and Deployment

### 5.1 Code Review and Merge
- [ ] **Open a pull request for each feature branch** once development is complete.
- [ ] **Conduct code reviews with peers(aka me)** to ensure code quality and adherence to best practices.
- [ ] **Merge the feature branch into the `main` branch** after passing all tests.
  - Best Practices: Use tools like `pre-commit` hooks and continuous integration (CI) to automate code quality checks.

### 5.2 Deployment
- [ ] **Set up the production environment**, ensuring that settings are configured securely (e.g., `DEBUG=False`, proper database settings).
- [ ] **Deploy the application** using a reliable platform like either Heroku, AWS, or DigitalOcean.
- [ ] **Monitor the application post-deployment** to ensure it runs smoothly.
  - Best Practices: Implement automated deployment pipelines and monitoring tools like Sentry for error tracking.

### 5.3 Documentation
- [ ] **Document the setup, configuration, and deployment process**.
- [ ] **Include instructions for maintaining and updating the application**.
  - Best Practices: Maintain clear and concise documentation that other developers can easily follow.

