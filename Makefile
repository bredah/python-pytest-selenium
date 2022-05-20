setup:
	pip install -r requirements.txt

testAll:
	pytest -n 3 test/

test: testAll
