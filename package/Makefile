include $$(GOROOT)/src/Make.inc

TARG = ${name}
GOFILES = ${name}.go
	
include $$(GOROOT)/src/Make.pkg

.PHONY: gofmt
gofmt:
	gofmt -w $$(GOFILES)
