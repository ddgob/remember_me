# remember_me

1. Create and Activate the Conda Environment
```sh
conda env create -f environment.yaml
conda activate remember_me_env
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