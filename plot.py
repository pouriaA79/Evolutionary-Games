from matplotlib import pyplot as plt


f = open("socres.txt","r")
Lines = f.readlines()
max_score = []
avg_score = []
min_score = []

for i in range(len(Lines)):
    Line=Lines[i].split(" ")
    max_score.append(float(Line[0]))
    avg_score.append(float(Line[1]))
    x= Line[2][0:-1]
    min_score.append(float(Line[2]))

plt.plot(max_score, label="max")
plt.plot(min_score, label="min")
plt.plot(avg_score, label="avg")
plt.xlabel("generation")
plt.ylabel("fitness")
plt.legend()
plt.show()
