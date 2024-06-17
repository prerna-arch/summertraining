black_square = "\u25A1"
white_square = " \u25A0"





for i in range(0,8):
    for j in range(0,8):
         if i==0:
              if j == 0 or j == 7:
                   print("\u2656",end=" ")
              elif j == 1 or j == 6 :
                   print("\u2658",end=" ")   
              elif j == 2 or j == 5:
                   print("\u2657",end=" ")  
              elif j == 3:
                   print("\u2654",end=" ")    
              elif j == 4:
                   print("\u2655",end=" ")
              else:
                       if j%2 == 0:
                             
                           print(black_square,end=" ")

                       else: 
                          print(white_square,end=" ")

              
         
         elif i == 7:
              if j == 0 or j == 7:
                   print("\u265C",end=" ")
              elif j == 1 or j == 6 :
                   print("\u265E",end=" ")   
              elif j == 2 or j == 5:
                   print("\u265D",end=" ")  
              elif j == 3:
                   print("\u265B",end=" ")    
              elif j == 4:
                   print("\u265A",end=" ")
              else:
                         if (j+1)%2 == 0:
                             
                           print(black_square,end=" ")

                         else: 
                          print(white_square,end=" ")

              
         elif i == 1: 
              print("\u2659",end=" ")
         elif i == 6:
              print("\u265f",end=" ")
         else:    
              
           if (i%2 == 0):
              if j%2 == 0:
                   print(black_square,end=" ")
              else: 
                   print(white_square,end=" ")
           else:
              if (j+1)%2 == 0:
                   print(black_square,end=" ")
              else:
                   print(white_square,end=" ")


    print()

         
                   
        
              
                   