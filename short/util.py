
# Convert decimal to binary with bin(), which returns result with prefix `0b`.
decimal_to_binary = lambda x: int(bin(x)[2:])

# Convert binary to decimal
binary_to_decimal = lambda x: int(n,2)

flipping_bits = lambda x: x ^ 0xffffffff

# Check if the given number is power of 2.
is_power_of_2 = lambda x: (x > 0) and ((x & (x-1)) == 0)


# Generate array of N integers; N is within the range [1..100,000];
# Each element of array A is an integer within the range [-1,000,000..1,000,000].
import random
random_A = [random.randint(-100000, 1000000) for n in range(random.randint(1, 100000))]
