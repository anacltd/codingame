def closest_to_zero():
    temp = []
    n = int(input())
    if n:
        for i in input().split():
            t = int(i)
            if not -273 < t < 5526:
                raise ValueError("Temperature cannot be lower than -273 and superior to 5526")
            temp.append(t)

        t = [(t, abs(t)) for t in temp]
        output = sorted(t, key=lambda x: x[1])
        if len(output) > 1:
            if output[0][1] == output[1][1]:
                new_temp = [output[0][0], output[1][0]]
                result = sorted(new_temp)[-1]
            else:
                result = output[0][0]
        else:
            result = output[0][0]
        print(result)
    else:
        print("0")


if __name__ == '__main__':
    closest_to_zero()
