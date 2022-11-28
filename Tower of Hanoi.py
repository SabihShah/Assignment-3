def tower_hanoi(n):
    no_of_moves = 2**n-1 
    moves = []
    
    print("No. of Moves:", no_of_moves)

    if n % 2 != 0:
        
        for i in range(1, no_of_moves+1):

            pole1 = 'A'
            pole2 = 'B'
            pole3 = 'C'

            if i % 3 == 1:
                print(pole1, "to", pole3)
                moves.append(pole1+pole3)

            elif i % 3 == 2 and i >= 5:    
                (pole2, pole1) = (pole1, pole2)
                print(pole1, "to", pole2)
                moves.append(pole1+pole2)
            
            elif i % 3 == 2:
                print(pole1, "to", pole2)
                moves.append(pole1+pole2)
            
            elif i % 3 == 0 and i >= 6:
                (pole2, pole3) = (pole3, pole2)
                print(pole3, "to", pole2)
                moves.append(pole3+pole2)

            elif i % 3 == 0:
                print(pole3, "to", pole2)
                moves.append(pole3+pole2)

    return moves
            





print(tower_hanoi(3))