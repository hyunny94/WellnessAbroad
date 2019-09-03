pip3 install --upgrade pip3
pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd googleauth
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
