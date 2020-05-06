teams = open("teams.txt", "r")
for i in range(5):
    if i == 1:
        print(teams.readline(1))
    elif i == 4:
        print(teams.readline(4))
    else:
        continue



teams.cloes