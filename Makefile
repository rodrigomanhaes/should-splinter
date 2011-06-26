all: test

dependencies: should-dsl splinter specloud flask coverage

clean:
	@find . -name "*.pyc" -delete

specloud:
	@python -c 'import specloud' 2>/dev/null || pip install specloud

flask:
	@python -c 'import flask' 2>/dev/null || pip install flask

splinter:
	@python -c 'import splinter' 2>/dev/null || pip install https://github.com/cobrateam/splinter/tarball/master

should-dsl:
	@python -c 'import should_dsl' 2>/dev/null || pip install https://github.com/hugobr/should-dsl/tarball/master

coverage:
	@python -c 'import coverage' 2>/dev/null || pip install coverage

which = 'tests'

test: dependencies clean
	@echo "Running all tests..."
	specloud --nocapture --with-coverage --cover-erase --cover-inclusive --cover-package=should_web --tests=$(which)

