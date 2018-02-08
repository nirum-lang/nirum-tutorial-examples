NIRUM ?= nirum
PYVENV ?= python3 -m venv

run-counter-server: counter-server/venv/bin/nirum-server
	pushd counter-server/ && venv/bin/nirum-server -d 'counter_server:CounterImpl("/tmp/state")' && popd

test-counter-server: counter-server/venv/bin/nirum-server
	pushd counter-server/ && venv/bin/python -m unittest tests.py && popd

repl-counter-server: counter-server/venv/bin/nirum-server
	pushd counter-server/ && venv/bin/python && popd

counter-server/venv/bin/nirum-server: counter-server/venv/ counter-schema/out/
	counter-server/venv/bin/pip install nirum-http nirum-wsgi
	counter-server/venv/bin/pip install -e counter-schema/out/

counter-server/venv/:
	$(PYVENV) counter-server/venv/

counter-schema/out/:
	$(NIRUM) -t python -o counter-schema/out/ counter-schema/

clean:
	rm -rf counter-schema/out/
	rm -rf counter-server/venv/
