from square import pythagorean_triplets

def test_pythagorean():
    assert pythagorean_triplets(5)[0]==(3,4,5)
    assert len(pythagorean_triplets(10))==2
    for i in range(1,5):
        assert pythagorean_triplets(i)==[]