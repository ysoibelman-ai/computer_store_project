def valid_str(string):
    return string.strip()

def valid_num(num):
    try:
        int(num)>0
        if int(num) > 0:
            return True
        else:
            print ("number must be larger than 0")
            return False
    except ValueError:
        print ("must be a number")
        return False