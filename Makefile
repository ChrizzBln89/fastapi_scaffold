.PHONY: start_fastapi

PORT ?= 8000

start_fastapi:
	uvicorn main:app --reload --port ${PORT} --host 0.0.0.0

.PHONY: push_to_github

push_to_github:
	git add .
	git commit -m "`date`"
	git push origin main

.PHONY: start_locust

start_locust:
	locust -f locustfile.py
