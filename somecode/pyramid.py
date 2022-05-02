# Print a pyramid by *
n = int(input('Please input an integer between 1~10:  ' ))
print('')
for idx in range(n): print(' '*(n-idx) + '*'*(idx*2+1))
    
    #nst=idx*2+1
    #nsp=n-idx  # 即[(n*2-1)-nst]*0.5 再加開頭空格
    #fp =' '*nsp + '*'*nst
    #print(fp)