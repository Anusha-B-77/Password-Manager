from datetime import datetime
print("------------------------------WELCOME-----------------------------")
name=input("Enter Your Name: ")
#List of items
lists='''
Rice      Rs 20/kg
Sugar     Rs 30/kg
Salt      RS 20/kg
Oil       Rs 80/liter
Paneer    Rs 110/kg
Maggie    Rs 50/kg
Boost     Rs 90/each
Colgate   Rs 85/each
'''
#declaration
price=0
pricelist=[]
totalprice=0
Finalprice=0
ilist=[]
qlist=[]
plist=[]
finalamount=gst=0
#rates for items
items={
    'rice':20,
    'sugar':30,
    'salt':20,
    'oil':80,
    'paneer':110,
    'maggie':50,
    'boost':90,
    'colgate':85
}
option=int(input("For list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("If you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        exit()
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity: "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst+=(totalprice*5)/100
            finalamount+=gst+totalprice
        else:
            print("Sorry you entered item is not available")
    else:
        print("Please enter 1 or 2")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","SUPER MARKET",25*"=")
            print(28*" ","Guntur")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',5*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',5*'',ilist[i],10*' ',qlist[i],10*" ",plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("GST Amount",45*" ",'GST Rs:',gst)
            print(75*"-")
            print(50 * " ", 'FinalAmount:', 'Rs', finalamount)
            print(75*"-")
            print(27*"-","Thanks For Visting",28*"-")
            print(75*"-")
