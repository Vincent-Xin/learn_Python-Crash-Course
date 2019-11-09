motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#motorcycles[0] = 'ducati'
#print(motorcycles)

print(motorcycles[0])

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0,"250")
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motor = motorcycles.pop()
print(popped_motor)
print(motorcycles)

popped_motor = motorcycles.pop(1)
print(popped_motor)
print(motorcycles)

dear_motor = 'suzuki'
motorcycles.remove(dear_motor)
print(motorcycles)
print("\nA "+dear_motor+" is too expensive for me.")