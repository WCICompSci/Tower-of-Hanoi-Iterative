# tower_of_hanoi.py
# David Gurevich
# October 26, 2018

from stack import Stack

def tower_print(towers, num_of_disks):
    """
    Print all tower info elegantly
    """
    for i in range(num_of_disks, 0, -1):
        for tower in towers:
            try:
                tower.print_tower(tower.items[::-1][-i], num_of_disks)
            except IndexError:
                tower.print_tower(0, num_of_disks)
        print()
    print("–" * 11*(num_of_disks))
    for tower in towers:
        print(tower.name, ":", tower, end=";\t")
    print("\n")

def initialize():
    """
    Initializes game variables.

    Returns:
        towers: List of towers
        even: whether num_of_disks is even or not
        max_iter: Maximum number of iterations to solve
        num_of_disks: user defined value
    """
    while True:
        try:
            num_of_disks = int(input("Enter the number of Disks: "))
            break
        except:
            print("Invalid Entry. Try again!")

    towers = [Stack("Tower 1"), Stack("Tower 2"), Stack("Tower 3")]
    for i in range(num_of_disks, 0, -1):
        towers[0].push(i)

    max_iter = (2 ** num_of_disks) - 1
    even = num_of_disks % 2 == 0

    return towers, even, max_iter, num_of_disks

towers, even, max_iter, num_of_disks = initialize()

if even:
    A = towers[0]
    B = towers[1]
    C = towers[2]
else:
    A = towers[0]
    B = towers[2]
    C = towers[1]

print("< BEGIN >")
tower_print(towers, num_of_disks)
for i in range(1, (3 * max_iter) + 1, 3):  
    if towers[-1].size() != num_of_disks:
        A.disk_move(B)
        print("< MOVE >", i, "between", A.get_name(), "and", B.get_name())
        tower_print(towers, num_of_disks)

    if towers[-1].size() == num_of_disks: break
    
    A.disk_move(C)
    print("< MOVE >", i+1, "between", A.get_name(), "and", C.get_name())
    tower_print(towers, num_of_disks)

    B.disk_move(C)
    print("< MOVE >", i+2, "between", B.get_name(), "and", C.get_name())
    tower_print(towers, num_of_disks)
    
print("< COMPLETE >")




