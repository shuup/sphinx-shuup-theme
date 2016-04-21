from setuptools import setup
from sphinx_shoop_theme import __version__


setup(
    name='sphinx_shoop_theme',
    version=__version__,
    url='https://github.com/shoopio/sphinx_shoop_theme/',
    license='MIT',
    author='Shoop Ltd (original by Dave Snider)',
    description='Sphinx Theme for Shoop',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['sphinx_shoop_theme'],
    package_data={'sphinx_shoop_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*'
    ]},
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
