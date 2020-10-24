# 선형 리스트 구현하기 (카톡  친구들)
katok = []

# 배열의 제일 뒤에 친구를 추가하는 함수
def add_data(friend):
    katok.append(None)  # 빈칸을 추가
    kLen = len(katok)   # 배열의 전체 길이
    katok[kLen-1] = friend

add_data('다현')
add_data('정연')
add_data('쯔위')
print(katok)