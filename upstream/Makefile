NAME=heisenbug-kde-theme
VERSION=$(shell sed -n -r -e '/Version:/s/[[:alpha:]]+:[[:space:]]+//p' ${NAME}.spec)
SVNTAG="${NAME}-${VERSION}"

tag:
	svn copy "$(shell svn info | grep ^URL: | sed -e 's/[^:]*: //')" \
	"$(shell svn info | grep Root: | sed -e 's/[^:]*: //')/tags/$(SVNTAG)" \
	-m "tagged release $(VERSION)"
                                          
archive:
	rm -rf /tmp/${NAME}
	cd /tmp; svn export --force $(shell svn info | grep Root: | sed -e 's/[^:]*: //')/tags/$(SVNTAG) /tmp/${NAME}-${VERSION}
	cd /tmp; tar cvjf ${NAME}-${VERSION}.tar.bz2 ${NAME}-${VERSION}
	mv /tmp/${NAME}-${VERSION}.tar.bz2 .
	rm -rf /tmp/${NAME}
	echo "The archive is in ${NAME}-${VERSION}.tar.bz2"

snapshot:
	rm -rf /tmp/${NAME}
	cd /tmp; svn export --force $(shell svn info | grep Root: | sed -e 's/[^:]*: //')/trunk/$(NAME) /tmp/${NAME}-${VERSION}
	cd /tmp; tar cvjf ${NAME}-${VERSION}.tar.bz2 ${NAME}-${VERSION}
	mv /tmp/${NAME}-${VERSION}.tar.bz2 .
	rm -rf /tmp/${NAME}
	echo "The archive is in ${NAME}-${VERSION}.tar.bz2"

upload:
	scp ${NAME}-${VERSION}.tar.bz2 fedorahosted.org:fedora-kde-artwork

release: tag archive upload
