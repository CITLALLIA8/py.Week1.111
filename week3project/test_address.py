# test_address.py


from address import extract_city, extract_state, extract_zipcode


def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("1600 Pennsylvania Ave, Washington, DC 20500") == "Washington"
    assert extract_city("400 South Orange Ave, Orlando, FL 32801") == "Orlando"


def test_extract_state():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("1600 Pennsylvania Ave, Washington, DC 20500") == "DC"
    assert extract_state("400 South Orange Ave, Orlando, FL 32801") == "FL"


def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("1600 Pennsylvania Ave, Washington, DC 20500") == "20500"
    assert extract_zipcode("400 South Orange Ave, Orlando, FL 32801") == "32801"