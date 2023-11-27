def main():
 name = input("Name: ")
 a,b,c,d = input("Type a 4 Subjects: ").split(" ")
 e,f,g,h =(input("Type your Average:  ")).split(" ")

 
 print("Name: "+name)

 if int(e) >= 99:
   print("Invalid Grade Value for "+a)
 else:
   print(a+": "+e)
 if int(f) >= 99:
   print("Invalid Grade Value for "+b)
 else:
   print(b+": "+f)
 if int(g) >= 99:
   print("Invalid Grade Value for "+c)
 else:
   print(c+": "+g)
 if int(h) >= 99:
   print("Invalid Grade Value for "+d)
 else:
   print(d+": "+h)    
 
 print("Compute Your grade ")
 print()
 ab=float(input("Subject#1: "))
 ac=float(input("Subject#2: "))
 ad=float(input("Subject#3: "))
 ae=float(input("Subject#4: "))
 ave=((float(ab)+float(ac)+float(ad)+float(ae)) / (4 ))
 print()
 print("Name: "+name)
 print("Average: ",ave)
 
 if ave >= 75:
  print("Amount to be paid: 0 ")
  print("Remarks: Passed ")
  print("Notes: Eligible for next semester")
  print(" Thank you! ")
  exit()
 elif ave <= 75:
  print("Amount to be paid: 4")
  print("Remarks: Failed ")
  print("Notes: N/A")
  	
  repeat= input("would you like to repeat again? ")
  if repeat == "Y":
   main()
  
  elif repeat == "N":
   print("good bye")
   exit()	
  if repeat == "y":
   print("Invalid operation ")
  elif repeat == "n":
   print("Invalid operation ")
   
main()
