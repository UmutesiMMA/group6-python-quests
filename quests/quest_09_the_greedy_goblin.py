# Level 2 - quest 9
import math

gold_pieces_num = 27
friends_num = 4
# Calculating the pieces that each friend will receive
pieces_given = math.floor(gold_pieces_num / friends_num)

# Calculating the pieces the goblin will remain with

remaining_pieces = gold_pieces_num % pieces_given

print(pieces_given)
print(remaining_pieces)