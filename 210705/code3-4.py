def add_data(friend):
    katok.append(None)
    klen = len(katok)
    katok[klen-1] = friend


def insert_data(position, friend):
    katok.append(None)
    klen = len(katok)
    for i in range(klen-1, position, -1):
        katok[i]=katok[i-1]
        katok[i-1] = None
    katok[position] = friend


def del_data(position):
    katok[position] = None
    klen = len(katok)
    for i in range(position+1, klen, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[klen-1])


katok=[]

if __name__ == '__main__':
    while True:
        select = int(input('선택하세요(1:추가 2: 삽입 3:삭제 4: 종료)-->'))
        if select == 1:
            friend = input('추가할 데이터--> ')
            add_data(friend)
            print(katok)
        elif select == 2:
            friend = input('추가할 데이터--> ')
            position = int(input('추가할 위치--> '))
            insert_data(position, friend)
            print(katok)
        elif select == 3:
            position = int(input('삭제할 위치--> '))
            del_data(position)
            print(katok)
        elif select == 4:
            print(katok)
            break
        else:
            print('1~4 중 입력하세요.')
            continue