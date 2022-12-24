# Assignment

1. Postgres setup:
   - `docker pull postgres`
   - `docker run -itd -e POSTGRES_PASSWORD=text_scanner -e POSTGRES_USER=text_scanner_db -p 5432:5432 -v /data:/var/lib/postgresql/data --name postgresql postgres`
- This should start postgres. You can check if it is running by `docker ps`

2. Start a virtual environment and install the requirements:
   - `python3 -m venv venv`
   - `source venv/bin/activate`
   - `pip install -r requirements.txt`

3. Take care about the database:
   - `python manage.py makemigrations`
   - `python manage.py migrate`

4. Run the server:
   - `python manage.py runserver`

5. Go to `http://127.0.0.1:8000/scanner/signup` to signup.
6. Go to `http://127.0.0.1:8000/scanner/login` to login.
7. Go to `http://127.0.0.1:8000/scanner/upload/` to scan a document.
8. Go to `http://127.0.0.1:8000/scanner/list_scan` to see the list of scanned documents.