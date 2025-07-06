from setuptools import setup, find_packages

import conf

attrs={}

for i in dir(conf):
    if not i.startswith('_'):
        attrs[i] = getattr(conf, i)

attrs['name'] = attrs['pypi_name']


setup(
 packages=find_packages(),
 py_modules=['imp'],
 install_requires=[],
 **attrs
)
