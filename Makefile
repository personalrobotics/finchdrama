# Makefile to generate individual project pages.

# define all the generated pages
HTMLFILES = index.html

default: ${HTMLFILES}

%.html: %.rst
	rst2html5 --date --no-generator --stylesheet="css/basic.css" $< $@

clean:
	-rm ${HTMLFILES}
