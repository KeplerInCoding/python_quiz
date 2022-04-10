print("Welcome to the quiz!!")
n= 0
L_q= ["Which organization developed an Indian robot named Vyom mitra?",
      "The Noble Prize for 2018 in the area of physics has been awarded for the work in the area of -",
      "The wave nature of electrons was first experimentally established by -",
      "In which year Capt. Rakesh Sharma travelled to space in a soviet space programmed?",
      "Which is the second country in the world to land a Rover on Mars?",
      "Calamine and Sphalerite are the ores of -",
      "Which of the following defence equipment's/ systems has not been developed or upgraded by Defence Research and Development organization (DRDO)?",
      "Virtual currency Bitcoin is based on -"]
L_o= ["1) C-DAC, Pune","2) ISRO","3) TIFR","4) DRDO",
      "1) Laser physics","2) Black hole","3) Magnetic resonance","4) Gravitational wave",
      "1) Photoelectric effect","2) Double slit experiment","3) Davisson and Germer experiment","4) Compton effect",
      "1) 1981","2) 1982","3) 1983","4) 1984",
      "1) Russia","2) Japan","3) China","4) India",
      "1) Iron","2) Mica","3) Zinc","4) Copper",
      "1) Arjun Mk-1A","2) Sniper Rifles","3) Light Combat Aircraft Mk-1A","4) PINAKA-Extended Range, Guided",
      "1) Block Chain Technology","2) Internet of Things","3) Artificial Intelligence","4) 3-D Printing"]

L_a=["2","1","3","4","3","3","2","1"]
print()
k=input(("Enter 1 to start:"))
print()
while k=="1":
    for m in range(0,8):
          print("QUESTION: ",m+1)
          print(L_q[m])
          for l in range(4*m,4*(m+1)):
              print(L_o[l])
          print()
          c=input("Enter correct choice (1/2/3/4):")
          print()
          if c==L_a[m]:
               print("CORRECT ANSWER!!")
               n=n+1
          else:
              print("INCORRECT ANSWER :(")
              print("the correct answer is:",L_a[m])
              print()
          choose=input("Enter for next qustion, Enter 'q' to quit exit the quiz")
          print()
          print()
          print()
          if choose=="q" or m==7:
              k=2
              break
print("Well done! You scored ",n," out of ",m+1)
print("Exiting the game...")
          
          
