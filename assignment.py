class LikeLion:
    def __init__(self,name,number,gender):
        self.name = name
        self.number = number
        self.gender = gender

    def introduce(self):
        print("이름은 %s, 전화번호는 %s, 성별은 %s입니다." %(self.name, self.number, self.gender))

myList=[]   

while True:

    name = input("이름을 입력하세요: ")
    if name == "그만":
        for x in myList:
            x.introduce()
        break

    number = input("전화번호를 입력하세요 : ")
    gender = input("성별을 입력하세요(male이나 female로 작성해주세요) : ")
    if gender == "male" or gender == "female":
        gender = gender
    else:
        gender = 'unknown'

    one = LikeLion(name,number,gender)
    myList.append(one)

    for x in myList:
        x.introduce()
    print("\n")