def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        rotated = s1[i:] + s1[:i]
        print("s1[i:] ",s1[i:])
        print("s1[:i] ",s1[:i])
        print("rotated ",rotated)

        if rotated == s2:
            return True

    return False


s1 = "abcd"
s2 = "cdab"

print(is_rotation(s1, s2))