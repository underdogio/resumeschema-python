import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    long_description = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as requirements:
    install_requires = [line.strip() for line in requirements]

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
]

setup(
    name='resumeschema',
    packages=['resumeschema'],
    package_data={'resumeschema': ['schema.json']},
    setup_requires=[],
    author='Brett Langdon',
    author_email='me@brett.is',
    classifiers=classifiers,
    description='JSON schema validator for the resume-schema (https://github.com/jsonresume/resume-schema) spec',
    install_requires=install_requires,
    license='MIT',
    long_description=long_description,
    url='http://github.com/underdogio/resumeschema-python',
    version='1.0.0',
)
