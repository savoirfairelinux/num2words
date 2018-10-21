import re

from setuptools import find_packages, setup

PACKAGE_NAME = "num2words"

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Library or Lesser General Public License '
    '(LGPL)',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Internationalization',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Localization',
    'Topic :: Text Processing :: Linguistic',
]

LONG_DESC = open('README.rst', 'rt').read() + '\n\n' + \
            open('CHANGES.rst', 'rt').read()


def find_version(fname):
    """Parse file & return version number matching 0.0.1 regex
    Returns str or raises RuntimeError
    """
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version


setup(
    name=PACKAGE_NAME,
    version=find_version("bin/num2words"),
    description='Modules to convert numbers to words. Easily extensible.',
    long_description=LONG_DESC,
    license='LGPL',
    author='Taro Ogawa <tso at users sourceforge net>',
    author_email='tos@users.sourceforge.net',
    maintainer='Savoir-faire Linux inc.',
    maintainer_email='istvan.szalai@savoirfairelinux.com',
    keywords=' number word numbers words convert conversion i18n '
             'localisation localization internationalisation '
             'internationalization',
    url='https://github.com/savoirfairelinux/num2words',
    packages=find_packages(exclude=['tests']),
    test_suite='tests',
    classifiers=CLASSIFIERS,
    scripts=['bin/num2words'],
    install_requires=["docopt>=0.6.2"],
    tests_require=['delegator.py'],
)
