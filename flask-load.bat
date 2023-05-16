python -m venv venv
CALL venv\Scripts\activate.bat
echo hello
pip install -r requirements.txt
flask db init
flask db migrate
flask db upgrade
deactivate