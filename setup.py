# -*- coding: utf-8 -*-
import os.path
from setuptools import setup


def get_source_files():
    for dirname, _, files in os.walk('ckeditor/static/ckeditor/ckeditor/_source'):
        for filename in files:
            yield os.path.join('/'.join(dirname.split('/')[1:]), filename)

setup(
    name='django-extended-flatpages',
    version='0.1',
    packages = ['extended_flatpages'],
    include_package_data = True,
    license = 'Apache License, Version 2.0', 
    description='Django flatpages CKEditor integration and SEO values.',
    long_description=open('README.md', 'r').read() + open('AUTHORS.md', 'r').read() + open('CHANGELOG.md', 'r').read(),
    url='https://github.com/hisie/django_extended_flatpages',
    author='hisie',
    author_email='dcebrian@serincas.com',
    install_requires=[
        'django-ckeditor',
    ],
    exclude_package_data={
        'ckeditor': list(get_source_files()),
    },
    test_suite="setuptest.setuptest.SetupTestSuite",
    tests_require=[
        'django-setuptest>=0.1.1',
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
