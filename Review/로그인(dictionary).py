# users 정보(dictionaly)
users = {
    "user1":"1234",
    "user2":"1234",
    "user3":"1234",
}

def get_user_info():
    user_id = input("ID입력: ")
    user_pw = input("PW입력: ")
    return user_id, user_pw

def check_login(user_id, user_pw):
    if user_id not in users.keys():
        print(f"{user_id}는 없는 ID")
        return False
    elif user_pw == users[user_id]:
        return True
    else:
        print("비밀번호 틀림")
        return False

def print_result(result):
    if result:
        print("로그인 성공")
    else:
        print("로그인 실패")


def main():
    result = False

    for _ in range(3):
        id, password = get_user_info()
        result = check_login(id,password)
        if result:
            break
    print_result(result)


def sign_up():
    while True:
        new_id = input("ID 입력: ")
        if new_id in users.keys():
            print("이미 존재하는 ID")
        else:
            new_pw = input("PW 입력: ")
            users[new_id] = new_pw
            break


main()