# Daily Docs App

This project is a Django application designed to help users document their daily tasks, reminders, and notes. It also includes functionality to send notifications via email or SMS.

## Features

- **Task Management**: Create, update, and delete daily tasks with due dates and completion status.
- **Reminders**: Set reminders for important tasks and receive notifications.
- **Notes**: Take and manage notes with associated metadata.
- **Notifications**: Send notifications via email or SMS for tasks and reminders.

## Project Structure

```
daily-docs-app
├── daily_docs
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── tasks
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
├── reminders
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
├── notes
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
├── notifications
│   ├── __init__.py
│   ├── email.py
│   ├── sms.py
│   └── utils.py
├── manage.py
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd daily-docs-app
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```
   python manage.py migrate
   ```

5. **Start the development server**:
   ```
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Use the admin interface to manage tasks, reminders, and notes.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.