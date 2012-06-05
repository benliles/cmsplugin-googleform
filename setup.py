from os.path import dirname, join

from setuptools import setup, find_packages



version = '0.1'

setup(
    name = 'cmsplugin-googleform',
    version = version,
    description = "Django CMS Plugin for Google Forms",
    long_description = open(join(dirname(__file__), 'README.rst')).read() + "\n" + 
                       open(join(dirname(__file__), 'HISTORY.rst')).read(),
    classifiers = [
        "Framework :: Django",
        "Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License"],
    keywords = 'django cms plugin google forms docs',
    author = 'Corbin Fanning',
    author_email = 'corbinfanning@gmail.com',
    url = 'https://github.com/benliles/cmsplugin-googleform',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'setuptools',
        'django-cms>=2.1.0',],
)
