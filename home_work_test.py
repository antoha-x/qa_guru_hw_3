from selene import browser, be, have


def test_google_should_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search_abra_cadabra_and_not_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('abra-cadabra').press_enter()
    browser.element('[id="search"]').should(have.no.text('Selene - User-oriented Web UI browser tests in Python'))
