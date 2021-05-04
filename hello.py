stock_values = [100, 60, 70, 80, 85, 70]
N = 6
result = [ ]
present_value = 0

for i in range(N):
    if i == 0:
        result.append(1)
        present_value = stock_values[i]
    elif present_value > stock_values[i]:
        result.append(1)
        present_value = stock_values[i]
    else:
        count = 0
        for j in range(i):
            if stock_values[i] > stock_values[i-1]:
              count =  count + 1
            else:
                break
        result.append(count)
        present_value = stock_values[i]

print(*result)