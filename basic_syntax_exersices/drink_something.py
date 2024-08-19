person_age = int(input())
output = ""
kid_drink = "drink toddy"
teen_drink = "drink coke"
yound_adults_drink = "drink beer"
adults_drink = "drink whisky"

if person_age <= 14:
    output = kid_drink
elif person_age <= 18:
    output = teen_drink
elif person_age <= 21:
    output = yound_adults_drink
elif person_age > 21:
    output = adults_drink

print(output)

