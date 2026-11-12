from application.validations import valid_num,valid_str
def get_str(msg=""):
    while True:
        string = input(msg)
        if valid_str(string):
            return string
        else:
            print ("string musy not be empty")
        
def get_num (msg,):
    while True:
        num = input(msg)
        if valid_num(num):
            return int(num)