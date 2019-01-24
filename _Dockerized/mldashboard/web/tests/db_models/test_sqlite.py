from project.algorithms.models import PreprocessingModel, RedFlagModel, AlgorithmModel
from project.library.models import TypeModel, ComplexityModel, MethodModel
from project.users.models import UserModel
from tests.base_test import BaseTest




class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('test', 'test@gmail.com','abcd')

            self.assertIsNone(UserModel.find_by_username('test'), "Found an user with name 'test' before save_to_db")
            self.assertIsNone(UserModel.find_by_id(1), "Found an user with id '1' before save_to_db")

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('test'),
                                 "Did not find an user with name 'test' after save_to_db")
            self.assertIsNotNone(UserModel.find_by_id(1), "Did not find an user with id '1' after save_to_db")

            self.assertEqual(user.username, 'test',
                             "The name of the user after creation does not equal the constructor argument.")
            self.assertEqual(user.password, 'abcd',
                             "The password of the user after creation does not equal the constructor argument.")


class TypeTest(BaseTest):
    def test_crud(self):
        with self.app_context():

            test = TypeModel('test')

            self.assertIsNone(TypeModel.find_by_type('test'), "Found 'test' before save_to_db")
            self.assertIsNone(TypeModel.find_by_id(1), "Found an id '1' before save_to_db")

            test.save_to_db()

            self.assertIsNotNone(TypeModel.find_by_type('test'),
                                 "Did not find a name 'test' after save_to_db")
            self.assertIsNotNone(TypeModel.find_by_id(1), "Did not find an id '1' after save_to_db")

            self.assertEqual(test.type_of_algorithm, 'test',
                             "The name after creation does not equal the constructor argument.")

class ComplexityTest(BaseTest):
    def test_crud(self):
        with self.app_context():

            test = ComplexityModel('test')

            self.assertIsNone(ComplexityModel.find_by_complexity('test'), "Found 'test' before save_to_db")
            self.assertIsNone(ComplexityModel.find_by_id(1), "Found an id '1' before save_to_db")

            test.save_to_db()

            self.assertIsNotNone(ComplexityModel.find_by_complexity('test'),
                                 "Did not find a name 'test' after save_to_db")
            self.assertIsNotNone(ComplexityModel.find_by_id(1), "Did not find an id '1' after save_to_db")

            self.assertEqual(test.complexity, 'test',
                             "The name after creation does not equal the constructor argument.")

class MethodTest(BaseTest):
    def test_crud(self):
        with self.app_context():

            test = MethodModel('test')

            self.assertIsNone(MethodModel.find_by_method('test'), "Found 'test' before save_to_db")
            self.assertIsNone(MethodModel.find_by_id(1), "Found an id '1' before save_to_db")

            test.save_to_db()

            self.assertIsNotNone(MethodModel.find_by_method('test'),
                                 "Did not find a name 'test' after save_to_db")
            self.assertIsNotNone(MethodModel.find_by_id(1), "Did not find an id '1' after save_to_db")

            self.assertEqual(test.method, 'test',
                             "The name after creation does not equal the constructor argument.")


class MethodTest(BaseTest):
    def test_crud(self):
        with self.app_context():

            test = PreprocessingModel('test')

            self.assertIsNone(PreprocessingModel.find_by_name('test'), "Found 'test' before save_to_db")
            self.assertIsNone(PreprocessingModel.find_by_preprocess_id(1), "Found an id '1' before save_to_db")

            test.save_to_db()

            self.assertIsNotNone(PreprocessingModel.find_by_name('test'),
                                 "Did not find a name 'test' after save_to_db")
            self.assertIsNotNone(PreprocessingModel.find_by_preprocess_id(1), "Did not find an id '1' after save_to_db")

            self.assertEqual(test.name, 'test',
                             "The name after creation does not equal the constructor argument.")


class RedFlagModelTest(BaseTest):
    def test_crud(self):
        with self.app_context():

            test = RedFlagModel('test')

            self.assertIsNone(RedFlagModel.find_by_issue('test'), "Found 'test' before save_to_db")
            self.assertIsNone(RedFlagModel.find_by_issue_id(1), "Found an id '1' before save_to_db")

            test.save_to_db()

            self.assertIsNotNone(RedFlagModel.find_by_issue('test'),
                                 "Did not find a name 'test' after save_to_db")
            self.assertIsNotNone(RedFlagModel.find_by_issue_id(1), "Did not find an id '1' after save_to_db")

            self.assertEqual(test.issue, 'test',
                             "The name after creation does not equal the constructor argument.")


class AlgorithmModelTest(BaseTest):
    def test_crud(self):
        with self.app_context():

            test = AlgorithmModel('test', 'test', 'test')

            self.assertIsNone(AlgorithmModel.find_by_algorithm_type('test'), "Found 'test' before save_to_db")


            test.save_to_db()

            self.assertIsNotNone(AlgorithmModel.find_by_algorithm_type('test'),
                                 "Did not find a name 'test' after save_to_db")


            self.assertEqual(test.algorithm_type, 'test',
                             "The name after creation does not equal the constructor argument.")
