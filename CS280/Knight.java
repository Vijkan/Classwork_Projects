//Mihir kandlur

class Main {
    public static void main(String[] args) {
        boolean solved = false;
        int[][] board = new int[8][8];
        int[] correctsol = new int[64];
        int[][] lastsplit = new int[64][2];
        int[][] triedmoves = new int[65][8];

        int movenum = 0;
        int bnum = 1;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                board[i][j] = bnum++;
            }
        }

        int currrow = 0;
        int currcol = 0;
        int testrow, testcol;
        int y = 0;
        correctsol[movenum] = board[0][0];
        Check.visited[board[0][0]] = board[0][0];
        movenum++;

        while (!solved) {
            boolean moved = false;
            for (int dir = 0; dir < 8; dir++) {
                int[] drow = {2, 2, -2, -2, 1, 1, -1, -1};
                int[] dcol = {1, -1, 1, -1, 2, -2, 2, -2};
                testrow = currrow + drow[dir];
                testcol = currcol + dcol[dir];

                if (testrow >= 0 && testrow < 8 && testcol >= 0 && testcol < 8
                        && triedmoves[board[currrow][currcol]][dir] == 0) {
                    triedmoves[board[currrow][currcol]][dir] = -1;
                    if (!Check.check(testrow, testcol, board)) {
                        correctsol[movenum] = board[testrow][testcol];
                        lastsplit[y][0] = currrow;
                        lastsplit[y][1] = currcol;
                        currrow = testrow;
                        currcol = testcol;
                        movenum++;
                        y++;
                        moved = true;
                        break;
                    }
                }
            }

             if (movenum == 64) {
                solved = true;
            }
        }

        if (solved) {
            for (int z = 0; z < 64; z++) {
                System.out.println(correctsol[z]);
            }
        } else {
            System.out.println("No solution found.");
        }
    }

    static class Check {
        static int[] visited = new int[65];

        public static boolean check(int testrow, int testcol, int[][] board) {
            return visited[board[testrow][testcol]] != 0 || (visited[board[testrow][testcol]] = board[testrow][testcol]) == 0;
        }
    }
}
