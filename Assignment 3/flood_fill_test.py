import random
import solution

inputs = [[]]*10
outputs = ['']*10

inputs[0] = [
    "3 2", "3 1", "2 1", "1 2"
]
outputs[0] = "N"

inputs[1] = [
    "3 1", "3 1", "2 1"
]
outputs[1] = "Y"

inputs[2] = ["10 8" , "5 2"] + ["{} {}".format(9-i,i) for i in range(1,9)]
outputs[2] = "N"

inputs[3] = ["10 7" , "5 2"] + ["{} {}".format(9-i,i) for i in range(1,9)][:-1]
outputs[3] = "Y"

inputs[4] = ["1000 250000", "2 2"] + ["{} {}".format(i+251,j+251) for i in range(500) for j in range(500)]
outputs[4] = "Y"

inputs[5] = ["1000 250000", "2 2"]
for i in range(250000):
    x = random.randint(1,1000)
    y = random.randint(1,1000)
    inputs[5].append("{} {}".format(x,y))
outputs[5] = solution.get_answer(inputs[5])

inputs[6] = ["40 0", "24 4"]
outputs[6] = "Y"

inputs[7] = ["83 6888", "1 1"] + ["{} {}".format(i,j) for i in range(2,84) for j in range(2,84)] + ["{} 1".format(i) for i in range(2, 84)] + ["1 {}".format(i) for i in range(2,84)]
outputs[7] = "Y"

for t in range(2):
    print("Generating {} input".format(9+t))
    n = random.randint(1,1000)
    b = random.randint(1,20000)
    i_x = random.randint(1,n)
    i_y = random.randint(1,n)
    inputs[8+t] = ["{} {}".format(n,b), "{} {}".format(i_x, i_y)]
    count = 0
    while count < b:
        x = random.randint(1,n)
        y = random.randint(1,n)
        if x != i_x and y != i_y:
            inputs[8+t].append("{} {}".format(x,y))
            count = count+1
    outputs[8+t] = solution.get_answer(inputs[8+t])

for i in range(10):
    f_input = open("input{:02d}.txt".format(i), "w")
    f_output = open("output{:02d}.txt".format(i), "w")

    actual_inputs = []
    for l in inputs[i]:
        actual_inputs.append(l+"\n")

    f_input.writelines(actual_inputs)
    f_output.write(outputs[i])

    f_input.close()
    f_output.close()

for i in range(4):
    if outputs[i] != solution.get_answer(inputs[i]):
        print("Wrong answer for {}".format(i))