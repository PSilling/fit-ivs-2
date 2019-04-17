.PHONY: all run pack doc install test clean

all: *.py
	python3 -m compileall $^

run: gui_calc.py
	python3 gui_calc.py

test: math_lib_test.py
	python3 math_lib_test.py

doc: Doxyfile
	cd .. && rm -rf doc
	cd .. && doxygen src/$^

clean:
	rm -rf __pycache__

pack: doc clean
	cd .. && mkdir tmp && cd tmp && mkdir src && mkdir install && mkdir repo
	cp -r ../doc ../tmp/doc
	cp -r . ../tmp/src
	#cp -r ../installer ../tmp/install
	cd .. && rsync -Rr ./* ./tmp/repo
	rm -rf ../tmp/repo/tmp
	cd ../tmp && zip -qr ../xsilli01_xmaste02_xschme00_xradan00.zip ./*
	rm -rf ../tmp
