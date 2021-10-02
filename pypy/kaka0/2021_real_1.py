def solution(new_id):
    in_id = new_id
    # print(in_id)
    rower_id = in_id.lower()
    # print(rower_id)
    remove_id = str()
    for x in rower_id:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            remove_id += x
        if x == '-' or x == '_' or x == '.':
            remove_id += x
        if ord(x) >= ord('0') and ord(x) <= ord('9'):
            remove_id += x

    one_dot = str()
    idx = 0
    while idx < len(remove_id):
        one_dot += remove_id[idx]

        if remove_id[idx] == '.':
            while idx < len(remove_id) and remove_id[idx] == '.' :
               idx += 1
            continue
        idx += 1

    one_dot = one_dot.strip('.')
    if len(one_dot) == 0:
        one_dot = "a"
    if len(one_dot) >= 16:
        one_dot = one_dot[0:15]
    if one_dot[-1] == '.':
        one_dot = one_dot[0: -1]
    if len(one_dot) <= 2:
        while len(one_dot) <3:
            one_dot += one_dot[-1]
    return one_dot

if __name__ == '__main__':
    new_id = "...!@BaT#*..y.abcdefghijklm"
    print(solution(new_id))
    new_id ="z-+.^."
    print(solution(new_id))
    new_id = "=.="
    print(solution(new_id))
    new_id = "123_.def"
    print(solution(new_id))
    new_id = "abcdefghijklmn.p"
    print(solution(new_id))