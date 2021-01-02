myUniqueList = []
myLeftOver = []

def add(x):
    global myUniqueList
    global myLeftOver
    if x in myUniqueList:
      myLeftOver.extend([x])
      return False

    else:
          myUniqueList.append(x)
          return True



add(10)
add(10)
add(30)
add(99)
add(99)

print(myUniqueList)
print(myLeftOver)