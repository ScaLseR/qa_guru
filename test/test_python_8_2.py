"""Домашнее задание урок - 2. Погружаемся в инструментарий и библиотеки."""
from selene import be, have


# Тест на удачный поиск в Google
def test_successful_search(open_browser_full_screen):
    open_browser_full_screen.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    open_browser_full_screen.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser tests in ...'))


# Тест на пустой поиск в Google
def test_empty_search(open_browser_full_screen):
    open_browser_full_screen.element('[name="q"]').should(be.blank).type('hjhsdgfukjsdhf;lasdfp[asodfojusdoifghslkd]').press_enter()
    open_browser_full_screen.element('#extabar #result-stats').should(have.text('Результатов: примерно 0'))
