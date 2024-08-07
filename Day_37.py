print("STARS WARS NAME GENERATOR ")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print()
name = input("Enter your first name: , Enter your last name: , Enter mother's maiden name: , Enter the city name where they born: ").split()
print()
first_name = name[0].strip()
last_name = name[1].strip()
mother_name = name[2].strip()
city_name = name[3].strip()
stars = f"{first_name[:3].title()}{last_name[:3].lower()}{mother_name[:2].title()}{city_name[-3:].lower()}" 
print(f"Your star wars name is {stars} 🧑‍🎤")    


# Another way to solve this problem 


print("STARS WARS NAME GENERATOR ")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print()
first_name = input("Enter first name: ")
last_name = input("second name: ")
join_name = first_name[:3] + last_name[:3]
print()
mother_name = input("Enter your mother name: ")
mother_city = input("Enter your city: ")
join_name2 = mother_name[:2] + mother_city[-3::]
print()
print(f"Your stars wars name is {join_name}{join_name2} 🧑‍🚀 ")

