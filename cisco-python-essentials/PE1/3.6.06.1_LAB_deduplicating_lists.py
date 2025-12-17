hardcoded = [3, 6, 3, 5, 6, 2, 5, 7, 3, 5, 2, 4, 4, 4]

# Make a copy of the content in memory instead
# of referencing the same content in memory
temp = hardcoded[:]

# Get a number from the list
for i in range(len(temp) - 1):
    #print('i', i, temp)
    # Get the next number in the list
    for j in range(i + 1, len(temp)):
        #print('j', j, temp)
        try:
            while True:
                # Compare current number with the next number
                if temp[i] == temp[j]:
                    # If True, delete the next number then
                    # try again with the new next number
                    del temp[j]
                    #print(temp)
                else:
                    # Break when all of the duplicates of
                    # the current number have been removed
                    break
        except IndexError:
            # Ignore any IndexErrors and continue
            pass

print(f"""Original:  {hardcoded}
Processed: {temp}""")
