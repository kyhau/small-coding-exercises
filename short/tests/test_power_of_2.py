from math import pow


# Check if the given number is power of 2.
is_power_of_2 = lambda x : (x > 0) and ((x & (x-1)) == 0)


def test_is_power_of_2():

    for i in range(32):
        x = int(pow(2, i))
        assert is_power_of_2(x) is True

        if x > 2:
            assert is_power_of_2(x-1) is False
