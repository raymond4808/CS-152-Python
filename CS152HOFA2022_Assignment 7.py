#Prints cost of speeding tickets ONLY without mandatory court date in Clay County, Missouri | Sources: http://www.circuit7.net/traffic/violation-fines
#Values are flat rate based on speed over the the set speed limit
#Raymond Cheung, 10/25/2022
def speedingTicketPrice (aSpeedOver):
    #(Question 1)calculations for speeding tickets costs in which doesn't require you to go to court, takes the filtered valid offending speed over (aSpeedOver) the limit and places it into a bracket of costs based on boolean ruleouts. 
    #Based on the bracket of valid offending speed (aSpeedOver), the cost of the ticket is charged a flat rate plus bracket rate based on formula table on website.
    intialCourtCost= 72.50       
    courtCost= 76.50
    if aSpeedOver >0 and aSpeedOver < 6:
        return (intialCourtCost+50.50)
    elif aSpeedOver > 5 and aSpeedOver <11:
        return (courtCost + 60.50)
    elif aSpeedOver >10 and aSpeedOver <16:
        return (courtCost + 70.50)
    elif aSpeedOver >15 and aSpeedOver <20:
        return (courtCost +  100.50)
    elif aSpeedOver >19 and aSpeedOver <26:
        return (courtCost + 155.50)
    

def isValidInput (isSpeedOver):
    #(Question 3) Checks if speed over the speed limit is valid for a ticket (checks for lowest limit)
    return isSpeedOver > 0
        

def main (): 
    #(Question 2) Start off IF statement with upper limit checker, if valid runs through cost calculator and reports out speed over along with cost for speeding ticket
    #(Question 4) Added while loop to only allow speeds over the speed limit to run in the calculation 
    
    speedOver= int(input("Enter the total speed over the speed limit: "))
    
    
    while not isValidInput (speedOver):
    #(Question 4) Implement while loop to call function from question 3 for valid input
        speedOver= int(input("Enter valid speed over the speed limit:"))
        
        
    if speedOver > 25:
        print ("MANDATORY COURT DATE REQUIRED")
    else:        
        if isValidInput(speedOver):
            speedingTicketCost= speedingTicketPrice(speedOver)
            print ("Going", speedOver, "MPH over the speed limit, your speeding ticket will come out to be","$", speedingTicketCost, ".")
      # else:
          # print ("Speed is within legal limits, no speeding ticket should have been given")
      # Only needed if while loop doesn't exist to accommodate for lower limit user inputs
main ()