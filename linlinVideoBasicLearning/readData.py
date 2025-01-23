with open("./data.txt", "r", encoding="utf-8") as f:
    # content = f.read()
    # print(content)
    # content = f.readline()
    # while content != '':
    #     print(content)
    #     content = f.readline()
    contents = f.readlines()
    for content in contents:
        print(content)
