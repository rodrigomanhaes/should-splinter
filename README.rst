should-web
==========

Should-DSL matchers for web application tests using `Splinter <http://splinter.cobrateam.info>`_ framework.


For using the matchers, you should import::

    >>> import should_web


In the following examples, ``browser`` is an instance of the
``splinter.browser.Browser`` class that is currently visiting the desired page.

include_text
------------

Ensures that page includes the given text::

    >>> browser |should| include_text('Example')
    >>> browser |should_not| include_text('unexisting')


how to install
~~~~~~~~~~~~~~

There's no Pypi packages at the moment, but you can install directly from Github::

    pip install -U https://github.com/rodrigomanhaes/should-web/tarball/master


should-web?
~~~~~~~~~~~

Yes, the name is ugly. If you have a better one, let me know.

