#List of cars available 
cars={'BMW','Audi','Nissan','Mercedes-Benz','Tesla','Ferrari','Hyundai','Kia',
'Maserati','Honda','Bentley','Porshe','Toyota','Jeep','Chevrolet','Volkswagen','Lexus',
'Chrysler','Mazda','Jaguar','Dodge','Suzuki','Aston Martin','Cadillac','Lotus','Volvo',
'Opel','Mitsubishi','Peugeot','Ford'}
models={'Corolla':30000,'Ford explorer':52000,'BMW X5':65000,'Jeep Wrangler':50000,'Passat':25000,
'SUV':60000,'Audi A3':40000,'Altima':27490,'BMW X3':47000,'Elantra':20000,'Magnite':20000,
'C class sedan':43550,'CLA coupe':40000,'Camry':26000,'Yaris':19000,'Picanto':12910,'Tucson':27000,
'Civic':24000,'Accord':25000,'Levante':90000,'Continental GT':240000,'Sedan':30000,'Cayenne':79000,
'Model S':95000,'296GTB':338255,'Challenger':60000,'Rapide':241000,'Outlander':30000,'2008 allure':39000}
brand_of_car=input('what brand of car are you looking for?   ')
if brand_of_car in cars:
    print('Yes, it is available.')
    #if brand of car is available,ask for the model
    model_of_car=input('What model are you looking to buy?   ')
    if model_of_car in models:
        print('Yes, it is available.')
        price_of_car=models[model_of_car]
        print('The price is ${}.'.format(price_of_car))
    else:
        print('Sorry, we do not have that model.')
else:
  print('Sorry, it is not available.')

