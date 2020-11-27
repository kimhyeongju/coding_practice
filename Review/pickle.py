import pickle

def save(fpath, data):
    try:
        with open(fpath, 'wb') as file:
            pickle.dump(data,file)
    except Exception as e:
        print(f"{fpath}파일 쓰기에 실패했습니다.")
        print(e)

def load(fpath):
    try:
        with open(fpath, 'rb') as file:
            data = pickle.load(file)
            return data
    except:
        print(f"{fpath}파일 읽기에 실패했습니다.")

def main():
    data = [
        [1,2,3,54,45],
        [7,8,3,4,5],
        [1,12,13,4,25]
    ]

    save("./data/data2.dat", data)

    data2 = load("./data/data2.dat")
    print(data2)

main()

import shutil
shutil.copy("live.txt","live2.txt")