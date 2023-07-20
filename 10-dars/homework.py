with open("uy.txt", 'r') as file:
    for i, line in enumerate(file, 1):
        if i == 10:
            print(line.strip())
            break
    else:
        print("Faylda 10 dan kam satr mavjud.")


