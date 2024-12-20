"""
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
             (nav)            (5)          (1)            (!)

예) 생겅된 비밀번호 : nav51!
"""

# 내 답안
url = "http://naver.com"
url = url[7:]
index = url.index(".")
url = url[:index]
password = url[:3] + str(len(url)) + str(url.count("e")) + "!"
print(password)


# 나도코딩 답안
url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = url[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다." .format(url, password))

