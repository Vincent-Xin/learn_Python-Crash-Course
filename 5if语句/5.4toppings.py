available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

requested_toppings=['mushrooms','green peppers','extra cheese','french fries']

if requested_toppings:
	for requested_topping in requested_toppings:
		if requested_topping not in available_toppings:
			print("Sorry,we are out of "+requested_topping+".")
		else:
			print("Adding "+requested_topping+".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")


# if requested_toppings:
# 	for requested_topping in requested_toppings:
# 		if requested_topping=="green peppers":
# 			print("Sorry,we are out of green peppers right now.")
# 		else:
# 			print("Adding "+requested_topping+".")
# 	print("\nFinished making your pizza!")
# else:
# 	print("Are you sure you want a plain pizza?")