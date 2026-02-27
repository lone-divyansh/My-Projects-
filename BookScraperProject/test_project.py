import unittest
from main import clean_and_sort

class TestScraperLogic(unittest.TestCase):
    """
    Unit Tests for the Book Scraper logic.
    We do NOT test the website connection here (that would be slow).
    We only test our internal data processing logic.
    """
    
    def test_cleaning_and_sorting(self):
        """
        Test if clean_and_sort() correctly handles currency conversion and sorting.
        """
        # 1. ARRANGE: Create fake input data
        fake_data = [
            ('Expensive Book', '£50.00'),
            ('Cheap Book', '£10.50'),
            ('Middle Book', '£20.00')
        ]
        
        # 2. ACT: Run the function being tested
        result = clean_and_sort(fake_data)
        
        # 3. ASSERT: Define the expected perfect output
        expected_output = [
            ('Cheap Book', 10.50),    # Should be first (cheapest)
            ('Middle Book', 20.00),   # Should be second
            ('Expensive Book', 50.00) # Should be last
        ]
        
        # Check if Result == Expectation
        self.assertEqual(result, expected_output)
        print("\nSUCCESS: The sorting logic works perfectly!")

if __name__ == '__main__':
    unittest.main()