import unittest
from app import app


class LibraryTestCase(unittest.TestCase):

            
        # Classification Page Test
        def test_add_request_page_loads(self):
            tester = app.test_client(self)
            response = tester.get('/add_request', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Add Template' in response.data) 
            
        # Regression Page Test    
        def test_edit_code_page_loads(self):
            tester = app.test_client(self)
            response = tester.get('/edit_code/1', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Edit Template' in response.data) 
            
        # Clustering Page Test    
        def test_library_page_loads(self):
            tester = app.test_client(self)
            response = tester.get('/', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Available Code Templates' in response.data) 
