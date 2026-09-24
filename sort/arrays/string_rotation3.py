# s1 = "abcd"

# s1 + s1 = "abcdabcd"

# Now look for: "cdab"

# It exists inside:

# abcdabcd
#   cdab


def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
     
    doubled = s1 + s1

    return s2 in doubled


s1 = "abcd"
s2 = "cdab"

print(is_rotation(s1, s2))