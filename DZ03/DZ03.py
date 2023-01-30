n = int (input("Введите шестизначное число "))
d = list(map(int, list(f'{n:06}'))) 
print(('NO', 'YES')[sum(d[:3])==sum(d[3:])])