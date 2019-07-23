# Students
Student Account Service

for student accounting. It's based on the fact that the user has to register (in this way he gets access to add, edit and delete students, groups, exams, and may make changes to the journal). It is also possible to send a letter to the administrator. Exist student filtration. It's possible to view the site in three languages. Authorization via social networks.

## Installation

#### 1. Install dependencies:

```bash
pip install -r requirements.txt
```

#### 2. Make migrations:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

#### 3. Run sever:

```bash
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
