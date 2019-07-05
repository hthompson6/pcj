# (Blind) Using data structure
def test_unique_ds(test_str):
    store_arr = []
    for char_val in test_str:
        if char_val in store_arr:
            return False
        else:
            store_arr.append(char_val)
    return True


# (Blind) Not using data structure
def test_unique(test_str):
    cnt = len(test_str)
    i = 0
    while (i < cnt):
        char_val = test_str[i]
        test_str = test_str[i+1:]
        ret = test_str.replace(char_val, '')
        if ret != test_str:
            return False
        cnt = len(test_str)
        i += 1
    return True
    

unique_str = "abcdefg"
non_unique_str = "aabbccddeeffgg"

print(test_unique(unique_str))
print(test_unique(non_unique_str))

print(test_unique_ds(unique_str))
print(test_unique_ds(non_unique_str))