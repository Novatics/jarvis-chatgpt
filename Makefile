all: build_docker

build_docker:
	docker build -t jarvis:latest . 
	./scripts/set_alias.sh

build_python:
	pip install -r requirements.txt
	./scripts/set_alias.sh python
