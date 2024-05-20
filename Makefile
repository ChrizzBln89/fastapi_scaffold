.PHONY: start_fastapi

PORT ?= 8000

start_fastapi:
	uvicorn main:app --reload --port ${PORT} --host 0.0.0.0
