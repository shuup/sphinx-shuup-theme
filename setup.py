import os

import setuptools


def _get_version():
    filepath = os.path.join('sphinx_shoop_theme', '__init__.py')
    with open(filepath) as fp:
        for line in fp:
            if line.startswith("__version__ = '"):
                return line.strip().split("'", 2)[1]
    raise EnvironmentError("Cannot detect version from %s" % filepath)


def _get_long_description():
    with open('README.rst') as fp:
        return fp.read()


if __name__ == '__main__':
    setuptools.setup(
        name='sphinx_shoop_theme',
        version=_get_version(),
        url='https://github.com/shoopio/sphinx_shoop_theme/',
        license='MIT',
        author='Shoop Ltd (original by Dave Snider)',
        description='Sphinx Theme for Shoop',
        long_description=_get_long_description(),
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
