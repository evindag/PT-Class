sayilar = [1,3,5,7,9,12,19,21]
#hangi sayılar 3'ün katıdır?
for sayi in sayilar:
    if(sayi%3==0):
        print(sayi)
#listedeki tek sayıların karesini alın.
for sayi in sayilar:
    if(sayi%2==1):
        print(sayi**2)
