import unittest
import sys
sys.path.append('../src/')
import codebase as cb

class Test_codebase(unittest.TestCase):

    def test_process(self):
        Json_payload = """  {
  	    "Year": "1993",
  	    "Month": "09",
  	    "Day": "16",
  	    "Hour": "17",
  	    "Min": "55",
  	    "Lat": "16.989",
  	    "Lon": "82.247"
        }
        """
        cb.process(Json_payload)

        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()