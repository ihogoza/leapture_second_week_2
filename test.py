import os
import unittest
 
from flasksec import app, db
 
TEST_DB = 'test.db'
 
class BasicTests(unittest.TestCase):
 
############################
#### setup and teardown ####
############################
 
# executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        # os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        
        # Disable sending emails during unit testing
        # mail.init_app(app)
        self.assertEqual(app.debug, False)
 
# executed after each test
    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
if __name__ == "__main__":
    unittest.main()
 


# try:
#     from flaskswa import app
#     import unittest

# except Exception as e:
#     print('Some Modules are Missing{}'.format(e))
    
# class FlaskTestCase(unittest.TestCase):
    
#     #Check if Response is 200
#     def test_index(self):
#         tester = app.test_client(self)
#         response = tester.get('localhost:5000/register')
#         print(response)
#         statuscode = response.status_code
#         self.assertEqual(statuscode, 200)
        
        
# if __name__ == '__main__':
#     unittest.main()