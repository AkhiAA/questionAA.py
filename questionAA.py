# question.py by akhi

# initialize variables
q1 = """QA: whats 2*2
1) 2 
2) 3
3) 1
4) 4
"""
a1 = int(0)
check1 = bool(False)
score = int(0)

# question1
print(q1)

while check1 == False:
    try:
        a1 = int(input("Choose 1, 2, 3, or 4 Based on your thoughts.  "))
        if a1 == 4:
            print("Thanks")
            score=int(score+1)
            check1 = True
        elif 0 < a1 < 5:
            print ("Thanks")
            
            check1 = True
        else:
            print (" Please enter an integer from 1-4 ")
    except ValueError:
        print (" Come on now, Just try ")
        
#score
print("quiz score: ",score * 100, "%")

