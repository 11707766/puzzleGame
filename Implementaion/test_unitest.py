
import unittest   # The test framework
from options1 import options

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increasescore(self):
        previous_score=10
        add_5=5
        total= options.add(previous_score,add_5)
        output=15
        self.assertEqual(total, output)

    def test_decreasescore(self):
        previous_score=25
        sub_5=5
        total= options.reduce(previous_score,sub_5)
        output=20
        self.assertEqual(total, output)
        

    def test_input1(self):
        """
        Text input and ouput
        """
        in1 ="elephant"
        result = options.check(in1)
        self.assertEqual(result,True)

    def test_list_int(self):
        """
        Test that it can sum a list of scores
        """
        data = [5, -5, 15]
        result = options.sumofscore(data)
        self.assertEqual(result, 15)

    def test_input2(self):
        """
        Text input and ouput
        """
        in1 ="aple"
        result = options.checkw(in1)
        self.assertEqual(result,False)
        
    

if __name__ == '__main__':
    unittest.main()
