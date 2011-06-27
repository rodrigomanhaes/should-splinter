should-web
==========

Should-DSL matchers for tests/specifications using Splinter.


For using the matchers, you should import::

    >>> import should_web


In the following examples, ``browser`` is an instance of the
``splinter.browser.Browser`` class that is currently visiting the desired page.

include_text
------------

Ensures page includes the given text::

    >>> browser |should| include_text('Example')
    >>> browser |should_not| include_text('unexisting')

