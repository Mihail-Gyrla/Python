import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# Делает первую букву заглавной.Позитивный тест
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Делает первую букву заглавной.Негативный тест
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Удаляет пробелы в начале.Негативные проверки

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("   @@@abc", "123abc"),
    ("", ""),
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Удаляет пробелы в начале.Позитивные проверки


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   123abc", "123abc"),
    ("   04 апреля 2023", "04 апреля 2023"),
    ("  SkyPro", "SkyPro"),
    ("   :-D", ":-D"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

    # Возвращает `True`, если строка содержит искомый символ.Позитивные проверки


@pytest.mark.positive
@pytest.mark.parametrize("input_str, Symbol ", [
    ("SkyPro", "y"),
    ("Abcd", "A"),
    ("sd4", "4"),
    ("111.222", "."),
    ("@@@", "@"),
])
def test_contains_positive(input_str, Symbol):
    assert string_utils.contains(input_str, Symbol) == True


# Возвращает `False`, если строка не содержит искомый символ.Позитивные проверки
@pytest.mark.positive
@pytest.mark.parametrize("input_str, Symbol ", [
    ("SkyPro", "t"),
    ("Abcd", "Ae"),  # Баг, строка одновременно содержит и искомый,и отсутствующий символ
    (" sd4", "3"),
    ("111.222", ","),
    ("@@@", "f"),
    ("S", "s")  # Баг, не учитывает регистр
])
def test_contains_positive(input_str, Symbol):
    assert string_utils.contains(input_str, Symbol) == False


# Удаляет все подстроки из переданной строки.Позитивные проверки

@pytest.mark.positive
@pytest.mark.parametrize("input_str, Symbol ,expected", [
    ("SkyPro", "P", "Skyro"),
    (" Abcd", " ", "Abcd"),
    ("sd4", "4", "sd"),
    ("111.222", "111.222", ""),
    ("@@@   ", "   ", "@@@"),
])
def test_delete_symbol_positive(input_str, Symbol, expected):
    assert string_utils.delete_symbol(input_str, Symbol) == expected

    # Удаляет все подстроки из переданной строки.Негативные  проверки


@pytest.mark.negative
@pytest.mark.parametrize("input_str, Symbol ,expected", [
    ("", "", ""),
    ("A_bcd", "_", "Abcd"),
    ("   ", "   ", ""),
    ("Вика", "л", "Вика"),  # Баг,при удалении несуществующего символа нет сообщения об ошибке
    ("@@@   ", "   ", "@@@"),
])
def test_delete_symbol_positive(input_str, Symbol, expected):
    assert string_utils.delete_symbol(input_str, Symbol) == expected
    print(expected)
