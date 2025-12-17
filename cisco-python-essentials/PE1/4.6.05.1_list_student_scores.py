school_class = {}

while True:
    name = input("Enter the student's name: ")
    if not name:
        break
    
    try:
        score = float(input("Enter the student's score: "))
    except:
        break

    if score not in range(0, 11):
        break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class.update({name:(score, )})
    
for name in school_class:
    total = count = 0
    for score in school_class[name]:
        total += score
        count += 1
    print(f"{name}: {total / count}")