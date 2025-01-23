with open("poem.txt", "w", encoding="utf-8") as f:
    f.write("hello\nmy name is brant\nnice to meet you\n")

with open("poem.txt", "a", encoding="utf-8") as f:
    f.write("this is new line\nhahaha")
