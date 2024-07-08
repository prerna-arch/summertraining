
#strings are immutable->they can not be changed

quote="be exceptional"
print("hasdcode of quote is:",id(quote))
s1=quote.upper()
print("1.quote is:",quote)
print("1.hashcode ",id(quote))

s2=quote.lower()
print("2.quote is:",quote)
print("2.hashcode ",id(quote))

print(s1)
print(s2)

s3=quote.capitalize()
print(s3)

s4=quote.title()
print("s4:",s4)

quote="Be Exceptional"
s5=quote.swapcase()
print("s5 :",s5)