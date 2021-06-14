def input_validation(string):
    if string.isnumeric():
        return split_string(string)
    elif string.isalnum():
        return "you have enter alphanumeric"
    else:
        return "please Enter Number"

def split_string(string):
    result = 0
    result_string = ""
    for i in range(len(string)):
        for j in range(len(string)-1,-1,-1):
            s = string[i:j+1]
            length_s = len(s)
            if length_s != 0 and length_s%2 == 0:
                result1 = finding_sum(s)
                if result < result1:
                    result_string = s
                    result = result1
    return result                           #return result,result_string

def finding_sum(s):
    first_sum = 0
    last_sum = 0
    length_s = len(s)
    
    for i in range(length_s):
        if i < length_s//2:
            first_sum += int(s[i])
        else:
            last_sum += int(s[i])
    if first_sum == last_sum:
        return length_s
    else:
        return 0
