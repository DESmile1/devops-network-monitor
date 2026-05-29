.PHONY: run test

run:
		python3 monitor.py

test:
		python3 -m unittest discover -s . -p "*tester.py"