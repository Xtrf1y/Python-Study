#삭제기능 만들었음#

class filedata:
    def __init__(self, name, locate, date, owner, price):
        self.name = name
        self.locate = locate
        self.date = date
        self.owner = owner
        self.price = price

    def print_data(self):
        print("-----------------------")
        print("물건이름: ", self.name)
        print("물건위치: ", self.locate)
        print("보관날짜: ", self.date)
        print("물건주인: ", self.owner)
        print("물건가격: ", self.price)
        print("-----------------------")

    def searchresult(self, keyword):
        if(keyword in self.name):
            return True
        elif(keyword in self.locate):
            return True
        elif(keyword in self.date):
            return True
        elif(keyword in self.owner):
            return True
        elif(keyword in self.price):
            return True
        else:
            return False


def set_data():
    name = input("물건이름: ")
    locate = input("물건위치: ")
    date = input("보관날짜: ")
    owner = input("물건주인 : ")
    price = input("물건가격 : ")
    data = filedata(name, locate, date, owner, price)
    return data


def print_menu():
    print("<메뉴>")
    print("1)등록")
    print("2)조회")
    print("3)검색")
    print("4)종료")
    answer = int(input("선택하세요 :"))
    return int(answer)


def run():
    data_list = []
    while 1:
        answer = print_menu()
        if answer == 1:
            data = set_data()
            data_list.append(data)
        elif answer == 2:
            print_data_2(data_list)
        elif answer == 3:
            keyword = str(input("찾고 싶으신 키워드를 입력해주세요 :"))
            countdown = 0
            for data in data_list:
                if data.searchresult(keyword):
                    data.print_data()
                    countdown += 1
            if countdown == 0:
                print("값이 없습니다")
        elif answer == 4:
            break


def print_data_2(data_list):
    for data in data_list:
        data.print_data()


if __name__ == "__main__":
    run()
