should-splinter
===============

Should-DSL matchers for web application tests using `Splinter <http://splinter.cobrateam.info>`_ framework.


For using the matchers, you should import::

    >>> import should_splinter


In the following examples, ``browser`` is an instance of the
``splinter.browser.Browser`` class that is currently visiting the desired page.

include_text
------------

Ensures that page includes the given text::

    >>> browser |should| include_text('Example')
    >>> browser |should_not| include_text('unexisting')

include_id
----------

Ensures that page includes the given id::

    >>> browser |should| include_id('firstheader')
    >>> browser |should_not| include_id('unexisting')

include_tag
----------

Ensures that page includes the given tag::

    >>> browser |should| include_tag('h1')
    >>> browser |should_not| include_tag('h9')

include_name
------------

Ensures that page includes the given name::

    >>> browser |should| include_name('header')
    >>> browser |should_not| include_name('unexisting')

include_css
-----------

Ensures that page includes the given css::

    >>> browser |should| include_css('title')
    >>> browser |should_not| include_css('unexisting')

include_title
-------------

Ensures that page includes the given title::

    >>> browser |should| have_title('Example Title')
    >>> browser |should_not| have_title('unexisting')


how to install
~~~~~~~~~~~~~~

There's no Pypi packages at the moment, but you can install directly from Github::

    pip install -U https://github.com/rodrigomanhaes/should-splinter/tarball/master

