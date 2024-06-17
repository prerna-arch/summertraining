john_friends = {"joe","jim","fionna","harry","kim","joe"}
sia_friends = {"joe","george","fionna","leo","jack","ben"}

print(john_friends)
print(sia_friends)

mutual_friends = john_friends & sia_friends

print (mutual_friends)

# error:set does not support indexing.it works on hashing.
#print(john_friends[0])
#hence ,we can not get the data from set.