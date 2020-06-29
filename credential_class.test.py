import unittest # Importing the unittest module
import pyperclip#helps in copy and paste functions

from credential_class import User, Credential

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the users class behaviours
    Args:
        unittest.TestCase: Testcase class that helps create test cases
    '''

    def setUp(self):
        '''
        Function to help create user a/c details before each test
        '''
        self.new_user = User('Tom','Chege','angry')

    def test_init_(self):
        '''
        Test to check creation of new user instance
        '''
        self.assertEqual(self.new_user.first_name,'Norah')
        self.assertEqual(self.new_user.last_name,'Shako')
        self.assertEqual(self.new_user.password,'sugar')

    def test_save_user(self):
        '''
        Test to check if New user information is saved into the users_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours
    Args:
        unittest.TestCase: Testcase class that helps create test cases
    '''

    def test_confirm_user(self):
        '''
        Function to confirm login details to active user
        '''
        self.new_user = User('Norah','Shako','sugar')
        self.new_user.save_user()
        userX= User('Norah','Shako','sugar')
        userX.save_user()
        active_user = Credential.confirm_user('Norah', 'Shako','angry')
        self.assertTrue(active_user)

    def setUp(self):
        '''
        Function to create social media account credentials before each test
        '''
        self.new_credential = Credential('cyrian', 'facebook','cyrian254','contented')

    def test__init__(self):
        '''
        Confirm that instance of credentials creation is as expected
        '''
        self.assertEqual(self.new_credential.user_name,'cyrian')
        self.assertEqual(self.new_credential.social_media,'facebook')
        self.assertEqual(self.new_credential.account_name,'cyrian254')
        self.assertEqual(self.new_credential.password,'contented')

    def test_save_credentials(self):
        '''
        Test and confirm that the new credential information is being saved
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credential.credentials_list),1)

    def tearDown(self):
        '''
        tearDown method that executes a set of instructions after every test
        '''
        User.users_list = []
        Credential.credentials_list = []

    def test_display_credentials(self):
        '''
        Test to confirm user can view the correct credential details
        '''
        self.new_credential.save_credentials()
        facebook = Credential('cyrian','facebook','cyrian254','contented')
        facebook.save_credentials()
        self.assertEqual(Credential.display_credentials(),Credential.credentials_list)

    def test_search_social_media(self):
        '''
        Test to confirm if the method returns the correct social media credential
        '''
        self.new_credential.save_credentials()
        facebook = Credential('cyrian','Facebook','cyrian254','contented')
        facebook.save_credentials()
        credential_exists = Credential.search_social_media('Facebook')
        self.assertEqual(credential_exists,facebook)

    def test_copy_password(self):#uses pyperclip
        '''
        Test to check if the copy password method will copy the correct password from social media site specified
        '''
        self.new_credential.save_credentials()
        facebook = Credential('cyrian','Facebook','cyrian254','contented')
        facebook.save_credentials()
        Credential.copy_password('facebook')
        self.assertEqual(self.new_credential.password,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()