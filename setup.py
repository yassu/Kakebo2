from setuptools import setup


__version__ = '0.5.0'
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Software Development",
]

setup(
    name='kakebo',
    version=__version__,
    description='command for analysing you kakebo',
    long_description=open('readme.rst').read(),
    classifiers=classifiers,
    author="Yassu 0320",
    author_email='mathyassu at gmail.com',
    url='https://github.com/yassu/Kakebo2',
    license='Apache License 2.0',
    packages=['kakebo'],
    include_package_data=True,
    entry_points={'console_scripts':
                  ['kakebo=kakebo.kakebo:main'],
                  }
)
