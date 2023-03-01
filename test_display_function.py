from function import display_month
import pytest

#คำสั่งรัน pytest -m display
@pytest.mark.display
@pytest.mark.parametrize('input_number,expected_result', [
    (1,"january"),(2,"february"),(3,"march"),(4,"april"),(5,"may"),(6,"june"),(7,"july"),(8,"august"),(9,"september"),(10,"october"),(11,"november"),(12,"december"),(0,"out of range")
    ,(13,"out of range"),(-10,"out of range"),(22, "out of range"),(1.1,"input integer"),(13.1,"out of range"),("a","input integer"),("#","input integer"),(0.5,"out of range"),(-1.5,"out of range"),(1.5,"input integer")
])

def test_display(input_number,expected_result):
    actual_result = display_month(input_number)
    assert expected_result == actual_result

