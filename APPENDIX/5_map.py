"""
--- input과 map함수이용 예제 ---

input() ->  데이터를 입력받음
: 90 80 99 100 88   -- string

input().split() -> 입력받은 문자열을 공백으로 나눠서 리스트로 바꿈
: [99,80,99,100,88]   -- string

map(int, input().split()) ->  위의 리스트 모든 elements에 int()함수 적용  
: 99 80 99 100 88   -- integer

list(map(int,input().split()))  ->  위의 값을 list로 저장
: [99,80,99,100,88]   -- integer


학생의 성적데이터를 내림차순으로 정렬
첫 번째 줄에 데이터의 수(학생 수) 입력, 다음 줄에는 처리할 데이터
정보는 공백으로 구분

"""

n = int(input("데이터 개수 입력: "))

data = list(map(int,input("데이터 입력(띄어쓰기로 구분): ").split()))
data.sort(reverse=True)
print(data)

# n,m,k를 공백으로 구분하여 입력
n, m, k = map(int, input("n, m ,k 입력(콤마로 구분): ").split(","))
print(f"n={n}, m={m}, k={k}")

"""
입력 수가 많은 경우 input()함수는 동작이 느려서 시간 초과가 될 수 있다.
이 경우 sys 라이브러리에 정의되어 있는 sys.stdin.readline()을 사용한다.

"""