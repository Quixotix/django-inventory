from distutils.core import setup
import os
import inventory

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-inventory', 
    version=inventory.get_version(),
    description='Basic inventory management for Django applications.',
    long_description=read('README.markdown'),
    author='Micah Carrick',
    author_email='micah@quixotix.com',
    url='https://github.com/Quixotix/django-inventory',
    #packages=['inventory', 'inventory.management', 'inventory.management.commands'],
    packages=['inventory',],
    license='BSD',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
    ],
)
