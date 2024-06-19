# remember_me

1. Create and Activate a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate
```

2. Install Dependencies
```sh
pip install -r requirements.txt
```

3. Apply Migrations
```sh
python manage.py migrate
```

4. Create a Superuser
```sh
python manage.py createsuperuser
```

5. Run the Development Server
```sh
python manage.py runserver
```