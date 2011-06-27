all: test

dependencies: should-dsl splinter flask

clean:
	@find . -name "*.pyc" -delete

flask:
	@python -c 'import flask' 2>/dev/null || pip install flask

splinter:
	@python -c 'import splinter' 2>/dev/null || pip install https://github.com/cobrateam/splinter/tarball/master

should-dsl:
	@python -c 'import should_dsl' 2>/dev/null || pip install https://github.com/hugobr/should-dsl/tarball/master

test: dependencies clean
	@echo "Running all tests..."
	./run_all_examples.py

