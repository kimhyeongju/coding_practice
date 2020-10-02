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


