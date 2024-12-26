from . import demon

class Soldier:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.sinceMult = 0
        self.turns = 0

    def move(self, board, turn):
        if self.turns >= turn:
            return
        
        self.turns += 1
        self.sinceMult += 1

        direction = self.findDirection(board)
        if direction == -1:
            return
        
        newRow = self.r + direction[0]
        newCol = self.c + direction[1]

        if 0 <= newRow < 10 and 0 <= newCol < 10:
            if type(board[newRow][newCol]) is demon.Demon or type(board[newRow][newCol]) is Soldier:
                return
            
            if not board[newRow][newCol]:
                board[newRow][newCol] = self
                oldRow = self.r
                oldCol = self.c
                self.c = newCol
                self.r = newRow
                board[oldRow][oldCol] = None

    def numberOfNeighbors(self, board):
        directions = [
            (-1,  0), (-1, +1), ( 0, +1), (+1, +1), 
            (+1,  0), (+1, -1), ( 0, -1), (-1, -1)
        ]
        count = 0
        for dc, dr in directions:
            neighbor_row = self.r + dr
            neighbor_col = self.c + dc
            if 0 <= neighbor_row < 10 and 0 <= neighbor_col < 10:
                if type(board[neighbor_row][neighbor_col]) is Soldier:
                    count += 1
        return count
    
    def findDirection(self, board):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # North, East, South, West
        nearest_demons = []
        furthest_demons = []
        clear_pathways = []
        min_distance = float('inf')
        max_distance = -1

        for dr, dc in directions:
            r, c = self.r, self.c
            distance = 0
            found_demon = False

            # Move in the current direction until boundary or soldier is found
            while 0 <= r < 10 and 0 <= c < 10:
                distance += 1
                r += dr
                c += dc

                if 0 <= r < 10 and 0 <= c < 10 and type(board[r][c]) is demon.Demon:  # Assuming 'soldier' represents an soldier
                    
                    if distance <= min_distance:
                        min_distance = distance
                        nearest_demons.append((dr,dc,distance))
                        
                    if distance >= max_distance:
                        max_distance = distance
                        furthest_demons.append((dr,dc,distance))

                    found_demon = True
                    break  # Stop searching in this direction
            if distance > 0 and not found_demon:
                clear_pathways.append((dr,dc))
                

        nearest_demons = [tup for tup in nearest_demons if tup[2] == min_distance]
        furthest_demons = [tup for tup in furthest_demons if tup[2] == max_distance]

        if len(nearest_demons) == 0:
            return -1

        if len(nearest_demons) == 1:
            nearest_demon = nearest_demons[0]
            return self.awayFrom((nearest_demon[0], nearest_demon[1]))
        
        if len(clear_pathways) > 0:
            first_clear_pathway = clear_pathways[0]
            return (first_clear_pathway[0], first_clear_pathway[1])
        
        assert(len(furthest_demons) > 0)
        furthest_demon = furthest_demons[0]
        return (furthest_demon[0], furthest_demon[1])
        
    def awayFrom(self, tup):
        dr = 0 if tup[0] == 0 else -tup[0]
        dc = 0 if tup[1] == 0 else -tup[1]
        return (dr,dc)
    
    def mult(self, board):
        if self.sinceMult == 3:
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            for dr, dc in directions:
                newRow = self.r + dr
                newCol = self.c + dc
                if 0 <= newRow < 10 and 0 <= newCol < 10 and not board[newRow][newCol]:
                    newSoldier = Soldier(newRow, newCol)
                    newSoldier.turns = self.turns
                    board[newRow][newCol] = newSoldier
                    self.sinceMult = 0
                    return
            self.sinceMult = 0