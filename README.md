The Campus Lost & Found Management System is a Django-based web application designed to help students and campus users report, search, and manage lost and found items.

Users can register, log in, and log out securely. After logging in, a user can create a lost or found report by providing the item name, type, category, description, location, date, contact information, and optional image.

The system provides complete CRUD (Create, Read, Update, Delete) functionality. Users can view all reports, view individual report details, edit their own reports, and delete their own reports. Users cannot modify or delete reports created by other users.

The system also provides search and filtering based on item name, category, Lost/Found type, and status. Each report has an Active or Resolved status, and the report owner can mark their report as resolved.

The project uses Django Forms for user registration and report submission, Django Templates with template inheritance for the user interface, and the Django ORM to store and manage report data in PostgreSQL. Django's authentication system controls user access, while messages provide feedback after actions such as creating, updating, deleting, and resolving reports.

A custom middleware is also implemented to log the username, HTTP request method, requested URL/path, and request processing time in the terminal.

The main purpose of this project is to demonstrate practical use of Forms, Templates, User Interaction, CRUD operations, Authentication, Middleware, Django ORM, PostgreSQL, and Messages in a real-world Django application.
