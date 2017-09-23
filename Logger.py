class Logger:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def __init__(self):
        pass
    def err(self, s):
        print (self.FAIL + s + self.ENDC)
    def valid(self, s):
        print (self.OKGREEN + s + self.ENDC)
    def info(self, s):
        print (self.OKBLUE + s + self.ENDC)
    def file(self, fileName, s):
        f = open(fileName, 'w+')
        f.write(s)
        f.close()
