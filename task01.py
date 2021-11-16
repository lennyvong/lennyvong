def robotProgram():
    max = 16
    goal = 15
    victory = "Success !"
    retry = "Not yet"

    for i in range(0, max):
        if (i == goal):
            return victory
    print(i, retry)

assert(robotProgram() == 'Success !'), "File is still corrupted"
print("The file isn't corrupted anymore, good job !")