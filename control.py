array=[]
def Massiv(array):
    number_next=int(input("Введите число: "))
    array.append(number_next)
count=int(input("Введите сколько элементов в списке:"))
for i in range(0,count):
    Massiv(array)
print(array)
if count < 3:
    array=[]
elif count == 3:
    array_beta=[]
    for i in array:
        for y in range(0,1):
            array_beta.append(i)
    array=array_beta
elif count > 3 :
    count_2=0
    array_beta=[]
    for i in array:
        count_2+=1
        if count_2 > 1 and count_2 < 5:
            array_beta.append(i)
    array=array_beta
print(array)

