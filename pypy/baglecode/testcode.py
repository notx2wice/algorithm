#!/usr/bin/python3
# if __name__ == "__main__":
#     print ('구구단 2단')
#     for i in range(10):
#         print ('%d * %d = %d' % (2, i, 2*i) ) # % 뒤에 나열
#     str = 'str.{} {} example'.format('hi','format') #tag가 없으면 순서대로
#     str = "name : {name}, age : {age}".format(age='kim',name=28) #tag가 있음 태그대로
#     name = 'shin'
#     age = 22
#     score = 80
#     result = f'name : {name}, age : {age}, score : {score}'
#     #len(result)  # 문자열 길이 # print (str.count('2'))
#     #모두 소문자
#     print(result.lower())
#     #대문자
#     print(result.upper())
#     #모두 소문자
#     print(result.casefold())
#     #앞만 대문자
#     print(result.title())

#     print(result.strip())
#     print(result.split())
#     print(result.strip().split(':'))

#     print ('o : ', result.find('o')) #기본적으로 왼쪽에서 찾음 rfind는 오른쪽 rindex 마찬가지
#     print ('. : ', result.index(':'))
#     print ('original : ', result.find('original'))
#     print ('just : ' ,result.index('age'))
#     print ('6 :', result.find('6'))      #없는 문자열의 경우 -1 반환
#     #print ('6 :', result.index('6'))  #이놈은 에러  
#     #print (paul_rand.replace('to','TO')) #치환
#     #print (paul_rand.startswith('Do'))
#     #print (paul_rand.endswith('.'))
#     #print (paul_rand.startswith('The')) #이걸로 시작하나
#     #print (paul_rand.endswith('!')) #이걸로 끝나나
#     str = 'ABCDE'
#     print ("=".join(str)) 
#     str = ['Apple','Banana','Cherry']
#     print (', '.join(str))
#     # A=B=C=D=E
#     # Apple, Banana, Cherry
#     str = "12345"
#     print(int(str[0:len(str)])) #12345
#     print(int(str[-1:len(str)])) # a:a 면 str[a]를 출력함
#     print(int(str[0:4]))# a~b a <= 내용물 < b 이무니다.

#     #인풋이 한개일 떄 어떻게 동작하지?
#     # one_input = int(input())
#     # a, b = map(int, input().split())
#     # print(one_input, a, b)
def solution(directory, command):
    answer = []
    for x in directory:
        answer.append(x)

    for cmd in command:
        splited_cmd = cmd.split()
        if splited_cmd[0] == 'mkdir':
            answer.append(splited_cmd[1])

        elif splited_cmd[0] == 'cp':
            #splited_cmd[0] 하위에 있는 폴더드를 수집한다.answer
            temp_list = []
            for xx in answer:
                s = 0
                e = len(splited_cmd[1])
                if len(xx) < e :
                    continue
                if xx[s:e] == splited_cmd[1]:
                    find_last_slash = len(splited_cmd) -1
                    while find_last_slash > 0 :
                        if splited_cmd[1][find_last_slash] == '/':
                            break
                        find_last_slash -= 1
                    added = xx[find_last_slash + 1 : ]
                    print(added)
                    temp_list.append(added)
            
            #수집한 폴더들을 cp 2쨰 인자와 합쳐서 디렉토리 목록에 넣는다.
            for xxx in temp_list:
                if splited_cmd[2] == "/":
                    answer.append("/"+xxx)
                else :
                    answer.append(splited_cmd[2] + "/"+xxx)

        elif splited_cmd[0] == 'rm':
            idx = 0
            end = len(answer)
            while(idx < end):
                s = 0
                if len(answer[idx]) < len(splited_cmd[1]):
                    idx +=1
                    continue
                else:
                    e = len(splited_cmd[1])
                if answer[idx][s:e] == splited_cmd[1]:
                    answer[idx] = "not use ever~~~"
                idx+=1
    #빈칸들을 제거 한다
    start = len(answer) - 1
    
    while (start >= 0):
        if answer[start] == "not use ever~~~":
            answer.pop(start)
        start -= 1
    answer.sort()
    return answer



if __name__ == "__main__":
    directory = ["/", "/hello","/hello/tmp","/root","/root/abcd", "/root/abcd/etc","/root/abcd/hello"]
    command = ["mkdir /root/tmp", "cp /hello /root/tmp", "rm /hello"]

    # directory = ["/"]
    # command = ["mkdir /a", "mkdir /a/b", "mkdir /a/b/c", "cp /a/b /", "rm /a/b/c"]
    print(solution(directory, command))

    strr = " 100 123 122 102 123 123 111 111 111"
    num = list(map(int, strr.split()))
    print(num)
    for x in range(3, len(num) ,3):
        print(x)

