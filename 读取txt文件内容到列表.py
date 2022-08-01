import os


def get_content(filename):
    base_path = os.getcwd()
    file = os.path.join(base_path,filename)
    key_list = []
    flag = 1
    count = 0
    with open(file, "r" ,encoding="UTF-8") as fo:
        while flag == 1:
            content = fo.readline().rstrip("\n")
            key_list.append(content)
            if key_list[count] == "":
                del key_list[count]
                break
            count += 1
    return key_list
# key_list = get_content("1.txt")
# print(key_list)

