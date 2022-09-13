#This is Test Code 
from cmain1 import hw
import unittest

class SimpleCalll(unittest.TestCase):

     def setUp(self):
          print("Set Up")
          
     def tearDown(self):
          print("Tear Down")

     def test_main(self):
         #Code for the test
         self.assertEqual(hw(),"Hello world",'We are Equal')
         self.assertEqual(am(),"Hello amarjyoti",'We are Equal')
         
if __name__ == '__main__':
    unittest.main()
