array=[]
def Massiv(array):
    number_next=input("Введите число")
    array.append(number_next)
count=input("Сколько элементов в списке?")
for i in range(0,count):
    Massiv(array)

