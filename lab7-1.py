# Не Изменяемые
int 
float
str
bool
tuple

# Изменяемые
list
set 
dict

# a = [3,4,5,3,3,4,4,5,6,7,7,8,8,9,1,1,1,1,1,6]
# a = list(set(a))
# print(a)



# a = {3,4,5,3,3,4,4,5,6,7,7,8,8,9,6, 0, (2131, ), 123.123, 'asdasdsd' }
# a.add('wqeqwe')
# print(a)


# a = {3,4,5,3,3,4,4,5,6,7,7,8,8,9,6, 0, (2131, ), 123.123, 'asdasdsd' }
# a.remove(3)
# print(a)

# a = {3,4,5, 123.123, 'asdasdsd'}

# a.clear()
# print(a)

# a = set()

# a = {3,4,5, 123.123, 'asdasdsd'}

# a.remove(7)
# a.discard(7)
# print(a)
# print(a.p


# a = {1, 2, 4, 5}
# b = {4, 5, 6, 7, 8}

# print(a.intersection(b))
# print(a.intersection(b))
# print(b.difference_update(a))

# print(b)
# print(b)
#########################################

# a = {1, 2, 4, 5}
# b = {4, 5, 6, 7, 8}
# a.update(b)
# print(a)



# foods = ["Coca-Cola", ['Potato', 'Cheeps']]
# foods = {
#     "drinks": "Coca-Cola",
#     "drinks": "Pepsi",
#     "snacks": ['Potato', 'Cheeps']
# }

# print(foods['drinks'])
# print(foods['snacks'][1])




# foods = {
#     "drinks": "Pepsi",
#     "snacks": ['Potato', 'Cheeps']
# }

# foods.update({'colas': 'Coca-Cola'})
# print(foods)
# foods['eda'] = 'Plov'

# print(foods)
# foods['snacks'].append('Burger')
# print(foods)





foods = {
    "drinks": "Pepsi",
    "snacks": ['Potato', 'Cheeps']
}

# foods.pop('snacks')
# print(foods)

# print(foods.get("drin"))
# print(foods["drin"])


# print(foods.keys(), foods.values(), foods.items())

for key, value in foods.items():
    print(f"{key=}, {value=}")






    salaries = {
    'Aktan': 100,
    'Sultan': 200,
    'Aybek': 300,
    'Jamal': 400,
    'Abror': 500,
    'Jamshid': 600,
    'Ilana': 1000
}

print(min(salaries.items(), key=lambda x: x[1]))
print(max(salaries.items(), key=lambda x: x[1]))
sum_salay = sum(salaries.values())
count_salary = len(salaries)

print(f"Count salary: {count_salary} \nSum salary: {sum_salay} \nAverage salary: {sum_salay / count_salary}")