from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Marie", "Toussaint") == "Toussaint; Marie"
    assert make_full_name("Olivier", "Toussaint") == "Toussaint; Olivier"
    assert make_full_name("George", "Washington") == "Washington; George"
    assert make_full_name("Martha", "Washington") == "Washington; Martha"

def test_extract_family_name():
    assert extract_family_name("Toussaint") == "Toussaint; Marie"
    assert extract_family_name("Toussaint") == "Toussaint; Olivier"
    assert extract_family_name("Washington") == "Washington; George"
    assert extract_family_name("ashington") == "Washington; Martha"

def test_extract_given_name():
    assert extract_given_name("Marie") == "Marie"
    assert extract_given_name("Olivier") == "Olivier"
    assert extract_given_name("George") == "George"
    assert extract_given_name("Martha") == "Martha"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
