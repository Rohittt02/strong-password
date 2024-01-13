password=input("enter your password :  ")
if len(password)>=8 and len(password)<=12:
     if "A" in password or "a" in password or "B" in password or "b" in password or "C" in password or "c" in password or "E" in password or "e" in password or "F" in password or "f" in password or "G" in password or "g" in password or "H" in password or "h" in password or "I" in password or "i" in password or "J" in password or "j" in password or "K" in password or "k" in password or "L" in password or "l" in password or "M" in password or "m" in password or "N" in password or "n" in password or "O" in password or "o" in password or "P" in password or "p" in password or "Q" in password or "q" in password or "R" in password or "r" in password or "S" in password or "s" in password or "T" in password or "t" in password or "U" in password or "u" in password or "V" in password or "v" in password or "W" in password or "w" in password or "X" in password or "x" in password or "Y" in password or "y" in password or "Z" in password or "z" in password:
          if "@" in password or "#" in password or "$" in password or "&" in password:
               if "0" in password or "1" in password or "2" in password or "4"  in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password:
                    print("This is strong password")
               else:
                    print("Please includ atleast one numeric number\n This is not strong password ")
          else:
               print("Please Includ atleast one special character\n This is not strong password")
     else:
          print("Please Enter atleast one alphabate\n This is not strong password ")
else:
     print('Password length should be 8 to 12 character long')