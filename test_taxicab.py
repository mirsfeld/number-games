from square import check_taxicab_number, taxicab_numbers


def test_check_taxicab_number():
    assert check_taxicab_number(1729)[0] == True
    assert (1, 12) in check_taxicab_number(1729)[1] or (12, 1) in check_taxicab_number(
        1729
    )[1]
    assert (9, 10) in check_taxicab_number(1729)[1] or (10, 9) in check_taxicab_number(
        1729
    )[1]
    assert check_taxicab_number(1730)[0] == False
