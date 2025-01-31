all: install

install:
	pip install --upgrade pip
	pip install flake8
	pip install pyinstaller
	pip install -r requirements.txt

run:
	python main.py

lint:
	flake8 .

build:
	pyinstaller --onefile --name=certificate-generator main.py

clean:
	rm -rf build/ dist/ certificate-generator.spec
