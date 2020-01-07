import unittest
import sys
#sys.path.append('../src/')
import json
import src.codebase as cb

class test_codebase(unittest.TestCase):

    def test_process(self):
        Json_payload = """    {
  	"Year": "1993",
  	"Month": "09",
  	"Day": "16",
  	"Hour": "17",
  	"Min": "55",
  	"Lat": "16.989",
  	"Lon": "82.247"
    }
        """
        out = cb.process(json.loads(Json_payload))

        self.assertEqual(out['Sun'], '149 29 52 34 Leo')

if __name__ == '__main__':
    unittest.main()