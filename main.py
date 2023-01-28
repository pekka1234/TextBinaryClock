from time import sleep
# Hiding cursor so it is not in the way
import cursor
cursor.hide()

clock = list("0")

while 1:
    # Joining list and printing result with '\r' so that the next print overwrites this
    jclock = ''.join(clock)
    print(jclock, end = "\r")
    
    # If it is all ones, new char will be added and others turned to zero
    if jclock == len(jclock) * "1":
        clock = list("1" + len(jclock) * "0")
    # If not (most of the time)    
    else:
        # Reversing clock list
        rclock = clock[::-1] 
        for x in rclock:
            if x == "0":
                # When for loops hits first zero, it will be turned to 1 and all ones before the zero will be turned to zeroes
                place = rclock.index(x)
                rclock[place] = "1"
                rclock = rclock[place:]
                for x in range(place):
                    rclock.insert(0, "0")
                break    
        # Reversing the modified reversed clock         
        clock = rclock[::-1]            
    # Waits one second (this clock counts seconds)    
    sleep(1)



