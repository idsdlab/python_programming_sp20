# prob5. string compression

def convert_small(alphabet):
    return alphabet.lower()

def compress_str(s):
    answer = ''
    s_len = len(s)
    boss = convert_small(s[0])
    cnt = 1
    for i in range(1, s_len):
        if convert_small(s[i]) == boss:
            cnt += 1
        else:
            answer += boss
            answer += str(cnt)
            boss = convert_small(s[i])
            cnt = 1

    answer += boss
    answer += str(cnt)
    return answer

if __name__ == '__main__':
    print('string compression')
    sentence = input('문자열 s를 입력하세요 : ')

    comp_str = compress_str(s=sentence)

    print('compressed string : %s' % comp_str)