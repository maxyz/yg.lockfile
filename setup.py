#!/usr/bin/env python
# Generated by jaraco.develop (https://bitbucket.org/jaraco/jaraco.develop)
import setuptools

with open('README.rst') as readme:
	long_description = readme.read()

setup_params = dict(
	name='yg.lockfile',
	use_hg_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description="Lockfile object with timeouts and context manager",
	long_description=long_description,
	url="https://bitbucket.org/jaraco/yg.lockfile",
	packages=setuptools.find_packages(),
	namespace_packages=['yg'],
	zip_safe=True,
	setup_requires=[
		'hgtools',
	],
	install_requires=[
		'zc.lockfile',
	],
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)
