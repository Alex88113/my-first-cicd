from app import add_numbers

def test_sum():
    assert add_numbers(2, 3) == 5, "2 + 3 should equal 5"
    assert add_numbers(-1, 1) == 0, "-1 + 1 should equal 0"
    print("All tests passed!")

if __name__ == "__main__":
    test_sum()