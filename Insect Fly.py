import InsectClass as I 

wings =int(input('How many wings does the insect have:'))
legs= int(input('How many legs does the insect have:'))

mosquito = I.insect()
housefly = I.insect()


mosquito.flight_length()
housefly.flight_lenght()

print('The mosquito can fly', mosquito.get_miles(), 'miles')
print('The housefly can fly', housefly.get_miles(), 'miles')



