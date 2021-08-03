
while True:
    a = int(input('숫자 입력 : '))
    if a == 7:
        print('7입력! 종료')
        break
    else:
        int(input('다시 입력 : '))

coin = 10000
n = 0
while 1:
    n += 1
    print('노래를 %d 곡 블렀습니다. ' % n)
    coin -= 2000
    print('잔액은 %d 원 입니다.' % coin)

    if coin == 0:
        print('찬액이 없습니다. 종료합니다.')
        break
nameL=[]
for i in range(3):
    name=input('회원 입력 : ')
    nameL.append(name)
print('회원 명단 : ', *nameL)

num = int(input('학생수 입력 : '))
scores = []
total = high = 0
for i in range(num):
    score = int(input('학생'+str(i+1)+'의 점수를 입력하세요. :'))
    scores.append(score)
    total += score
    if score >= 80:
        high += 1
print('총점 : %d ' % total)
print('평균 : %.2f ' % (total/num))
print('80점 이상인 학생 : %d명' % high)

products=[]
while True:
    product=input('상품 등록(엔터키 누르면 종료) : ')
    if product =='':
        break
    else:
        products.append(product)

print('등록된 상품 : ',*products)

num = int(input('학생수 입력 : '))
scores = []
total = high = 0
for i in range(num):
    score = int(input('학생'+str(i+1)+'의 점수를 입력하세요. :'))
    scores.append(score)
    total += score
    if score >= 80:
        high += 1
scores.sort()
print('총점 : %d ' % total)
print('평균 : %.2f ' % (total/num))
print('80점 이상인 학생 : %d명' % high)
print('점수 내림차순 정열: ', *scores)


import random

answer_4=["개과천선","구사일생","군계일학","무용지물","동고동락",
          "유비무환","입신양명","괄목상대","막역지우","고장난명"]
story=['잘못을 고치고 옳은 길에 들어섬',
       '죽을 고비를 여러번 겪으며 살아나다.',
       '평범한 사람 가운데 뛰어난 사람',
       '아무 짝에나 쓸모 없는 것',
       '고통과 즐거움을 함께 한다.',
       '미리 준비해두면 근심걱정이 없다.',
       '사회적으로 인정받고 출세하여 이름을 세상에 드날림',
       '다른 사람의 학식이나 업적이 크게 진보한 것을 말함',
       '생사를 같이할 수 있는 친밀한 벗',
       '상대없이 혼자서는 어떤 일을 이룰 수 없다.']
print('사자성어 맞추기 게임을 시작합니다.')
print('-'*20)
while True:
       i = random.randint(0, 10)
       print(story[i])
       answer = input('이 말의 사자성어는? : ')
       if answer_4[i] == answer:
              print('정압입니다. 게임을 종료합니다.')
              break
       else:
              print('틀렸습니다....다시 도전')
students=[
    {'name': '홍길동', 'korean': 87, 'mate': 98, 'english': 88, 'science': 95},
    {'name': '이몽룡', 'korean': 92, 'mate': 98, 'english': 96, 'science': 98},
    {'name': '성춘향', 'korean': 76, 'mate': 96, 'english': 94, 'science': 90},
    {'name': '변학도', 'korean': 98, 'mate': 92, 'english': 96, 'science': 92},
    {'name': '박지성', 'korean': 95, 'mate': 98, 'english': 98, 'science': 98},
    {'name': '류현진', 'korean': 64, 'mate': 88, 'english': 92, 'science': 92}
]
print('이름\t\t총점\t\t평균')
for student in students:
    # total = avg = 0
    # for i in student.keys():
    #     if i == 'name':
    #         name = student[i]
    #     else:
    #         total += student[i]
    # avg=total/4
    # print(print('{0}\t{1}\t\t{2:.2f}'.format(name, total, avg)))
    total=sum(list(student.values())[1:5])
    avg=total/4
    print('{0}\t{1}\t\t{2:.2f}'.format(student['name'],total,avg))

mydic=dict()
while True:
    word=input('영어 단어 등록 (종료는 quit) : ')
    if word == 'quit':
        break
    elif word in mydic:
        print(word+'는 이미 등록된 단어입니다.')
    else:
        mean = input(word + '의 뜻입력 (종료는 quit) :')
        mydic[word]=mean
while True:
    search =input('검색할 단어 입력 (종료는 quit) : ')
    if search == 'quit':
        print('종료합니다.')
        break
    elif search not in mydic:
        print(search+ '는 사전에 없는 단어입니다.')
    else:
        print(search+'의 뜻은 '+mydic[search]+'입니다.')
cat_song = "my cat has blue eyes, my cat is cute"
print({i:j for j,i in enumerate(cat_song.split())})

colors = ['orange', 'pink', 'brown', 'black', 'white']
result = '&'.join(colors)
print(result)
result = [i for i in range(10) if i%2 == 0]
print(result)

items = 'zero one two three'.split("two")
result =[i for i in range(10)]
print(result)

animal = ['Fox', 'Dog', 'Cat', 'Monkey', 'Horse', 'Panda', 'Owl']
print([ani for ani in animal if 'o' not in ani])

name = "Hanbit University"
student = ["Hong", "Gil", "Dong"]
split_name = name.split()
join_student = ''.join(student)
print(join_student[-4:] + split_name[1])

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]
print(midterm_score[0][2])

a = [1, 2, 3]
b = [4, 5, ]
c = [7, 8, 9]
print([[sum(k), len(k)] for k in zip(a, b, c)])

kor_score = [30, 79, 20, 100, 80]
math_score = [43, 59, 0, 30, 90]
eng_score = [49, 72, 48, 67, 15]
midterm_score = [kor_score, math_score, eng_score]
print ("score:",midterm_score[2][1])

alist = ["a", "b", "c"]
blist = ["1", "2", "3"]
abcd= []
for a, b in enumerate(zip(alist, blist)):
     try:
         abcd.append(b[a])
     except IndexError:
         abcd.append("error")
print(abcd)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
nums = [i for i in range(20)]
answer = [alpha+str(num) for alpha in alphabet for num in nums if num%2==0]
print(len(answer))