
import CellPhoneClass as cp

def main():

    # getting data from user 
    manufacturer = input("who is the manufacturer: ")
    model = input('what is the model: ')
    retail_price = int(input('what is the retail price: '))
    
    # creating an instance of the object
    phone = cp.CellPhone(manufacturer,model,retail_price)

    # printing the entered data 
    print('here is the data you have entered:')
    print('Your phone is manufactured by ', phone.get_manufact())
    print('Your phone is the model ', phone.get_model())
    print('The retail price is ', int(phone.get_retail_price()))


    manufacturer = 'Sprint'
    model = '13'
    retail_price = '100'

    
    phone.set_manufact(manufacturer)
    phone.set_model(model)
    phone.set_retail_price(retail_price)


  



main()