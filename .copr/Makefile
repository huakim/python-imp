EXT    := .src.rpm
name   := python-download_rpm_source
outdir ?= $(shell rpm --eval '%{_srcrpmdir}')

srpm:
	dnf install -y pyp2spec python3-build rpm-build python3-setuptools
	bash -x ./main.sh
	rpmbuild -D'%_srcrpmdir $(outdir)' -D'%_sourcedir .' -bs $(name).spec
	
