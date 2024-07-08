#Properties

"""
Indexing
negative indexing
slicing
concatenation
Multiplicity
Membership testing
"""
quote="search the candle rather than cursing the darkness"
#indexing
print(quote[1])
print(quote[-1])
print(quote[-8:])
#concatenation
data=quote+"\n" +"Be exceptional \n"
print(data)

#multiplicity
quote=quote*3
print(quote)

#membership testing
print("the"in quote)

email=input("enter your email:")
if "@" in email and"." in email:
    print("email is well formed",email)
else:
    print("email is not well formed",email)


contacts=["john","sia","ben"]
search=input("enter search keyword")
for contact in contacts:
    if contact
     