def fares(age, senior=False, student=False,adult=False, discount=False):
    if age > 20 and age < 65:
        if adult==True:
            return "Fullprice 30kr"
        else:
            return "discount price 20kr"
    elif age<=20 or age >=65:
            if student==True:
                return "Discount price 20kr"
            elif senior==True:
                return "Discount price 20kr"

    print "error"






print fares(10)
print fares(65,senior=True)
print fares(20,student=True)
print fares(64,adult=True)