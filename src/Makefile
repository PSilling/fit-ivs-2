.PHONY: all run test doc clean cleanall pack wispack install uninstall

TEST_SRC_FILES := $(wildcard *_test.py)
SRC_FILES := $(filter-out $(TEST_SRC_FILES), $(wildcard *.py))
MATH_FILES := $(wildcard math*.py)
WIS_DOC_FILES = dokumentace.pdf odevzdani.txt hodnoceni.txt
TEAM_PACK_NAME = xsilli01_xmaste02_xschme00_xradan00

vpath %.pdf ..
vpath %.sh ../installer
vpath %.txt ..

all: run
run: $(SRC_FILES)
	python3 -m gui_calc

test: $(MATH_FILES)
	python3 -m math_lib_test

profile: $(SRC_FILES)
	python3 -m deviation

doc: Doxyfile $(SRC_FILES) $(TEST_SRC_FILES)
	cd .. && rm -rf doc
	doxygen
	mv doc ../doc

clean:
	rm -rf __pycache__ ../../tmp

cleanall:
	rm -rf __pycache__ ../doc ../../tmp ../../$(TEAM_PACK_NAME).zip ../../$(TEAM_PACK_NAME)_wis.zip

pack: doc clean $(SRC_FILES) $(TEST_SRC_FILES)
	mkdir -p ../../tmp/doc && cp -a ../doc/. ../../tmp/doc
	mkdir -p ../../tmp/install && cp -a ../installer/. ../../tmp/install
	mkdir -p ../../tmp/repo &&  cp -a ../. ../../tmp/repo
	rm -rf ../../tmp/repo/doc ../../tmp/repo/venv
	rm -rf ../../tmp/repo/Pipfile ../../tmp/repo/Pipfile.lock ../../tmp/repo/.idea
	cd ../../tmp && zip -qr ../$(TEAM_PACK_NAME).zip .

wispack: clean $(WIS_DOC_FILES) $(SRC_FILES) $(TEST_SRC_FILES)
	mkdir -p ../../tmp && cp ../hodnoceni.txt ../../tmp
	mkdir -p ../../tmp/src/ && cp ./*.py ../../tmp/src
	cp ../dokumentace.pdf ../../tmp
	cp ../odevzdani.txt ../../tmp
	cd ../../tmp && zip -qr ../$(TEAM_PACK_NAME)_wis.zip .

install: install.sh $(SRC_FILES) $(TEST_SRC_FILES)
	bash ../installer/install.sh

uninstall: uninstall.sh
	bash ../installer/uninstall.sh
