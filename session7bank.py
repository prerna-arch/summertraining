

user_input = int(input("enter the amount you want to take from bank:"))
if user_input <= 50000:
            print("YOU CAN TAKE THE LOAN")
            print("------------------------")
            minimum_amount = 0.10 * user_input
            print(" minumun installment every month should be paid by you:",minimum_amount)
            print("--------------------------")
            first = int(input("enter the first installment you can pay:"))
            print("-------------------------------")
            pending = user_input - first
            interest = 0.15 * pending
            print("interest:",interest)
            print("-----------------------------------")
            remaining = pending + interest
            print("remaining:",remaining)
            print("---------------------------------------")
            next_month = int(input("enter the amount you are able to pay per  month:"))
            print("-----------------------------")
            start_month = int(input("Enter the month number //ex 1 for jan// in which you have taken the loan:"))
                


            months = 0
            while remaining > 0:
               
               remaining -= next_month
               if remaining < 0:
                     remaining = 0 
               months += 1
               print("After", months, "month ,amount :",remaining)
               print("-------------------------")
            print("installments wiil be over after  :",months,"months")
            end_month = start_month + months 
            
            
            
            if end_month == 1:
                  print("installment will be over in JAN")
            elif end_month == 2:
                  print("installment will be over in FEB")
            elif end_month == 3:
                  print("installment will be over in MARCH")
            elif end_month == 4:
                  print("installment will be over in APRIL")
            elif end_month == 5:
                  print("installment will be over in MAY")
            elif end_month == 6:
                  print("installment will be over in JUNE")
            elif end_month == 7:
                  print("installment will be over in JULY")
            elif end_month == 8:
                  print("installment will be over in AUG")
            elif end_month == 9:
                  print("installment will be over in SEP")
            elif end_month == 10:
                  print("installment will be over in OCT")
            elif end_month == 11:
                  print("installment will be over in NOV")
            else:
                  print("installment will be over in DEC")
         

else:
    print("YOU CAN NOT TAKE THE LOAN")


"""
I have HDFC Bank Credit Card.
 HDFC Bank will charge 15% interest on outstanding amount
 Minimum, you should be able to pay 10% of outstanding amount else your credit score will be compromised.

 April 2024 -> 50,000 ---> input by user
    April 2024,  min ---> 5000
                 pending -> 45000
                         + 15% of 45,000 = 6750
 I can only pay max of 8000 per month -----> input by user

 Find in which month whole amount will become 0                         
 """


"""
amount = int(input("Enter the amount you have spent: "))
             
print("You have to pay 10% of" , amount , "that is" , 0.10*amount , "first.")

amount = amount - (0.10 * amount)
interest = 0.15 * amount
amount += interest

print("\nOutstanding amount including 15% interest: " , amount)
          
min_amount = int(input("Enter the minimum amount you can pay per month: "))

month = 0
while amount > 0:
    
    amount -= min_amount
    if amount < 0: 
        amount = 0

    month += 1   
    print("Month", month, "Outstanding Amount = ", amount)


month_names = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }


start_month = 4
end_month = start_month + month

start_year = 2024
if month > 8:
    start_year += 1
    end_month = end_month - 12

print("Your outstanding amount will become zero in :" , month_names[end_month], start_year)
"""