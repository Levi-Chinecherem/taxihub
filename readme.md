
# TaxiHub - Online Campus Booking Taxi System

TaxiHub is an online platform designed to streamline and simplify the process of booking taxis on a university campus. This system provides a convenient way for students, faculty, and staff to book taxis for their transportation needs within the campus.

## Features

- **User Authentication**: Users can register, login, and manage their profiles.
- **Book Taxi**: Users can easily book a taxi for their desired pickup time.
- **View Bookings**: Users can view their booking history and upcoming rides.
- **Admin Panel**: Administrators have access to manage taxis, bookings, and user accounts.
- **Responsive Design**: The system is designed to work seamlessly on desktop and mobile devices.

## Technologies Used

- **Django**: Backend framework for building the web application.
- **Tailwind CSS**: Frontend framework for responsive and customizable styling.
- **SQLite**: Default database used for development.
- **Amazon S3**: For storing taxi images in production.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- Pipenv or virtual environment for managing dependencies.

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/Levi-Chinecherem/taxihub.git
   ```
2. Navigate to the project directory:

   ```bash
   cd taxihub
   ```
3. Create a virtual environment:

   ```bash
   python3 -m venv env
   ```
4. Activate the virtual environment:

   ```bash
   source env/bin/activate
   ```
5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```
7. Create a superuser (for accessing the admin panel):

   ```bash
   python manage.py createsuperuser
   ```
8. Start the development server:

   ```bash
   python manage.py runserver
   ```
9. Access the application at `http://localhost:8000/`

## Usage

- **Admin Panel**: Access the admin panel at `http://localhost:8000/admin/` to manage taxis, bookings, and users.
- **User Registration**: Users can register for an account on the registration page.
- **Login**: Users can login to their accounts to book taxis.
- **Book Taxi**: Once logged in, users can navigate to the "Book Taxi" page, select a taxi, and choose a pickup time.
- **View Bookings**: Users can view their past and upcoming bookings on the "My Bookings" page.

## Folder Structure

```
taxihub/
├── accounts/             # User authentication app
├── bookings/             # Booking management app
├── taxis/                # Taxi management app
├── static/               # Static files (CSS, images)
├── templates/            # HTML templates
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md             # Project README
```

## License

This project is licensed under the [MIT License](LICENSE).
