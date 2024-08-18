Certainly! Here’s how the updated README could look with the new section for setting up user roles and permissions, followed by the steps for setting up the tour and agent views:

---

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
- [x] **Run the Django management command** to create an admin superuser:
  ```bash
  python manage.py createsuperuser
  ```
- [x] **Choose a secure and robust password** following best practices (e.g., at least 12 characters, mix of letters, numbers, and symbols).
  - Best Practices: Use a password manager to store admin credentials securely.

### 3.2 Set Up User Roles and Permissions
Before setting up the views, it’s essential to establish the user roles and permissions within the Django admin panel:

#### Define User Roles:
- **Administrators**: Have full permissions, including modifying any users and tour data.
- **Agents**: Can provide and modify their personal information, add tours, and modify tours they manage.
- **Managers**: Can modify the information of all agents and tours.

#### Create User Groups and Assign Permissions:
- [x] **Define the user roles** (Administrator, Agent, Manager) in the Django admin panel.
- [x] **Create user groups for each role** and assign appropriate permissions based on the department deputy list:
  - **Administrators**: Haywood Luby, Mariah Schumaker
  - **Agents**: Marty Schaeffer, Beryl Gauer, Cathrine Heckstall, Dane Ratliff
  - **Managers**: Halina Dabbs, Andres Peltier

#### Assign Permissions:

1. **Administrators:**
   - **Full Permissions**: 
     - **Log Entry**: `can add`, `can change`, `can view`, `can delete`
     - **Group**: `can add`, `can change`, `can view`, `can delete`
     - **Permission**: `can add`, `can change`, `can view`, `can delete`
     - **Session**: `can add`, `can change`, `can view`, `can delete`
     - **User**: `can add`, `can change`, `can view`, `can delete`
     - **Content Type**: `can add`, `can change`, `can view`, `can delete`

2. **Managers:**
   - **Log Entry**: `can view`
   - **Session**: `can view`, `can change`
   - **User**: `can add`, `can change`, `can view`, `can delete`
   - **No permissions** for managing groups, permissions, or content types.

3. **Agents:**
   - **Log Entry**: `can view`
   - **Session**: `can view`
   - **User**: `can change` (only for their own profile), `can view`
   - **No permissions** for managing groups, permissions, or content types.

- [x] **Create users** based on the defined roles (e.g., Haywood Luby, Mariah Schumaker) and assign them to their respective groups.
  - Best Practices: Implement the principle of least privilege by giving each group only the permissions necessary for their role.

By completing these steps, the user management system will be set up with appropriate roles and permissions, ensuring that users have access only to the resources and actions necessary for their roles.

### 3.3 Set Up “Signup” and “Login” Views
- [ ] **Create Django views and forms** for user signup and login.
- [ ] **Ensure passwords are hashed** using Django’s built-in `make_password()` function.
- [ ] **Implement form validation** to prevent attacks like SQL injection.
- [ ] **Apply Bootstrap styling** to forms for a clean and user-friendly interface.
  - Best Practices: Use Django’s built-in authentication mechanisms to manage sessions securely.

### 3.4 Authentication and User Management: Manual Testing Tasks

Manually test the various endpoints to ensure that everything is functioning as expected. Below is a list of endpoints to test:

#### 1. Admin Interface
- **Admin Login Page:**
  - **URL:** `/admin/`
  - **Description:** Access the Django admin interface login page to authenticate as an admin.
  - **Task:** Verify that the login page loads correctly and that you can log in with admin credentials.

- **Admin Dashboard:**
  - **URL:** `/admin/`
  - **Description:** Once logged in, this dashboard allows management of models registered with the admin interface.
  - **Task:** Ensure that the admin dashboard is accessible and displays all registered models.

#### 2. Home Page
- **Home Page:**
  - **URL:** `/home/`
  - **Description:** The main landing page for GoNZ Tours.
  - **Task:** Confirm that the home page loads successfully and displays the expected content.

#### 3. Agents Management
- **Agent List:**
  - **URL:** `/agents/`
  - **Description:** Lists all agents associated with GoNZ Tours.
  - **Task:** Verify that the list of agents is displayed correctly.

- **Agent Detail:**
  - **URL:** `/agents/<agent_id>/`
  - **Description:** Displays detailed information for a specific agent.
  - **Task:** Replace `<agent_id>` with a valid agent ID and ensure that the detail page displays the correct information for that agent.

#### 4. Tours Management
- **Tour List:**
  - **URL:** `/tours/`
  - **Description:** Displays a list of all available tours.
  - **Task:** Ensure that the list of tours is displayed correctly.

- **Tour Detail:**
  - **URL:** `/tours/<tour_id>/`
  - **Description:** Displays detailed information for a specific tour.
  - **Task:** Replace `<tour_id>` with a valid tour ID and confirm that the detail page displays the correct information for that tour.

#### 5. Static Files Access
- **Static Files:**
  - **URL:** `/static/<path_to_static_file>`
  - **Description:** Access static files like CSS, JavaScript, or images.
  - **Task:** Replace `<path_to_static_file>` with the relative path to a specific static file and verify that the file loads correctly.

### Testing Checklist
- [ ] Confirm the admin login page is accessible and functional.
- [ ] Ensure the admin dashboard displays all registered models.
- [ ] Verify the home page loads with the correct content.
- [ ] Confirm that the agent list and detail pages display correctly.
- [ ] Ensure that the tour list and detail pages are functioning as expected.
- [ ] Test access to static files to verify they are being served properly.

By completing the above tasks, you can ensure that your authentication, user management, and overall application are working as intended.

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
