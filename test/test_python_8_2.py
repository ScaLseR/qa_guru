"""Домашнее задание урок - 2. Погружаемся в инструментарий и библиотеки."""
import pytest
from selene import be, have


# Тест на удачный поиск в Google
def test_successful_search(open_url):
    open_url.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    open_url.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser tests in ...'))


# Тест на пустой поиск в Google
@pytest.mark.parametrize("find_string", ['hjhsdgfukjsdhf;lasdfp[asodfojusdoifghslkd]'])
def test_empty_search(open_url, find_string):
    open_url.element('[name="q"]').should(be.blank).type(find_string).press_enter()
    open_url.element('#extabar #result-stats').should(have.text('Результатов: примерно 0'))
    print(f'При поиске строки - {find_string}, результатов не обнаружено')
