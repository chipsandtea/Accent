import unittest

from gluon.globals import Request

execfile("applications/accent/controllers/default.py", globals())

#db(db.acc.id>0).delete()  # Clear the database
#db.acc.insert(firstname='Leslie', lastname= 'Li', email = 'test@test.com', password = '1234')
#db.commit()

class TestListActiveGames(unittest.TestCase):
    def setUp(self):
	request = Request()
    def testListActiveGames(self):
        # Set variables for the test function
	request.env.request_method = "POST"
        request.post_vars["firstname"] = "leslie"
	request.post_vars["lastname"] = "li"
	request.post_vars["password"] = "1234"
	request.post_vars["email"] = "test@test.com"

	response = api()
        self.assertEquals('success', response.status)

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestListActiveGames))
unittest.TextTestRunner(verbosity=2).run(suite)

