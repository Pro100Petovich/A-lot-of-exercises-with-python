print("1 Задание")
file_1 = open('nginx.txt', 'r', encoding='utf-8')
content = file_1.readlines()
re_content = []
for i in range(len(content)):
    re_content.append((content[i].split()[0], content[i].split()[5][1:], content[i].split()[6]))
print(re_content)
file_1.close()
