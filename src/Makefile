.PHONY: all setup run test doc clean cleanall pack wispack install uninstall

TEST_SRC_FILES := $(wildcard *_test.py)
SRC_FILES := $(filter-out $(TEST_SRC_FILES), $(wildcard *.py))
MATH_FILES := $(wildcard math*.py)
WIS_DOC_FILES = dokumentace.pdf odevzdani.txt hodnoceni.txt
TEAM_PACK_NAME = xsilli01_xmaste02_xschme00_xradan00

vpath %.pdf ..
vpath %.sh ../installer
vpath %.txt ..

# target all does not compile (Python), but installs all dependencies necessary for a later installation
# note that Python (v2 and v3) should both be pre-installed on later versions of Ubuntu
all: setup
setup: $(SRC_FILES)
	sudo apt-get -y update
	sudo apt-get install python3-pip
	sudo -H pip3 install pyqt5
	sudo -H pip3 install pyinstaller

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
	rm -rf __pycache__ ../doc ../../$(TEAM_PACK_NAME) doxygen_warn_logfile.log

cleanall:
	rm -rf __pycache__ ../doc ../../$(TEAM_PACK_NAME) ../../$(TEAM_PACK_NAME).zip
	rm -rf ../../$(TEAM_PACK_NAME)_wis.zip doxygen_warn_logfile.log

pack: clean doc $(SRC_FILES) $(TEST_SRC_FILES)
	mkdir -p ../../$(TEAM_PACK_NAME)/doc && cp -a ../doc/. ../../$(TEAM_PACK_NAME)/doc
	mkdir -p ../../$(TEAM_PACK_NAME)/install && cp -a ../installer/. ../../$(TEAM_PACK_NAME)/install
	mkdir -p ../../$(TEAM_PACK_NAME)/repo &&  cp -a ../. ../../$(TEAM_PACK_NAME)/repo
	rm -rf ../../$(TEAM_PACK_NAME)/repo/doc ../../$(TEAM_PACK_NAME)/repo/venv
	rm -rf ../../$(TEAM_PACK_NAME)/repo/Pipfile ../../$(TEAM_PACK_NAME)/repo/Pipfile.lock
	rm -rf ../../$(TEAM_PACK_NAME)/repo/.idea  ../../$(TEAM_PACK_NAME)/repo/src/doxygen_warn_logfile.log
	cd ../.. && zip -qr $(TEAM_PACK_NAME).zip $(TEAM_PACK_NAME)

wispack: clean $(WIS_DOC_FILES) $(SRC_FILES) $(TEST_SRC_FILES)
	mkdir -p ../../$(TEAM_PACK_NAME) && cp ../hodnoceni.txt ../../$(TEAM_PACK_NAME)
	mkdir -p ../../$(TEAM_PACK_NAME)/src/ && cp ./*.py ../../$(TEAM_PACK_NAME)/src
	cp ../dokumentace.pdf ../../$(TEAM_PACK_NAME)
	cp ../odevzdani.txt ../../$(TEAM_PACK_NAME)
	cd ../.. && zip -qr $(TEAM_PACK_NAME)_wis.zip $(TEAM_PACK_NAME)

install: install.sh $(SRC_FILES) $(TEST_SRC_FILES)
	bash ../installer/install.sh

uninstall: uninstall.sh
	bash ../installer/uninstall.sh
