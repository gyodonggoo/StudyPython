f = open("./data/basic.txt", "w")
f.write("hello python")
f.close

f1 = open("./data/basic.txt", "a")
f1.write("Added document")
f.close

with open("./data/test.txt", "W") as f3:
    f3.write("with sentence document")

