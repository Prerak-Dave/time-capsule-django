# time-capsule-djangoProject: 
## Time Capsule Website

Overview:
Create a web application that allows users to create digital time capsules that will be unlocked in the future. Users can add messages, media (images, text, audio), or documents, and choose when they want the capsule to be opened (e.g., after 1 year, 5 years, or a specific date). This project will help you understand the core Django concepts you've learned so far and provide a seamless segue into concepts you'll cover next, like custom user models, logging, signals, Celery, and more.

1. Requirements Overview:

The Time Capsule Website will have the following core functionalities:

User Registration & Authentication: Users can sign up, log in, and manage their accounts.
Time Capsule Creation: Users can create new time capsules with various content types (messages, images, etc.).
Capsule Unlocking: Time capsules are locked until the specified unlock date.
Capsule Management: Users can view, edit, and delete their time capsules.
Notifications: Notify the user when a capsule is unlocked (via email or site notifications).
Admin Interface: Admin can manage time capsules, users, and notifications.
2. Detailed Feature Breakdown & Tasks:
2.1. User Authentication & Registration
Objective: Implement user authentication and a basic registration system.

Django Topics:

Models, Forms, Views (Function-based Views)
Templates (DTL)
Admin Interface (for user management)

Tasks:

Create a Custom User Model to store user data like email, username, and password.
Implement a User Registration Form that allows users to create accounts (email, password, confirm password).
Implement Login and Logout functionality.
Use Django's built-in User Authentication views or create custom views for user login/logout.
Use Django’s Authentication System to handle user login/logout functionality.

Concepts Covered:

Models (Custom User)
Forms (ModelForm for user registration)
Authentication system
Templates (login, registration pages)
Admin (user management)
2.2. Time Capsule Creation
Objective: Implement the core feature: users can create time capsules and lock them for a future date.

Django Topics:

Models, ORM, Forms
URL Dispatcher (reverse resolution)
Templates (form rendering, display content)

Tasks:

Create a TimeCapsule Model that includes:
Title (CharField)
Message (TextField)
Unlock Date (DateTimeField)
User (ForeignKey to User Model)
Media Files (ImageField or FileField for attachments)
Implement a TimeCapsule Form to allow users to submit time capsules (use a ModelForm).
On form submission, save the time capsule with the current date and unlock date.
Implement a Time Capsule View to display a list of time capsules the user has created. Use pagination to display the list in chunks.
Use Django’s reverse URL resolution to link to capsule details from the list.

Concepts Covered:

Models (TimeCapsule)
ORM (ForeignKey, DateTimeField)
Forms (ModelForm)
URL Dispatcher (reverse resolution)
Templates (form, list rendering)
2.3. Capsule Unlocking
Objective: Users should only be able to unlock their capsules after the set unlock date.

Django Topics:

ORM (filtering data based on date)
Views (conditional rendering)
Templates

Tasks:

In the Capsule Detail View, check if the current date is equal to or after the unlock date. If it is, display the capsule content (message, media). Otherwise, display a message that the capsule is still locked.
Use Django ORM’s filter and Q objects to retrieve capsules that can be unlocked.
Implement a Capsule Detail Page where the user can view the capsule details and check whether it is unlocked.

Concepts Covered:

ORM (filtering, Q objects)
Views (conditional rendering based on unlock date)
Templates (capsule detail page)
2.4. Capsule Management
Objective: Users should be able to view, edit, and delete their time capsules.

Django Topics:

Views, Forms
URL Dispatcher (reverse resolution)

Tasks:

Implement views for editing and deleting capsules (e.g., edit_capsule, delete_capsule).
Use Django forms to handle editing the message and media fields.
Implement a confirmation page before deleting a capsule.
Provide URL links to edit and delete capsules from the list view.

Concepts Covered:

Views (CRUD operations)
Forms (edit, delete)
URL Dispatcher (reverse resolution)
2.5. Admin Interface
Objective: Implement an admin interface to manage users and time capsules.

Django Topics:

Admin interface

Tasks:

Create custom admin views for the TimeCapsule Model and User Model.
Implement filters and search functionality for easier management (e.g., filter capsules by unlock date or user).
Ensure that admins can view, edit, and delete time capsules, even those belonging to users.

Concepts Covered:

Admin (ModelAdmin, list_display, search_fields)
2.6. Notifications
Objective: Notify users when a capsule is unlocked.

Django Topics:

Signals (user registration, capsule unlock)
Email integration

Tasks:

Use Django signals to trigger an email when a time capsule is unlocked or when a user registers.
Implement an email notification system using Django’s send_mail function.
Create a notification system that shows messages on the user’s dashboard when a capsule is unlocked.

Concepts Covered:

Signals (post-save, pre-save)
Email (send_mail, email templates)
Templates (rendering notifications)
3. Advanced Topics (Next Steps)
3.1. Logging
Implement logging to capture important events (e.g., when a user creates or unlocks a time capsule, when there are errors, etc.).
3.2. Background Task with Celery
Celery: Automate background tasks, such as sending email notifications at specific times (e.g., the day a time capsule unlocks).
3.3. Scheduled Tasks with Celery Beat
Use Celery Beat to schedule tasks, such as sending periodic reminders to users about upcoming capsule unlocks.