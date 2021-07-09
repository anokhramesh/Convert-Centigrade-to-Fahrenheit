# This is simple program to Convert Cent to Square metre,Square Feet and Acre.
C ="" # C is a variable to store the user input value.
while C != "q":# Run the loop,Untill user pressed the small letter 'q'
    C = float(input("Enter the value of Cent or enter q for Quit\n"))
    S_M =(C*40.460000) # Squar metre = Cent * 40.460000
    S_F =(C*435.508003) # Squar Feet = Cent * 434.508003
    A_C = (C*0.009998) # Acre = Cent * 0.009998
    print (C,"Cent is = ",S_M,"Square Meter or",S_F,"Square Feet or",A_C,"Acre.\n")