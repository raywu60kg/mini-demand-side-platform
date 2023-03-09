from tests.test_data.test_data import test_records

class MockPostgresClient():
    @staticmethod
    def cursor(**kwargs):
        return MockCursor()


class MockCursor():

    def execute(self, query_schema):
        if query_schema == "SELECT * FROM ctr;":
            self.res = test_records
        else:
            self.res = None

    def fetchall(self):
        return self.res
