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

include_value
-------------

Ensures that page includes the given value::

    >>> browser |should| include_value('div_value')
    >>> browser |should_not| include_value('unexisting')

be_in_url
---------

Ensures that page is in the given url::

    >>> browser |should| be_in_url('http://localhost:5000/')
    >>> browser |should_not| be_in_url('unexisting')

have_status_code
----------------

Ensures that page have the given status code::

    >>> browser |should| have_status_code(200)
    >>> browser |should_not| have_status_code(404)


how to install
~~~~~~~~~~~~~~

There's no Pypi packages at the moment, but you can install directly from Github::

    pip install -U https://github.com/rodrigomanhaes/should-splinter/tarball/master

