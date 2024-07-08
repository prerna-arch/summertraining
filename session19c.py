covid_data_world = {
    "usa": {"active":786167, "serious":403330, "recovered":985},
    "india": {"active":226167, "serious":2344, "recovered":1985},
    "brazil": {"active":961670, "serious":1221670, "recovered":850},
    "italy": {"active":18167, "serious":4433, "recovered":31850},
    "uk": {"active":61670, "serious":672250, "recovered":9090},
}

# Write the Logic to copmute below data
# 1: Total Active
# 2: Total Serious
# 3: Total Recovered

# 4: Min/Max Active/Serious/recovered on Country

# 5: To compute Average of all Active/Serious/Recovered in world

"""
s1=covid_data_world.get("usa")
print(s1)
s2=s1.get("active")
print(s2)
"""

items=list(covid_data_world.values())
totalactive=0
totalserious=0
totalrecovered=0
for i in items:
    s1=i.get("active")
    s2=i.get("serious")
    s3=i.get("recovered")
    totalactive+=s1
    totalserious+=s2
    totalrecovered+=s3
avg1=totalactive/len(items)
avg2=totalserious/len(items)
avg3=totalrecovered/len(items)
print("Total active cases:",totalactive)
print("Total serious cases:",totalserious)
print("Total recovered cases:",totalrecovered)
print("Average of Active cases in world",avg1)
print("Average of serious cases in world",avg2)
print("Average of recovered cases in world",avg3)

values=list(covid_data_world.values())
#print(values)
max=values[0].get("active")
max1=values[0].get("serious")
#print(max)
for i in values:
    s1=i.get("active")
    s2=i.get("serious")
    if s1>max and s2>max1:
        max=s1
        max1=s2
print(" maximum active  cases ",max)
print(" maximum serious cases ",max1)

max2=values[0].get("recovered")
for j in values:
    s1=j.get("recovered")
    if s1>max2:
        max2=s1
print(" maximum recovered  cases ",max2)


values = list(covid_data_world.values())
#print(values)

# Initialize min values with the first element's active and serious cases
min_active = values[0].get("active")
min_serious = values[0].get("serious")
min_recovered=values[0].get("recovered")
# Iterate through the list to find the minimum values
for i in values:
    s1 = i.get("active")
    s2 = i.get("serious")
    s3 = i.get("recovered")
    
    # Update the minimum active cases if a lower value is found
    if s1 < min_active:
        min_active = s1
        
    # Update the minimum serious cases if a lower value is found
    if s2 < min_serious:
        min_serious = s2

    if s3 < min_recovered:
        min_recovered = s3

print("Minimum active cases:", min_active)
print("Minimum serious cases:", min_serious)
print("Minimum recovered cases:", min_recovered)


