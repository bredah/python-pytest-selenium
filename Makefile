setup:
	pip install -r requirements.txt

testAll:
	pytest -n auto test/ -v

test: testAll
