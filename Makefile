install:
	pip install -e .

test:
	pytest tests/

format:
	black pyalgolab/ cli.py tests/

lint:
	flake8 pyalgolab/ cli.py tests/
