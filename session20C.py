password=" hello "
print(password,len(password))
p1=password.strip()
print(p1,len(p1))

data="0008765700"
s1=data.strip("0")
print(s1)
print(data)



message="no internet connection"
print(message)
print(message.center(50))
print(message.ljust(50))
print(message.rjust(50))


amount=545
data=str(amount).zfill(8)
print("data is:",data)


quote="search the candle rather than cursing the darkness"
idx1=quote.find("the")
idx2=quote.find("dark")
print("idx1:",idx1)
print("idx2:",idx2)

