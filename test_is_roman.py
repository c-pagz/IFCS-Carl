from roman_numerals import roman_numerals_converter

# Happy Test
def test_happy():
        assert roman_numerals_converter(5) == "V"
        assert roman_numerals_converter(3) != "X"

# Unhappy Test
def test_unhappy():
    assert roman_numerals_converter(68) != "X"
    assert roman_numerals_converter ("IX") != 9

    
    

        
        


