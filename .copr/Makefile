outdir ?= $(shell rpm --eval '%{_srcrpmdir}')

srpm:
	dnf install -y pyp2spec python3-build rpm-build python3-setuptools rpkg ||:
	bash -x ./main.sh
	rpkg srpm --outdir '$(outdir)'
