def closest_to_zero(temperatures):
    t = [(temp, abs(temp)) for temp in temperatures]
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
    return result


if __name__ == '__main__':
    n = int(input())
    if n:
        temp = []
        for i in input().split():
            t = int(i)
            if not -273 < t < 5526:
                raise ValueError("Temperature cannot be lower than -273 and superior to 5526")
            temp.append(t)
        closest_to_zero(temp)
    else:
        print("0")
