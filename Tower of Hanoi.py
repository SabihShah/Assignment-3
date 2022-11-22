def tower_hanoi(n):
    no_of_moves = 2**n-1 
    moves = []           
    pole1 = 'A'            
    pole2 = 'B'          
    pole3 = 'C'          
    
    if n % 2==0:         
        pole3 = 'B'       
        pole2 = 'C'
    
    for i in range (1,no_of_moves+1):  
        if i%3 == 1:                   
            moves.append(pole1+pole3)
            print("Moving disc from ", pole1, "to", pole3)
        if i%3 == 2:
            moves.append(pole1+pole2)
            print("Moving disc from ",pole1,"to", pole2)
        if i%3 == 0:
            moves.append(pole3+pole2)
            print("Moving disc from ",pole3,"to",pole2)
            
    return moves

print(tower_hanoi(3))