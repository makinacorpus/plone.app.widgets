NIX_PATH=~/.nix-defexpr/channels/

all: bootstrap
	bin/buildout -v

travis: bootstrap
	bin/buildout -c travis.cfg -v

bootstrap:
	NIX_PATH=${NIX_PATH} nix-build --out-link nixenv dev.nix
	./nixenv/bin/virtualenv --distribute --clear .
	echo ../../../nixenv/lib/python2.7/site-packages > lib/python2.7/site-packages/nixenv.pth
	./bin/easy_install -H "" zc.buildout
	mkdir -p buildout-cache/downloads

test:
	bin/test

print-syspath:
	./bin/python -c 'import sys,pprint;pprint.pprint(sys.path)'

.PHONY: all bootstrap print-syspath
