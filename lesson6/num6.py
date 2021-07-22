print("6 Задание")
file_1 = open('bakery.csv', 'a', encoding='utf-8')
file_2 = open('bakery.csv', 'r', encoding='utf-8')
content = file_2.readlines()
length = len(content)
if length > 1 and [i for i in content[1:] if i.replace(".", "").isdigit()]:
    if length == 3:
        print(*file_2.read().split()[int(file_2[1]) - 1:int(file_2[2])], sep='\n')
    if "," in file_2[1] or "." in file_2[1]:
        file_2.read()
        print(content[1], file=file_1)
    else:
        print(*file_2.readlines()[int(file_2[1])-1:], sep="")
else:
    print(file_2.read())
file_1.close()
file_2.close()
