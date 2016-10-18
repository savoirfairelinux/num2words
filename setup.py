from setuptools import setup, find_packages


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Internationalization',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Localization',
    'Topic :: Text Processing :: Linguistic',
]

LONG_DESC = open('README.rst', 'rt').read() + '\n\n' + open('CHANGES.rst', 'rt').read()

setup(
    name='num2words',
    version='0.5.4',
    description='Modules to convert numbers to words. Easily extensible.',
    long_description=LONG_DESC,
    license='LGPL',
    author='Taro Ogawa <tso at users sourceforge net>',
    author_email='tos@users.sourceforge.net',
    maintainer='Savoir-faire Linux inc.',
    maintainer_email='virgil.dupras@savoirfairelinux.com',
    keywords=' number word numbers words convert conversion i18n localisation localization internationalisation internationalization',
    url='https://github.com/savoirfairelinux/num2words',
    packages=find_packages(exclude=['tests']),
    test_suite='tests',
    use_2to3=True,
)
