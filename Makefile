all: install

install:
	pip install --upgrade pip
	pip install -r requirements.txt

run:
	python main.py

lint:
	flake8 .
