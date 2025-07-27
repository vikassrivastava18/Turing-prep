import problems
import unittest

class TestProblems(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(problems.is_prime(2))
        self.assertTrue(problems.is_prime(13))
        self.assertFalse(problems.is_prime(1))
        self.assertFalse(problems.is_prime(0))
        self.assertFalse(problems.is_prime(9))

    def test_sum_digits(self):
        self.assertEqual(problems.sum_digits("12345"), 15)
        self.assertEqual(problems.sum_digits("000"), 0)


    def test_same_chars(self):
        self.assertTrue(problems.same_chars("abc", "cab"))
        self.assertFalse(problems.same_chars("abc", "def"))
        self.assertTrue(problems.same_chars("aabb", "baba"))

    def test_dot_product(self):
        self.assertEqual(problems.dot_product((1,2,3), (4,5,6)), (3, 32))
        self.assertEqual(problems.dot_product((0,0), (0,0)), (2, 0))

    def test_count_sqrts(self):
        self.assertEqual(problems.count_sqrts([3,4,2,1,9,25]), 3)
        self.assertEqual(problems.count_sqrts([1,2,3]), 1)

    def test_is_anagram2(self):
        self.assertTrue(problems.is_anagram2("listen", "silent"))
        self.assertFalse(problems.is_anagram2("aab", "abb"))

    def test_is_anagram3(self):
        self.assertTrue(problems.is_anagram3("listen", "silent"))
        self.assertFalse(problems.is_anagram3("aab", "abb"))

    def test_sum_str_lengths(self):
        self.assertEqual(problems.sum_str_lengths(["a", "bb", ["ccc"]]), 6)
        with self.assertRaises(ValueError):
            problems.sum_str_lengths(["a", 1])

    def test_flatten(self):
        self.assertEqual(problems.flatten([1, [2, [3]], 4]), [1,2,3,4])
        self.assertEqual(problems.flatten([]), [])

    def test_Circle(self):
        c1 = problems.Circle(3)
        c2 = problems.Circle(4)
        self.assertEqual(c1.get_radius(), 3)
        c1.set_radius(5)
        self.assertEqual(c1.get_radius(), 5)
        self.assertAlmostEqual(c1.get_area(), 5*5*3.141592653589793, places=5)
        self.assertFalse(c1.equal(c2))
        self.assertEqual(c1.bigger(c2), c1)
        c3 = c1 + c2
        self.assertEqual(c3.get_radius(), 9)
        self.assertEqual(str(c1), "Circle of radius: 5")

    def test_Queue_Stack(self):
        q = problems.Queue()
        s = problems.Stack()
        q.add(1)
        q.add(2)
        self.assertEqual(q.remove(), 1)
        self.assertEqual(q.remove(), 2)
        self.assertIsNone(q.remove())
        s.add(1)
        s.add(2)
        self.assertEqual(s.remove(), 2)
        self.assertEqual(s.remove(), 1)
        self.assertIsNone(s.remove())

    def test_fibonacci(self):
        self.assertEqual(problems.fibonacci(0), 0)
        self.assertEqual(problems.fibonacci(1), 1)
        self.assertEqual(problems.fibonacci(5), 5)

    def test_fibonacci_optimal(self):
        self.assertEqual(problems.fibonacci_optimal(0), 0)
        self.assertEqual(problems.fibonacci_optimal(1), 1)
        self.assertEqual(problems.fibonacci_optimal(5), 5)

    def test_group_anagram(self):
        result = problems.group_anagram(["eat", "tea", "ate", "pan", "nap"])
        self.assertTrue(any(set(g) == {"eat", "tea", "ate"} for g in result))
        self.assertTrue(any(set(g) == {"pan", "nap"} for g in result))

    def test_encoded_string(self):
        self.assertEqual(problems.encoded_string("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(problems.encoded_string("2[ab]"), "abab")

    def test_generate_subsets(self):
        result = problems.generate_subsets([1,2])
        self.assertIn([], result)
        self.assertIn([1], result)
        self.assertIn([2], result)
        self.assertIn([1,2], result)

    def test_valid_anagram(self):
        self.assertTrue(problems.valid_anagram("aab", "baa"))
        self.assertFalse(problems.valid_anagram("aab", "bba"))

    def test_remove_and_sort(self):
        L = [1,6,3,5,7,0]
        problems.remove_and_sort(L, 2)
        self.assertEqual(L, [3, 5, 6, 7])

    def test_check_sorted(self):
        self.assertTrue(problems.check_sorted([1,2,3]))
        self.assertFalse(problems.check_sorted([3,2,1]))

    def test_second_largest(self):
        self.assertEqual(problems.second_largest([1,2,3]), 2)
        self.assertEqual(problems.second_largest([10,9,8]), 9)
        with self.assertRaises(AssertionError):
            problems.second_largest([1])

    def test_wave_array(self):
        arr = [1,2,3,4,5]
        result = problems.wave_array(arr[:])
        self.assertEqual(len(result), len(arr))
        self.assertTrue(all(result[i] >= result[i+1] if i%2==0 else result[i] <= result[i+1] for i in range(len(result)-1)))

    def test_merge_sorted_arrays(self):
        self.assertEqual(problems.merge_sorted_arrays([1,3,5], [2,4,6]), [1,2,3,4,5,6])
        self.assertEqual(problems.merge_sorted_arrays([], [1,2]), [1,2])
        self.assertEqual(problems.merge_sorted_arrays([1,2], []), [1,2])

if __name__ == "__main__":
    unittest.main()