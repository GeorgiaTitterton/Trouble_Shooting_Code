word = input("Enter word: ")

start = int(input("Enter starting digit: "))

finish = int(input("Enter finishing digit: "))

greater = len(word)
over = start


result = ""

while start <= finish:
    digit = word[over]
    result = (result+digit)
    print (result)
    start = start + 1
    over = over + 1
    if over == greater:
        over = int(0)

print (" " )
print (" " )
print (" " )
print(" Final Result: ")
print (result)
            
    
    
