all: ./dist/main/main
	sudo cp ./dist/main/main /usr/bin/say
	sudo cp -r ./dist/main/_internal/ /usr/bin
./dist/main/main:
	pyinstaller main.py
clear:
	rm -rf ./build
	rm -rf ./dist
