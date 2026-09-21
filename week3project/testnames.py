# test_names.py


from names import make_full_name, extract_family_name, extract_given_name


def test_make_full_name():
    
    assert make_full_name("Michelangelo", "Buonarroti") == "Buonarroti; Michelangelo"
    
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    
    assert make_full_name("Mary-Jane", "Smith-Jones") == "Smith-Jones; Mary-Jane"
    
    assert make_full_name("George", "Washington") == "Washington; George"


def test_extract_family_name():
   
    assert extract_family_name("Buonarroti; Michelangelo") == "Buonarroti"
    
    assert extract_family_name("Brown; Sally") == "Brown"
    
    assert extract_family_name("Smith-Jones; Mary-Jane") == "Smith-Jones"
    
    assert extract_family_name("Washington; George") == "Washington"


def test_extract_given_name():
   
    assert extract_given_name("Buonarroti; Michelangelo") == "Michelangelo"
   
    assert extract_given_name("Brown; Sally") == "Sally"
    
    assert extract_given_name("Smith-Jones; Mary-Jane") == "Mary-Jane"
    
    assert extract_given_name("Washington; George") == "George"