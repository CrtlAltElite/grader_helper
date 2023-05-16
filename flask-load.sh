python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
flask db init
flask db migrate
flask db upgrade
deactivate