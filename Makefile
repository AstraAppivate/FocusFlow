install-frontend:
	cd frontend && npm install

install-backend:
	cd backend && source venv/bin/activate && pip install -r requirements.txt

run-backend:
	cd backend && source venv/bin/activate && python3 api/manage.py runserver

run-frontend:
	cd frontend && npm run dev

install: 
	install-frontend install-backend

superuser:
	cd backend && source venv/bin/activate && python3 api/manage.py createsuperuser

make-migration:
	cd backend && source venv/bin/activate && python3 api/manage.py makemigrations

migrate:
	cd backend && source venv/bin/activate && python3 api/manage.py migrate

create-app:
	cd backend && source venv/bin/activate && python3 api/manage.py startapp focusflow

test-all: 
	cd backend && source venv/bin/activate && python3 api/manage.py test

showmigrations-app: 
	cd backend && source venv/bin/activate && python3 api/manage.py showmigrations focusflow

check:
	cd backend && source venv/bin/activate && python3 api/manage.py check

flush:
	cd backend && source venv/bin/activate && python3 api/manage.py flush