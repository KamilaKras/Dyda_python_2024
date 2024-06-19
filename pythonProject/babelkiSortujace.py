NIU = [8, 2, 3, 5]

length = len(NIU)

print(f"Wyjściowa lista: {NIU}")

for i in range(length):
    for j in range(0, length-i-1):
        if NIU[j] > NIU[j+1]:
            NIU[j], NIU[j+1] = NIU[j+1], NIU[j]
print(f"Lista posortowana rosnąco: {NIU}")


for i in range(length):
    for j in range(0, length-i-1):
        if NIU[j] < NIU[j+1]:
            NIU[j], NIU[j+1] = NIU[j+1], NIU[j]
print(f"Lista posortowana malejąco: {NIU}")