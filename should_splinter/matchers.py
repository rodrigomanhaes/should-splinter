from should_dsl import matcher

@matcher
def include_text():
    return (lambda browser, text: browser.is_text_present(text),
            '%r does %sinclude text %r')

@matcher
def include_id():
    return (lambda browser, id: browser.find_by_id(id),
            '%r does %sinclude id %r')
