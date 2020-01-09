test:
	python3.7 -m unittest -v

build:
	sam build --use-container

install:
	pip install -r src/requirements.txt

run:
	sam local start-api 