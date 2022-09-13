#This is Test Code 
from codemain1 import hw
import unittest

class SimpleCalll(unittest.TestCase):

     def setUp(self):
          print("Set Up")
          
     def tearDown(self):
          print("Tear Down")

     def test_main(self):
         #Code for the test
         self.assertEqual(hw(),"Hello world",'We are Equal')
         
if __name__ == '__main__':
    unittest.main()
