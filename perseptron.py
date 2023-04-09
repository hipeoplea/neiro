import random

data = [random.uniform(0, 1)]
weights = [random.uniform(0, 1), 0.55, 0.35, 0.65]


def activation():
    sum = 0
    for i in range(len(data)):
        sum += data[i] * weights[i]
    print(sum)
    if sum >= 1:
        return 1
    else:
        return 0


print("Идти ли мне на первую пару: отвечай 1 или 0")
data.append(int(input('давно ли ты не появлялась на этом предмете')))
data.append(int(input('давно ли я не появлялась на первой паре')))
data.append(int(input('есть ли долги по этому предмету')))
if activation() == 1:
    print('иди')
else:
    print('не иди')
