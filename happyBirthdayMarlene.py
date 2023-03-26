import badger2040
badger = badger2040.Badger2040()


badger.invert(True)

badger.pen(0)
badger.thickness(3)

badger.text("Happy Birthday", 10, 10)

badger.text("Marlene", 10, 40)

abstand = 5

length = 50

start = 45
end = 75

yWert = 60

for i in range(0, 26):
    
    if (i <  20):
        badger.line(start - abstand, yWert + i, start + abstand, yWert + i)
        badger.line(end - abstand, yWert + i, end + abstand, yWert + i)
        
        abstand +=   1
    
    if (i  > 20 and i < 26):
        badger.line(start - abstand, yWert + i, start + abstand, yWert + i)
        badger.line(end - abstand, yWert + i, end + abstand, yWert + i)
        
        maxEnd = end + abstand
        maxStart = start -abstand
        
    if(i == 25):
        for j in range(0, 41):
            badger.line(maxStart + j, yWert + i + j, maxEnd - j, yWert + i + j)
     
      
     
badger.text("Love ya", 170, 110)       
        
        
        
    
badger.update()