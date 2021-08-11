#Topic: Basic python concepts

#concepts used
#input output
#arithmatic operators
#conditional operators
#if else statements
#elif statements
#loop
#functions

                                #################################
                                #                               #
                                #       convertor  system       #
                                #                               #
                                #################################

# 1) currency convertor
#dollar to inr
#inr to dollar

# 2) temperature convertor
#fahrenheit to celcius
#celcius to fahrenheit
#celcius to kelvin
#kelvin to celcius

# 3) measures convertor
#meter to centimeter
#centimeter to meter

# 4) spead convertor
#km/hr to m/s
#m/s to km/hr


print("\n\n********************************************\n              Convertor   \n********************************************")


#########################################################################################


# 1) currency convertor
#dollar to inr
def dollarToInr():
    dollar=float(input("\n Enter the amount in Dollar: "))
    if dollar<0:
        print("\n Invalide inpute...Please try again")
    else:
        print("\n Value in Inr : ",dollar*73.41)

#inr to dollar
def inrToDollar():
    inr=float(input("\n Enter the amount in Rupee: "))
    if inr<0:
        print("\n Invalide inpute...Please try again")
    else:
        print ("\n Value in Dollar: ",inr/73.4)


#######################################################################################


# 2) temperature convertor
#fahrenheit to celcius
def fahrenheitToCelcius():
    fahrenheit = float(input("\n Enter temperature in fahrenheit: ")) 
    Celcius = (5/9) * (fahrenheit - 32)
    print("Temperature in Celcius: ",Celcius)

#celcius to fahrenheit
def celciusToFahrenheit():
    celcius = float(input("\n Enter temperature in Celsius: "))  
    fahrenheit = (celcius * 1.8) + 32  
    print("\n Temperature in fahrenheit: ",fahrenheit)

#celcius to kelvin
def celciusToKelvin():
    degree = float(input("\n Enter temperature in Degree: ")) 
    if degree < -273.15:
        print("\n Invalid input ... Please try again")
    else:
        kelvin = degree + 273.15
        print("\n Temperature in Kelvin: ",kelvin)

#kelvin to celcius
def kelvinToCelcius():
    kelvin = float(input("\n Enter temperature in kelvin: ")) 
    if kelvin<0:
        print("\n Invalid input ... Please try again")
    else:
        degree = kelvin - 273.15
        print("\n Temperature in degree: ",degree)


########################################################################################


# 3) measures convertor
#meter to centimeter
def meterToCentimeter():
    meter=float(input("\n Enter measure in meter: "))
    if meter<0:
        print("\n Invalid input ... Please try again")
    else:
        print("\n Measure in Centimeter: ",meter*100,"cm")

#centimeter to meter
def centimeterToMeter():
    centimeter=float(input("\n Enter measure in Centimeter: "))
    if centimeter<0:
        print("\n Invalid input ... Please try again")
    else:
        print("\n Measure in Meter: ",centimeter/100,"m")


######################################################################################

# 4) spead convertor
#km/hr to m/s
def kmhToMs():
    kmh=float(input("\n Enter Speed in Km/hr: "))
    ms=kmh*(5/18)
    print("\n Speed in m/s: ",ms,"m/s")

#m/s to km/hr
def msToKmh():
    ms=float(input("\n Enter Speed in m/s: "))
    kmh=ms*(18/5)
    print("\n Speed in km/hr: ",kmh,"km/hr")


###########################################################################################


while True:
    i= int(input("\n\nEnter the choice \n1-> Currency convertor\n2-> Temperature convertor\n3-> Measures convertor\n4-> Speed convertor\n0-> Exit\nYour Option: "))
    if i<0 or i>4:
        print("\nInvalid input...please enter correct choice")
    elif i==1:
        print("\n*********************************************************\n")
        print("\n1.Currency convertor\n")
        dollarToInr()
        inrToDollar()
        print("\n*********************************************************\n")
    elif i==2:
        print("\n*********************************************************\n")
        print("\n2.Temperature convertor\n")
        fahrenheitToCelcius()
        celciusToFahrenheit()
        celciusToKelvin()
        kelvinToCelcius()
        print("\n*********************************************************\n")
    elif i==3:
        print("\n*********************************************************\n")
        print("\n3.Measures convertor\n")
        meterToCentimeter()
        centimeterToMeter() 
        print("\n*********************************************************\n")
    elif i==4:
        print("\n*********************************************************\n")
        print("\n4.Speed convertor\n")
        kmhToMs()
        msToKmh()  
        print("\n*********************************************************\n")   
    elif i==0:
        print("\nThank you for using our convertor.")
        break
