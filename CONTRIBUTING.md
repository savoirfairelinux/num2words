## How can I contribute ?

### Code contribution

#### Issues

If you are unsure where to begin contribution to Num2Words, you can start by looking through the issues page.
Numerous issues are created and waiting for your love on the [issue board](https://github.com/savoirfairelinux/num2words/issues).

#### Pull Requests

Contributions will be accepted through the creation of Pull Requests. Here is the workflow:

* Fork the repository into yours and work from there
* Commit and push your changes into your fork
* When you are done, create a [Pull Request](https://github.com/savoirfairelinux/num2words/compare) on the **master** branch

A template is provided to create your Pull Request. Try to fill the information at the best of your knowledge.

#### Pull request checklist

For your pull request to be merged, the answer to the following questions must be 'yes':

##### General

* Can the branch be merged automatically?

##### Testing

* Do the unit tests pass?

##### Adding new code

* Is the code PEP8 compliant?
* Is the code covered by tests?

[TravisCI](https://travis-ci.org/) is configured to run those checks on every Pull-Request. It is recommended you configure your fork to do the same.

#### Adding a language

1. Choose a language code and add `num2words/lang_XX.py` with a
   `Num2Word_XX` converter. Use an existing language with similar grammatical
   rules as a starting point; copying its word lists alone is not sufficient.
   Most converters inherit from `Num2Word_Base` in `base.py`, or from a related
   converter such as `Num2Word_EU` in `lang_EU.py`. Preserve the license header
   when adapting an existing file.
2. Implement the conversion methods the language supports: `to_cardinal`,
   `to_ordinal`, `to_ordinal_num`, `to_year` and `to_currency`. Check inherited
   behavior too: the base ordinal and year methods fall back to cardinal output,
   which may not be correct for your language. If you use the base currency
   converter, supply `CURRENCY_FORMS` and the language's `pluralize` rules.
   Keep `str_to_number` available for numeric strings, and ensure any overridden
   constructor initializes the state needed by inherited methods.
3. Import the module in `num2words/__init__.py` and register a converter instance
   in `CONVERTER_CLASSES`, for example `'xx': lang_XX.Num2Word_XX()`.
   Language codes use lowercase letters; regional variants use codes such as
   `pt_BR`. Add the supported code to the language list in `README.rst`.
4. Add `tests/test_xx.py`, following the existing `unittest.TestCase` tests.
   Exercise the public `num2words(..., lang='xx')` function, so registration and
   argument forwarding are covered. Include zero, one, negative numbers,
   fractions, and boundaries where grammar changes (such as tens, hundreds and
   thousands), as applicable. Check supported output modes, numeric strings and
   language-specific options against references or a fluent speaker.

Language-specific variants belong in keyword arguments to the converter's
methods. The public `num2words` function forwards extra keyword arguments to the
method selected by `to`; there is no universal option for traditional versus
informal spelling. Give a new option a default that preserves existing output,
and support it on each conversion method where it applies. For example, Welsh
already accepts `gender` and `counted` for cardinal numbers:

```python
from num2words import num2words

num2words(3, lang='cy', gender='fem')  # 'tair'
num2words(23, lang='cy', counted='ci')  # 'tri chi ar hugain'
```

Document the new language's options and limitations with examples. Converters
are instantiated once in `CONVERTER_CLASSES`, so an option supplied for one call
must not change the default behavior of later calls.

Run the tests and style checks from the repository root. For example, with
Python 3.12 installed:

```console
python -m pip install tox
python -m tox -e py312,flake8,isort
```

Use the corresponding environment from `tox.ini` for your installed Python
version. The test environment checks both library and test coverage; the full
interpreter matrix runs in CI.

### Reporting bugs

Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/).

#### How to submit a good bug report

Please include as many details as possible. An issue template is automatically loaded when you create an issue.

* Use a clear and comprehensive title for the issue
* Describe the expected behaviour in as many details as possible
* Describe the actual behaviour in as many details as possible

### Testing the application

Our development process is based on Continuous Integration. We love to have a nice code coverage!
