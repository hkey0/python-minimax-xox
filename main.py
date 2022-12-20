class TicTacToe():
    def __init__(self) -> None:
        self.table = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
    

    def check_table(self, table: list):
        if sum(table[0]) == -15 or sum(table[1]) == -15 or sum(table[2]) == -15:
            return -1
        

        if sum(table[0]) == 15 or sum(table[1]) == 15 or sum(table[2]) == 15:
            return 1


        if table[0][0] + table[2][0] + table[1][0] == -15:
            return -1
        
        if table[0][0] + table[2][0] + table[1][0] == 15:
            return 1
        

        if table[0][1] + table[1][1] + table[2][1] == -15:
            return -1
        
        if table[0][1] + table[1][1] + table[2][1] == 15:
            return 1

        
        if table[0][2]  + table[1][2] + table[2][2] == -15:
            return -1
        
        if table[0][2]  + table[1][2] + table[2][2] == 15:
            return 1


        if table[0][0] + table[1][1] + table[2][2] == -15:
            return -1
        
        if table[0][0] + table[1][1] + table[2][2] == 15:
            return 1
        

        if table[0][2] + table[1][1]+ table[2][0] == -15:
            return -1
        
        if table[0][2] + table[1][1]+ table[2][0] == 15:
            return 1
        
        if 0 in table[0] + table[1] + table[2]:
            return "continue"
        
        return 0


    def minimax(self, isMaximazing):

        result = self.check_table(self.table)

        if result in [0, -1, 1]:
            return result


        if isMaximazing:
            best_score = 0

            for line in range(0, 3):
                for block in range(0, 3):
                    if not self.table[line][block]:
                        self.table[line][block] = 5

                        score = self.minimax(False)
                        self.table[line][block] = 0
                        if score > best_score:
                            best_score = score
                        
            return best_score
        

        if not isMaximazing:
            best_score = 0

            for line in range(0, 3):
                for block in range(0, 3):
                    if not self.table[line][block]:
                        self.table[line][block] = -5

                        score = self.minimax(True)
                        self.table[line][block] = 0
                        if score < best_score:
                            best_score = score
                        
            return best_score 


    def computer(self):
        best_score = 0
        a = 0
        b = 0

        for line in range(0, 3):
            for block in range(0, 3):
                if not self.table[line][block]:
                    self.table[line][block] = 5

                    score = self.minimax(False)
                    self.table[line][block] = 0
                    if score >= best_score:
                        best_score = score

                        a = line
                        b = block

        self.table[a][b] = 5
    

    def check_game(self):
        import sys
        data = {
            1: "BİLGİSAYAR KAZANDI",
            -1: "OYUNCU KAZANDI",
            0: "BERABERE!"
        }
        result = self.check_table(self.table)
        if result != "continue":
            print(data[result])
            sys.exit()
    

    def print_table(self):
        print("\n\n")
        data = {5: "X", -5: "O", 0: "-"}
        for row in self.table:
            for block in row:
                print("     " + data[block] + "  ", end="")

            print("\n")


    def user(self):
        sec = int(input("[1,9] Ağlama oyna: ")) - 1
        if not self.table[int(sec / 3)][sec%3]:
            self.table[int(sec / 3)][sec%3] = -5
        else:
            print("Oraya oynayamazsın.")
            self.user()
    

    def play_game(self):
        while True:
            self.computer()
            self.print_table()
            self.check_game()
            
            self.user()
            self.check_game()
            
    
game = TicTacToe()
game.play_game()
