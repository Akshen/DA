import time
t = time.time()
def func(N):
    dict_p ={}
    for i in range(1, N+1):
        temp_l = [1]
        if i == 1:
            dict_p[i] = 1
        else:
            dp = dict_p.get(i-1)
            for x in range(len(dp)):
                if x != len(dp)-1:
                    try:
                        temp_l.append((dp[x]+ dp[x+1]))
                    except:
                        pass
                else:
                    temp_l.append(1)

        dict_p[i] = temp_l
    return dict_p

if __name__ == '__main__':
    ans = func(int(input('Please Enter Value for Pascal triangle\n')))
    print('*'*50)
    for i,j in ans.items():
        print(*j, sep=' ')
    print('*'*50)
    print('Time take to execute above program')
    print(time.time() - t)
