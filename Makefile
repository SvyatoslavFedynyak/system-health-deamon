.PHONY: build
build:
	sudo python3.8 setup.py sdist
env:
	virtualenv env ; ./env/bin/python setup.py install
docker:
	docker build -t daemon --no-cache . && docker run --name daemon -it -d --rm daemon && echo "\nTo enter container tap\ndocker exec -it daemon bash"
clean:
	docker stop `docker ps -q` ; docker rm `docker ps -qa` ; docker image prune -f
