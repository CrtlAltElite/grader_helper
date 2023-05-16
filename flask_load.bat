python -m venv venv
CALL venv\Scripts\activate.bat
pip install -r requirements.txt
flask db init
flask db migrate
flask db upgrade
flask run
deactivate