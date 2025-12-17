beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)

for i in range(2): # not ideal for this task but okay...
    if i == 0:
        name = input("Add Stu Sutcliffe to The Beatles: ")
    elif i == 1:
        name = input("Add Pete Best to The Beatles: ")
    beatles.append(name)
print(beatles)

del beatles[3:]
print(beatles)

beatles.insert(0, "Ringo Starr")
print(beatles)
