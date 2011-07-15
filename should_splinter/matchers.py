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
