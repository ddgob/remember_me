# remember_me

## Introduction

This project is being created to help users to remember their tasks and appointments through whatsapp audios. Here we will be implementing the Whisper model to convert speech to text and then create embeddings for the tasks usign TF_IDF and allow the user to search the tasks using cosign similarity. The user will also automatically be reminded of task that have due dates!

## How to get the server up and running

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
