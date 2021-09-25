all:
	@echo "Usage: make install | make play | make remove"
install:
	sudo bash install.sh
remove:
	sudo bash remove.sh
play:
	sudo python3 rpigpad.py
