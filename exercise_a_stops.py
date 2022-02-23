from operator import index


stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list

stops.append ('Edinburgh Waverley')


#2. Add "Glasgow Queen St" to the start of the list

stops.insert (0, 'Glasgow Queen St')


#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")

index_of_linlithgow = stops.index ('Linlithgow')

stops.insert (index_of_linlithgow, 'Polmont')


#4. Print out the index position of "Linlithgow"

print (index_of_linlithgow)


#5. Remove "Livingston" from the list using its name

stops.remove ('Livingston')


#6. Delete "Cumbernauld" from the list by index

index_of_cumbernauld = stops.index ('Cumbernauld')
print(index_of_cumbernauld)
stops.pop(index_of_cumbernauld)


#7. Print the number of stops there are in the list

total_stops = len(stops)
print (total_stops)


#8. Sort the list alphabetically

print (sorted(stops))


#9. Reverse the positions of the stops in the list

print (sorted(stops, reverse = True))


#10 Print out all the stops using a for loop

for town in stops:
    print(town)
