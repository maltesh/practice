class BadExveptionKata:

    def __init__(self,func,success,failure,*args):
        self.args = args
        self.func = func
        self.failure = failure
        self.success = success

    def __enter__(self):
        raise
        pass

    def __exit__(self ,type, value, traceback):
        if isinstance(value,self.args):
            self.failure(self.func,value)
            return True


def handle(func, success, failure, *args):
    with BadExveptionKata(func, success, failure, args) as e:
            success(func,func())



func = lambda : 1/0
def success():pass
def failure():pas
handle(func, success, failure, SyntaxError, OSError, EOFError, KeyError)
