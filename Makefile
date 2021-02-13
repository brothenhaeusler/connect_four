all:
	pytest
	pandoc doc/documentation.md -o doc/documentation.html
	pandoc doc/documentation.md -o doc/documentation.pdf
	echo 'test'
	#other commands here
	
