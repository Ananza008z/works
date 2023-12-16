import string

str_lst = [c for c in string.ascii_uppercase]

global en_pass
def encode(passage1):
    return ''.join([str_lst[str_lst.index(c)-1] for c in passage1])
def decode():
    pass

passage = [str(char) for char in input()]
print(encode(passage))