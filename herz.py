import badger2040
badger = badger2040.Badger2040()


badger.invert(True)
    
badger.pen(0)
badger.thickness(3)
badger.text("Ich liebe dich", 80, 10)

badger.text("Heute ist", 80, 50)

badger.text("SHEEEEEEESH", 80, 90)


badger.line(
    0, # int: x coordinate of starting point
    40, # int: y coordinate of starting point
    40, # int: x coordinate of ending point
    80, # int: y coordinate of ending point
)

badger.line(
    40, # int: x coordinate of starting point
    80, # int: y coordinate of starting point
    80, # int: x coordinate of ending point
    40, # int: y coordinate of ending point
)


for i in range(0, 25):
    badger.pixel(0 + i, 40 - i)
    

for i in range(0, 15):
    badger.pixel(25 + i, 15 + i)
    
for i in range(0, 15):
    badger.pixel(40 + i, 30 - i)
    
for i in range(0, 26):
    badger.pixel(55 + i, 15 + i)
    


 
badger.update()



