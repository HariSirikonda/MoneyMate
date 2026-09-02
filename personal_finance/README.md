# MoneyMate — Django Personal Finance Application

A simple personal finance tracker built with:
- Python + Django
- SQLite (Django's default database)
- HTML templates
- Bootstrap 5
- Django authentication

## Features

1. User registration/login/logout.
2. Add, edit and delete transactions.
3. Transaction attributes:
   - Name
   - Description
   - Type (Income/Expense)
   - Category
   - Amount
   - Date
4. Dashboard with clickable month blocks.
5. Month-specific financial analysis:
   - Total income
   - Total expenses
   - Net savings
   - Savings rate
   - Expense-category breakdown
   - Basic financial suggestions
6. Django admin support.

## Run the project

### 1. Create and activate a virtual environment

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Django

```bash
pip install -r requirements.txt
```

### 3. Create the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create an admin account (optional)

```bash
python manage.py createsuperuser
```

### 5. Start the server

```bash
python manage.py runserver
```

Open:
http://127.0.0.1:8000/

## Suggested next improvements

- Monthly budget limits
- Recurring transactions
- Search/filter transactions
- Date-range reports
- CSV export
- Savings goals
- Charts using Bootstrap-compatible HTML/CSS or a chart library
- Stronger production settings and environment variables
