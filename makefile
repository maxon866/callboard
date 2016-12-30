server:
	venv/bin/python3 manage.py runserver

shell:
	venv/bin/python3 manage.py shell_plus --ipython

save_dependencies:
	pip3 freeze > requirements.txt

# tests
func_test:
	venv/bin/python3 manage.py test functional_tests

current_func_test:
	venv/bin/python3 manage.py test functional_tests.test_counter

tests:
	venv/bin/python3 manage.py test adverts

# DB
migrate:
	venv/bin/python3 manage.py migrate

makemigration:
	venv/bin/python3 manage.py makemigrations

# setup
venv/bin/activate:
	virtualenv --no-site-packages -p python3.4 venv

setup: venv/bin/activate requirements.txt
	. venv/bin/activate; pip install -Ur requirements.txt

jenk:
	# venv/bin/python3 manage.py jenkins adverts
	venv/bin/python3 manage.py jenkins --enable-coverage adverts
	# venv/bin/python3 manage.py jenkins --enable-coverage adverts