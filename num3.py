print("3 Задание")
file_1 = open('users.csv', 'r', encoding='utf-8')
file_2 = open('hobby.csv', 'r', encoding='utf-8')
content = file_1.readlines()
content_2 = file_2.readlines()
length = len(content)
arr = []
arr_2 = []
for i in range(length):
    arr.append(content[i].split()[0])
    arr_2.append(content_2[i].split()[0])
if len(content) > len(content_2):
    print(1)
else:
    ans = {}
    for j in range(length):
        ans.update({arr[j] : arr_2[j]})
print(ans)
file_1.close()
file_2.close()