#!/usr/bin/python3

if __name__ == "__main__":
    str1 = "hi"
    str2 = "it's me"
    print(str1, str2)
    print ('구구단 2단')
    for i in range(10):
        print ('%d * %d = %d' % (2, i, 2*i) ) # % 뒤에 나열
    
    str = 'str.{} {}example'.format('hi','format') #tag가 없으면 순서대로
    print(str)


    str = "name : {name}, age : {age}".format(age='kim',name=28) #tag가 있음 태그대로
    print (str)

    name = 'shin'
    age = 22
    score = 80

    result = f'name : {name}, age : {age}, score : {score}'
    print (result)

    print (len(result))
    print (str.count('2'))
    
    #모두 소문자
    print(result.lower())
    #대문자
    print(result.upper())
    #모두 소문자
    print(result.casefold())
    #앞만 대문자
    print(result.title())
    print(result.strip())
    print(result.split())
    print(result.strip().split(':'))

    print ('o : ', result.find('o')) #기본적으로 왼쪽에서 찾음 rfind는 오른쪽 rindex 마찬가지
    print ('. : ', result.index(':'))
    print ('original : ', result.find('original'))
    print ('just : ' ,result.index('age'))

    print ('6 :', result.find('6'))      #없는 문자열의 경우 -1 반환
    #print ('6 :', result.index('6'))  #이놈은 에러  
    #print (paul_rand.replace('to','TO')) #치환
    #print (paul_rand.startswith('Do'))
    #print (paul_rand.endswith('.'))

    #print (paul_rand.startswith('The')) #이걸로 시작하나
    #print (paul_rand.endswith('!')) #이걸로 끝나나
    str = 'ABCDE'
    print ("=".join(str)) 

    str = ['Apple','Banana','Cherry']
    print (', '.join(str))
    # A=B=C=D=E
    # Apple, Banana, Cherry

    str = "u 123"
    print( int(str[2:len(str) ]))
    print( 999 // 500)