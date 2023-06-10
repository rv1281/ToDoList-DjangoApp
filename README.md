
# ToDoList-DjangoApp

This is a basic Django-based application that allows users to sign up, log in, add task in the to-do List, and mark the tasks complete/incomplete.

The application uses HTML and CSS along with Bootstrap for designing the user interface. Bootstrap provides a responsive and user-friendly design which makes the application easily accessible on various devices and screen sizes.


## Tech Stack

The Django Todo List app is built using the following technologies:

- Python: The core programming language used for developing the backend logic and implementing the Django framework.

- Django: A high-level Python web framework that provides a solid foundation for building web applications. Django simplifies the process of developing robust, scalable, and secure web applications.

- Django REST Framework: An extension to Django that enables the development of RESTful APIs. It provides powerful tools and serializers to build APIs for seamless communication between the frontend and backend.

- SQLite: A lightweight and serverless relational database management system (RDBMS) used as the default database for Django development. SQLite is easy to set up and is well-suited for small to medium-sized projects.

- HTML: The standard markup language for creating web pages. HTML is used for structuring the content and layout of the Todo List app's frontend.

- Bootstrap: A popular front-end framework that provides a set of pre-designed components and responsive CSS classes. Bootstrap simplifies the process of creating visually appealing and mobile-friendly web pages.

## Installation

To install and set up the Django Todo List app, follow these steps:

1. Clone the repository:

```bash
    $ git clone https://github.com/your-username/django-todo-list.git
```
Replace 'your-username' with your actual GitHub username.

2. Navigate to the project directory:

```bash
    $ cd django-todo-list
```

3. Set up a virtual environment (optional, but recommended):

```bash
    $ python -m venv myenv
    $ source myenv/bin/activate  # For Linux/macOS
    $ myenv\Scripts\activate  # For Windows
```
Activating the virtual environment isolates the project dependencies from your system's global Python environment.

4. Install the project dependencies:

```bash
    $ pip install -r requirements.txt
```
This command will install all the necessary Python packages and libraries required for the Django Todo List app to function correctly.

5. Make the migrations to the database:

```bash
    $ python manage.py makemigrations
```

6. Apply the database migrations:

```bash
    $ python manage.py migrate
```
This command will create the necessary database tables and set up the initial database schema.

7. Start the development server:

```bash
    $ python manage.py runserver
```

The development server will start running, and you can access the Todo List app in your web browser at `http://localhost:8000`.

Note: If port 8000 is already in use, you can specify a different port by appending the desired port number to the runserver command (e.g., python manage.py runserver 8080).

## Usage

Once the development server is running and you have accessed the Todo List app in your web browser at `http://localhost:8000`, you can follow these steps to interact with the app:

1. Register an account or log in: If you are using the app for the first time, click on the "Sign Up" link to create a new account. Fill in the required details such as username, email, and password. If you already have an account, click on the "Log In" link and enter your credentials to log in.

2. View the task list: After logging in, you will be redirected to the task list page. Here, you can see all your tasks displayed in an organized manner.

3. Add a new task: To create a new task, simply add the title, check box for completed task or else simply add the task by clicking "Add Item"

4. Update task status: To mark a task as complete or incomplete, click on update button corresponding to the task, here you can update the status of the task and also name of the task.

5. Delete a task: If you want to remove a task from the list, find the task in the task list and simply click the "Delete" button representing delete functionality. You'll be redirected to confirmation pagem, click yes/no according to requirement. Be cautious as this action is irreversible.

6. Log out: When you are done using the app, make sure to log out to secure your account. Click on log out.

The Django Todo List app provides a user-friendly interface to manage your tasks efficiently.

## API Reference

The Django Todo List app provides a RESTful API using the Django REST Framework. You can interact with the following API endpoints:

#### Get all items

```http
    GET api/todo/ [name='todo_list']
```
Retrieves a list of all tasks.

#### Create Item

```http
    POST api/todo/create/ [name='create_todo']
```
Creates a new task. Send a POST request with the task details in the request body.

#### Update Item

```http
    PUT api/todo/update/<int:pk>/ [name='update_todo']
```
Updates a specific task by its ID. Send a PUT request with the updated task details in the request body.

#### Delete Item

```http
    DELETE api/todo/delete/<int:pk>/ [name='delete_todo']
```
Deletes a specific task by its ID.

## Django Dashboard

The Django Todo List app includes a built-in Django admin dashboard that provides an interface for managing the application's data and configurations. You can access the Django admin dashboard using the following steps:

1. Start the development server:

```bash
    $ python manage.py runserver
```
2. Open your web browser and navigate to `http://localhost:8000/admin.`

3. Enter the superuser credentials:

- Username: admin
- Password: admin

These are the default credentials provided as an example. You should change the superuser credentials to enhance the security of your application.

4. Once logged in, you will have access to the Django admin dashboard. From here, you can perform various administrative tasks such as managing users, handling database models, and configuring site settings.