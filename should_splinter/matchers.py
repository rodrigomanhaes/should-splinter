from should_dsl import matcher

@matcher
def include_text():
    return (lambda browser, text: browser.is_text_present(text),
            '%r does %sinclude text %r')

@matcher
def include_id():
    return (lambda browser, id: browser.is_element_present_by_id(id),
            '%r does %sinclude id %r')

@matcher
def include_tag():
    return (lambda browser, tag: browser.is_element_present_by_tag(tag),
            '%r does %sinclude tag %r')

@matcher
def include_name():
    return (lambda browser, name: browser.is_element_present_by_name(name),
            '%r does %sinclude name %r')

@matcher
def include_css():
    return (lambda browser, css_tag: browser.is_element_present_by_css(css_tag),
            '%r does %sinclude name %r')

@matcher
def have_title():
    return (lambda browser, title: title == browser.title,
            '%r does %sinclude title %r')

@matcher
def be_in_url():
    return (lambda browser, url: url == browser.url,
        '%r is %sin url  %r')
