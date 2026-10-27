
x = int(input("Enter integer x: "))
y = int(input("Enter integer y: "))
z = int(input("Enter integer z: "))


is_even = x % 2 == 0
is_positive = y > 0
is_in_range = 10 <= z <= 50  


final_condition = is_even and is_positive and is_in_range


print(f"Final condition met: {final_condition}")
