class QueryException(Exception):
    MESSAGE = 'No me pasaste una query papu'

    def __init__(self):
        super().__init__(self.MESSAGE)
