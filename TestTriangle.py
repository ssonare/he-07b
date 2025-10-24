"""
Enhanced Test Suite for Triangle Classification
Comprehensive test cases using equivalence partitioning and boundary value analysis
"""
import unittest
from Triangle import classify_triangle

class TestTriangle(unittest.TestCase):

    # Test Case Group 1: Equilateral Triangles
    def test_equilateral_small(self):
        """Test ID 1: Small equilateral triangle"""
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral")

    def test_equilateral_medium(self):
        """Test ID 2: Medium equilateral triangle"""
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral")

    def test_equilateral_large(self):
        """Test ID 3: Large equilateral triangle"""
        self.assertEqual(classify_triangle(100, 100, 100), "Equilateral")

    # Test Case Group 2: Isosceles Triangles
    def test_isosceles_ab_equal(self):
        """Test ID 4: Isosceles with a=b"""
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles")

    def test_isosceles_bc_equal(self):
        """Test ID 5: Isosceles with b=c"""
        self.assertEqual(classify_triangle(3, 5, 5), "Isosceles")

    def test_isosceles_ac_equal(self):
        """Test ID 6: Isosceles with a=c"""
        self.assertEqual(classify_triangle(5, 3, 5), "Isosceles")

    def test_isosceles_large(self):
        """Test ID 7: Large isosceles triangle"""
        self.assertEqual(classify_triangle(10, 10, 15), "Isosceles")

    # Test Case Group 3: Scalene Triangles
    def test_scalene_small(self):
        """Test ID 8: Small scalene triangle"""
        self.assertEqual(classify_triangle(2, 3, 4), "Scalene")

    def test_scalene_medium(self):
        """Test ID 9: Medium scalene triangle"""
        self.assertEqual(classify_triangle(5, 7, 9), "Scalene")

    def test_scalene_large(self):
        """Test ID 10: Large scalene triangle"""
        self.assertEqual(classify_triangle(13, 15, 20), "Scalene")

    # Test Case Group 4: Right Triangles
    def test_right_triangle_345(self):
        """Test ID 11: Classic 3-4-5 right triangle"""
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right")

    def test_right_triangle_543(self):
        """Test ID 12: 3-4-5 right triangle (different order)"""
        self.assertEqual(classify_triangle(5, 4, 3), "Scalene Right")

    def test_right_triangle_51213(self):
        """Test ID 13: 5-12-13 right triangle"""
        self.assertEqual(classify_triangle(5, 12, 13), "Scalene Right")

    def test_right_triangle_81517(self):
        """Test ID 14: 8-15-17 right triangle"""
        self.assertEqual(classify_triangle(8, 15, 17), "Scalene Right")

    def test_isosceles_right(self):
        """Test ID 15: Isosceles right triangle (1-1-sqrt2)"""
        self.assertEqual(classify_triangle(1, 1, 2**0.5), "Isosceles Right")

    def test_isosceles_right_larger(self):
        """Test ID 16: Larger isosceles right triangle"""
        self.assertEqual(classify_triangle(5, 5, 5*2**0.5), "Isosceles Right")

    # Test Case Group 5: Invalid Triangles - Violates Triangle Inequality
    def test_invalid_sum_equals_third(self):
        """Test ID 17: Sum of two sides equals third side"""
        self.assertEqual(classify_triangle(1, 2, 3), "Not a triangle")

    def test_invalid_sum_less_than_third(self):
        """Test ID 18: Sum of two sides less than third side"""
        self.assertEqual(classify_triangle(1, 2, 10), "Not a triangle")

    def test_invalid_one_side_too_large(self):
        """Test ID 19: One side much larger than others"""
        self.assertEqual(classify_triangle(1, 1, 5), "Not a triangle")

    def test_invalid_different_order(self):
        """Test ID 20: Invalid triangle with different parameter order"""
        self.assertEqual(classify_triangle(10, 1, 1), "Not a triangle")

    # Test Case Group 6: Invalid Input - Zero or Negative Values
    def test_invalid_zero_side_a(self):
        """Test ID 21: Zero value for side a"""
        self.assertEqual(classify_triangle(0, 5, 5), "Not a triangle")

    def test_invalid_zero_side_b(self):
        """Test ID 22: Zero value for side b"""
        self.assertEqual(classify_triangle(5, 0, 5), "Not a triangle")

    def test_invalid_zero_side_c(self):
        """Test ID 23: Zero value for side c"""
        self.assertEqual(classify_triangle(5, 5, 0), "Not a triangle")

    def test_invalid_all_zeros(self):
        """Test ID 24: All sides are zero"""
        self.assertEqual(classify_triangle(0, 0, 0), "Not a triangle")

    def test_invalid_negative_side_a(self):
        """Test ID 25: Negative value for side a"""
        self.assertEqual(classify_triangle(-1, 5, 5), "Not a triangle")

    def test_invalid_negative_side_b(self):
        """Test ID 26: Negative value for side b"""
        self.assertEqual(classify_triangle(5, -1, 5), "Not a triangle")

    def test_invalid_negative_side_c(self):
        """Test ID 27: Negative value for side c"""
        self.assertEqual(classify_triangle(5, 5, -1), "Not a triangle")

    def test_invalid_all_negative(self):
        """Test ID 28: All sides negative"""
        self.assertEqual(classify_triangle(-1, -1, -1), "Not a triangle")

    # Test Case Group 7: Boundary Value Tests
    def test_boundary_smallest_valid(self):
        """Test ID 29: Smallest valid triangle (all sides = 1)"""
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral")

    def test_boundary_large_values(self):
        """Test ID 30: Large but valid triangle"""
        self.assertEqual(classify_triangle(100, 150, 200), "Scalene")

    def test_boundary_just_valid(self):
        """Test ID 31: Triangle that just satisfies inequality"""
        self.assertEqual(classify_triangle(2, 3, 4), "Scalene")

    # Test Case Group 8: Floating Point Tests
    def test_float_scalene(self):
        """Test ID 32: Scalene triangle with float values"""
        self.assertEqual(classify_triangle(2.5, 3.5, 4.5), "Scalene")

    def test_float_equilateral(self):
        """Test ID 33: Equilateral with float values"""
        self.assertEqual(classify_triangle(2.5, 2.5, 2.5), "Equilateral")

    # Test Case Group 9: Edge Cases
    def test_edge_almost_equilateral(self):
        """Test ID 34: Almost equilateral but actually isosceles"""
        self.assertEqual(classify_triangle(5, 5, 5.1), "Isosceles")

    def test_edge_very_thin_triangle(self):
        """Test ID 35: Very thin but valid triangle"""
        self.assertEqual(classify_triangle(10, 10, 1), "Isosceles")

if __name__ == "__main__":
    # Run tests with verbose output
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTriangle)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print(f"\n{'='*70}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {(result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100:.1f}%")
