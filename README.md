# Plant-watering-schedule-API

###### Simple Plant Watering Schedule API

## Key Features

- Implemented create, read, update functionality for Plant model
- Add a custom action that marks a plant as watered and updates its last_watered_date to the current date

## Installation
Ensure you have `Python 3` installed.

#### Clone the repo:
```bash
git clone https://github.com/KolBohdan/plant-watering-schedule-API
cd plant-watering-schedule-API
```
Specify Django root folder and settings as on screen:
![settings](https://github.com/user-attachments/assets/6392c6c1-5681-4af4-8bee-bb56855fd546)

For Windows users:
```bash
python -m venv venv
source venv/Scripts/activate
```
For macOS/Linux users:
```bash
python3 -m venv venv
source venv/bin/activate
```
Install requirements:
```bash
pip install -r requirements.txt
```
Migrate db and create user
```bash
python manage.py migrate
```
You can create admin user:
```bash
python manage.py createsuperuser
```
### Run server:
- For Windows users:
```bash
python manage.py runserver
```
- For macOS/Linux users:
```bash
python3 manage.py runserver
```

## API Endpoints:
```
Plants:

/api/plants/ - GET list of plants and POST method there;
/api/plants/{id}/ - GET detail book page and there PUT method;
/api/plants/{id}/mark - PUT method only available to update last_watered_date;
```
