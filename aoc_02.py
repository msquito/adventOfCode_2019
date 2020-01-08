# Advent of Code 2019
# Day 02 - intcode program
# https://adventofcode.com/2019/day/2

# read input
file = "02_input.txt"
f = open(file, "r")
for line in f:
    Values = line.split(",")
for i in range(len(Values)):
    Values[i] = int(Values[i])

first = 12
second = 2
target = 19690720

Values[1] = first
Values[2] = second
vc = [x for x in Values]
live = True
rnd = 0

def op(vals, rnd):
    global live
    global vc

    v0 = rnd*4
    v1 = v0+1
    v2 = v0+2
    v3 = v0+3

    if vals[v0] == 1:
        vals[vals[v3]] = vals[vals[v1]] + vals[vals[v2]]
    elif vals[v0] == 2:
        vals[vals[v3]] = vals[vals[v1]] * vals[vals[v2]]
    elif vals[v0] == 99:
        live = False
    else:
        print("err: " + str(vc[0]))
        raise ValueError('Bad OpCode')

# run beyond target in coarse scale, 
# then step back to set up fine scale
while(vc[0] < target):
    vc = [x for x in Values]
    while(live):
        op(vc, rnd)
        rnd+=1
    print(vc[0])
    live = True
    rnd = 0
    Values[1]+=1
print("v[1]: " + str(Values[1]))
Values[1]-=2
print("v[1]: " + str(Values[1]))

# reset
live = True
rnd = 0
vc = [x for x in Values]

# run up to target with finer scale
while(vc[0] < target):
    vc = [x for x in Values]
    while(live):
        op(vc, rnd)
        rnd+=1
    print(vc[0])
    live = True
    rnd = 0
    Values[2]+=1

# output values...
print("v[1]: " + str(vc[1]) + " v[2]: " + str(vc[2]))
