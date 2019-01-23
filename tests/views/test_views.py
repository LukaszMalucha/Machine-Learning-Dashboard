from unittest import TestCase
from app import app


class TestHome(TestCase):

## Home Test

    def test_home(self):
        with app.test_client() as c:
            resp = c.get('/')
            self.assertEqual(resp.status_code, 200)


# Login page loads correctly

    def test_login_page_loads(self):
        with app.test_client() as c:
            response = c.get('/login', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Please Log in' in response.data)

# Signup page loads correctly

    def test_signup_page_loads(self):
        with app.test_client() as c:
            response = c.get('/signup', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Sign Up' in response.data)


# Manage DB page loads correctly


    def test_manage_db_page_loads(self):
        with app.test_client() as c:
            response = c.get('/manage_db', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Add Algorithm Type:' in response.data)


# Ensure that title & default user shows on main page

    def test_title_shows_up(self):
        with app.test_client() as c:
            response = c.get('/')
            self.assertTrue(b'Available Code Templates' in response.data)
            self.assertEqual(response.status_code, 200)

# Ensure that data table shows on main page

    def test_table_shows_up(self):
        with app.test_client() as c:
            response = c.get('/')
            self.assertTrue(b'Type of Estimator' in response.data)
            self.assertEqual(response.status_code, 200)

# Ensure that add algorithm page loads correctly

    def test_add_algorithm_page_loads(self):
        with app.test_client() as c:
            response = c.get('/add_request')
            self.assertTrue(b'Author' in response.data)
            self.assertEqual(response.status_code, 200)


# Ensure that edit algorithm page loads correctly

    def test_add_algorithm_page_loads(self):
        with app.test_client() as c:
            response = c.get('/edit_code/1')
            self.assertTrue(b'Edit Template' in response.data)
            self.assertEqual(response.status_code, 200)


# Ensure that Github Repo shows up

    def test_github_shows_up(self):
        with app.test_client() as c:
            response = c.get('/')
            self.assertTrue(b'Types of Estimator' in response.data)
            self.assertEqual(response.status_code, 200)

# Classification Page Test

    def test_classification_page_loads(self):
        with app.test_client() as c:
            response = c.get('/classification', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'classification' in response.data)

# Regression Page Test

    def test_regression_page_loads(self):
        with app.test_client() as c:
            response = c.get('/regression', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'regression' in response.data)

# Clustering Page Test

    def test_clustering_page_loads(self):
        with app.test_client() as c:
            response = c.get('/clustering', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'clustering' in response.data)


# Add Code Page Test

    def test_add_request_page_loads(self):
        with app.test_client() as c:
            response = c.get('/add_request', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Add Template' in response.data)

# Edit Code Page Test

    def test_edit_code_page_loads(self):
        with app.test_client() as c:
            response = c.get('/edit_code/1', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Edit Template' in response.data)
















