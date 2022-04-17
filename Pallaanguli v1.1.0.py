__version__ = '1.1.0'
__author__ = 'Praveen Kumar'


class Pallaanguli():
    """Pallaanguli board class"""
    total_coins:int = 70
    total_no_of_holes:int = 14
    no_of_players:int = 2
    
    coins_per_hole:int = total_coins // total_no_of_holes
    no_of_holes_per_player:int = total_no_of_holes // no_of_players
    
    init_coins_per_player:int = total_coins // no_of_players
    
    def __init__(self,initial_coins: tuple = (35,35)) -> None:
        
        self.coins:list[int] = list(initial_coins)
        
        self.no_of_holes:list[int] = [0] * Pallaanguli.no_of_players
        self._init_board_()

    def _init_board_(self) -> None:
        self.board:list[Union[int,str]] = ['*'] * Pallaanguli.total_no_of_holes
        
        for player in range(Pallaanguli.no_of_players):
            
            position = player * Pallaanguli.no_of_holes_per_player
            end_position = position + Pallaanguli.no_of_holes_per_player
            
            while position < end_position and self.coins[player] >= Pallaanguli.coins_per_hole:
                
                self.board[position] = Pallaanguli.coins_per_hole 
                self.coins[player] -= Pallaanguli.coins_per_hole
                self.no_of_holes[player] += 1
                
                position += 1
            
    
    def display_board(self):
        
        print(f"Player 1: {self.coins[0]}")
        print(f"Player 2: {self.coins[1]}")
        
        line1 = 'Player 1: | ' + (' | '.join([str(self.board[holes]).center(3,' ') for holes in range(Pallaanguli.no_of_holes_per_player)])) + ' |'
        line2 = 'Player 2: | ' + (' | '.join([str(self.board[holes]).center(3,' ') for holes in range((Pallaanguli.total_no_of_holes-1),(Pallaanguli.no_of_holes_per_player-1),-1)])) + ' |'
        
        space_len = " " * len('Player 1: ')
        print("<----------".center(63,' '))
        numbering = space_len + ' '
        for i in range(7,0,-1):
            numbering += str(i).center(6,' ')
        
        print(numbering)
        print(space_len + ("-" * 5).join(['+'] * 8))
        
        print(line2)
        
        print(space_len + ("=" * 5).join(['+'] * 8))
        
        
        print(line1)
        
        print(space_len + ("-" * 5).join(['+'] * 8))
        
        
        numbering = space_len + ' '
        for i in range(1,8):
            numbering += str(i).center(6,' ')
        
        print(numbering)
        print("---------->".center(63,' '))

        
    def next_hole(self,hole: int) -> int:
        hole_next = hole
        while True:
            hole_next = (hole_next + 1) % Pallaanguli.total_no_of_holes
            if self.board[hole_next] != '*':
                return hole_next
            
    
    def coins_to_add(self,player: int,hole: int) -> None:
        self.coins[player] += self.board[hole]
        self.board[hole] = 0
        
    def pasu(self,hole:int) -> None:
        player = hole // Pallaanguli.no_of_holes_per_player
        self.coins_to_add(player, hole)
            
    def taken_out(self,hole:int) -> int:
        takes = self.board[hole]
        self.board[hole] = 0
        return takes
    
    def single_turn(self,taken_hole:int) -> int:
        
        hole = taken_hole
        
        takes = self.taken_out(hole)
        
        while takes > 0:

            hole = self.next_hole(hole)
            self.board[hole] += 1

            if self.board[hole] == (Pallaanguli.coins_per_hole - 1):
                self.pasu(hole)

            takes -= 1
            
        return self.next_hole(hole)
    
    def player_turn(self,player:int,hole:int) -> None:
        
        while self.board[hole] > 0:
            hole = self.single_turn(hole)
            
        hole_won = self.next_hole(hole)
        
        self.coins_to_add(player,hole_won)
        
        
    def round_over_check(self,player:int) -> bool:

        start = player*Pallaanguli.no_of_holes_per_player
        end = start + self.no_of_holes[player]

        return sum(self.board[start:end]) == 0

    def player_input(self,player:int) -> int:
        
        round_check = not self.round_over_check(player)
        
        while round_check:
            try:
                hole = str(input(f"Player {player+1}: Enter the hole's number: "))
                hole = int(hole)
                if not (0 <= hole <= Pallaanguli.no_of_holes_per_player):
                    print(f"Enter a number from 1 to {Pallaanguli.no_of_holes_per_player} [0 for QUIT]...")
                    continue
            except ValueError:
                print(f"Enter a number from 1 to {Pallaanguli.no_of_holes_per_player} [0 for QUIT]...")
                continue

            if hole == 0:
                return None

            hole = (hole - 1) + player * Pallaanguli.no_of_holes_per_player

            if self.board[hole] != '*' and self.board[hole] != 0:
                return hole
            else:
                print("Enter the hole which has coins...")
        else:
            print(f"Player {player+1} can not select any holes!\nThis round has done!!")
            
    def next_player(self,current_player:int) -> int:
        return (current_player + 1) % Pallaanguli.no_of_players
    
    def round_finish(self) -> None:
        
        check = True
        
        for player in range(Pallaanguli.no_of_players):
            if self.round_over_check(player):
                check = False
                player = self.next_player(player)
                
                start = player*Pallaanguli.no_of_holes_per_player
                end = start + self.no_of_holes[player]

                ramaining_coins = sum(self.board[start:end])
                self.coins[player] += ramaining_coins
                
                break
        
        if check:
            print("Look like the round has not finished!")
    
    


def round(first_player:int = 0, coins:tuple = (35,35)) -> list:
    
    theboard = Pallaanguli(coins)
    
    theboard.display_board()
    
    player = first_player
    
    round_check = not theboard.round_over_check(player)
    
    while round_check:
        hole = theboard.player_input(player)
        
        if hole is None:
            return None
        
        theboard.player_turn(player, hole)
        theboard.display_board()

        player = theboard.next_player(player)
        round_check = not theboard.round_over_check(player)
    
    print("This round has done!")
    theboard.round_finish()

    
    return theboard.coins

def main():
    print("Welcome to Pallaanguli...!")

    coins = [Pallaanguli.init_coins_per_player] * Pallaanguli.no_of_players

    r = 1 
    check = False
    player = 0
    while True:
        print(f"Round:{r}")
        coins = round(player,tuple(coins))

        if coins is None:
            check = True
            break

        print(f"Result of round:{r}")
        for p in range(Pallaanguli.no_of_players):
            print(f"Player {p+1}: {coins[p]}")

        if coins[0] >= Pallaanguli.coins_per_hole and coins[1] >= Pallaanguli.coins_per_hole:
            r += 1

            ch = str(input(f"Do you want to go next round (Round:{r}) ('Y'/'N'): ")).upper()

            if ch == 'N':
                check = True
                break

            if player == 0:
                player = 1
            else:
                player = 0

        else:
            break

    if check:
        print("Thanks for playing...")
    elif coins[1] < Pallaanguli.coins_per_hole:
        print("Player 1 wins the game...!")
    else:
        print("Player 2 wins the game...!")

if __name__ == "__main__":
    main()

