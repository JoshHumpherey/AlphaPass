import unittest
import password_gen

class PasswordGenTests(unittest.TestCase):

    def test_PasswordGen(self):
        expectedResult = '749bd32ac64d1ceb519878e6e1925d072b8bf143eb84c035cb94caf9bc693a6f'
        masterKey = '1234'
        serviceName = 'Bank'
        testPW = password_gen.GeneratePassword(masterKey,serviceName)
        self.assertEqual(testPW,expectedResult)






if __name__ == '__main__':
    unittest.main()
