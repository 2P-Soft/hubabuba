import arktika
def hiza(health):
     if (health < 0):
           print("Собака Алишера мертва")
     else :
           print("Еще жива")


print("ОС Зеленая хуба-буба")
print("Выберите дейтсвие ОС:")
print("1.Гусь")
print("2.2-Кинотеатр")
print("3.Сервис эл-почты Почта и точка")
print("4.2-АРКТИКА")
print("5.2Tube")
print("6.2Школа")
choose = input(":")
if (choose == "1"):
    a = "goose"
    print(a)
    
if (choose == "2"):
    print("2 Кинотеатр 0.0.1")
    print("Название фильма")
    filmname = input(":")
    print("Введите адрес кинотеатра KINOSTAR(R)")
    kinoteat = input(":")
    print("Время")
    vremya = input(":")
    print("Билет на",filmname,"в кинотеатре",kinoteat,"на время",vremya,"забронирован")
    
if (choose == "3"):
    
    print("ПОЧТА И ТОЧКА Введите адрес")
    pochta = input(":")
    print("LOGIN:")
    login = input(":")
    if ("@" in pochta and "@" not in login):
        print("Успешная регистрация в ПОЧТА И ТОЧКА")
if (choose == "4"):
         arktika.arktikastart()
if (choose == "5"):
         name = input("ИМЯ")
         print("Возраст")
         age = input()
         agei = int(age)
         if (agei < 18):
                  print("Доступ запрещен!Родительский контроль! Вы,", name , "не можете смотреть в 2-Tube!")
         else :
                  
                  print("Добро пожаловать в 2-Tube, ", name, "Узнайте подробнее о продуктах 2`C на сайте http://openvk.su/twop")

if (choose == "6"):
    at = int(input())
    print(at*at*at)
    print(6*at*at)
    
                  


                  
         
    
        

                


                
