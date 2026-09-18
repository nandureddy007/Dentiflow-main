# Free PythonAnywhere Deployment

PythonAnywhere is the recommended free host for the Flask demo because its filesystem can preserve the local SQLite database and uploads.

## 1. Create the web app

1. Create a free account at https://www.pythonanywhere.com/.
2. Open a Bash console.
3. Clone the repository:

```bash
git clone https://github.com/nandureddy007/Dentiflow-main.git
cd Dentiflow-main
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python init_db.py
```

## 2. Configure the Web tab

Create a new **Manual configuration** web app using Python 3.11.

Set the virtualenv path to:

```text
/home/<username>/Dentiflow-main/venv
```

Set the WSGI file contents to:

```python
import os
import sys

project_root = "/home/<username>/Dentiflow-main"
if project_root not in sys.path:
    sys.path.insert(0, project_root)

os.environ.setdefault("APP_ENV", "production")
os.environ.setdefault("FLASK_DEBUG", "0")
os.environ.setdefault("SESSION_COOKIE_SECURE", "0")

from app import app as application
```

Alternatively, point the WSGI file at the committed `pythonanywhere_wsgi.py` after replacing `<username>` with the PythonAnywhere username in its project path.

## 3. Production settings

Set a strong `SECRET_KEY` in the WSGI file or PythonAnywhere environment configuration. Do not commit secrets.

Leave `DATABASE_URL` unset for the free demo so Dentiflow uses the persistent PythonAnywhere SQLite file:

```text
sqlite:///dentiflow.db
```

Do not run demo reset commands against a live deployment.

## 4. Firebase and uploads

For Firebase Admin, configure `FIREBASE_PROJECT_ID`, `FIREBASE_STORAGE_BUCKET`, and the service-account credentials through PythonAnywhere environment settings. Do not upload or commit `firebase-service-account.json`.

Firebase Storage is recommended for patient files. Local uploads work for a small demo but should be backed up.

## 5. Reload and test

After saving the Web tab, click **Reload** and check:

- `/`
- `/login`
- `/dashboard`
- `/treatment-plans`
- `/api/health`

The free service is suitable for demonstration and light use. SQLite is not intended for high-concurrency production workloads.
