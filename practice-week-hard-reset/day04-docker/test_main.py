import unittest
from main import is_prime

class TestPrime(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(13))
        
    def test_non_primes(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))

if __name__ == "__main__":
    unittest.main()