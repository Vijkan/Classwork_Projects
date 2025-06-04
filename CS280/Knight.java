//Mihir kandlur
class main {
    public static void main(String[] args) {
        boolean solved = false;
        int[][]  board =new int[8][8];
        int [] correctsol = new int[64];
        int[][] lastsplit= new int[64][2]; 
        int[][] triedmoves= new int [65][8];// keeps track of which moves have been tried on each board number
        int movenum= 0;//so I can put it in correct sol easy 
        int bnum = 1; //for board numbers
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                board[i][j] = bnum;
                System.out.println(bnum);
                bnum++;
                
            }
        }
        int currrow = 0;
        int currcol = 0;
        int testrow = 0;
        int testcol = 0;
        int y=0;//split
      correctsol[movenum] = board[0][0];
 Check.visited[board[0][0]] = board[0][0];
  movenum++;

        while (!solved){
            try {
                if (board[currrow+2][currcol+1] <8 && triedmoves[board[currrow][currcol]][0]!=-1){
                    triedmoves[board[currrow][currcol]][0]=-1;
                    testrow = currrow + 2;
                    testcol = currcol + 1;
                    if (!Check.check(testrow,testcol,board)){
                        correctsol[movenum]= board[testrow][testcol];
                        movenum++;
                        board[testrow][testcol]=-1;
                        lastsplit[y][0] = currrow;
                        lastsplit[y][1] = currcol;
                        currrow=testrow;
                        currcol=testcol;
                        y++;
                    }
                    else{
                        currrow=lastsplit[y][0];
                        currcol=lastsplit[y][1];
                        y--;
                        triedmoves[board[currrow][currcol]][0]=-1;
                        continue;
                    }

                }
                else if (board[currrow+2][currcol-1] <8 && board[currrow+2][currcol-1]>0 && triedmoves[board[currrow][currcol]][1]!=-1){
                    testrow = currrow + 2;
                    testcol = currcol - 1;
                    triedmoves[board[currrow][currcol]][1]=-1;
                    if (!Check.check(testrow,testcol,board)){
                        correctsol[movenum]= board[testrow][testcol];
                        movenum++;
                        board[testrow][testcol]=-1;
                        lastsplit[y][0] = currrow;
                        lastsplit[y][1] = currcol;
                        currrow=testrow;
                        currcol=testcol;
                        y++;
                        
                    }
                    else{
                        currrow=lastsplit[y][0];
                        currcol=lastsplit[y][1];
                        y--;
                        continue;
                    }
                }
                else if (board[currrow-2][currcol+1] <8 && board[currrow-2][currcol+1]>0 && triedmoves[board[currrow][currcol]][2]!=-1){
                    testrow = currrow - 2;
                    testcol = currcol + 1;
                    triedmoves[board[currrow][currcol]][2]=-1;
                    if (!Check.check(testrow,testcol,board)){
                        correctsol[movenum]= board[testrow][testcol];
                        movenum++;
                        board[testrow][testcol]=-1;
                        lastsplit[y][0] = currrow;
                        lastsplit[y][1] = currcol;
                        currrow=testrow;
                        currcol=testcol;
                        y++;
                        
                    }
                    else{
                        currrow=lastsplit[y][0];
                        currcol=lastsplit[y][1];
                        y--;
                        continue;
                    }
                }
                else if (board[currrow-2][currcol-1] <8 && board[currrow-2][currcol-1]>0 && triedmoves[board[currrow][currcol]][3]!=-1){
                    testrow = currrow - 2;
                    testcol = currcol - 1;
                    triedmoves[board[currrow][currcol]][3]=-1;
                    if (!Check.check(testrow,testcol,board)){
                       
                        correctsol[movenum]= board[testrow][testcol];
                        movenum++;
                        board[testrow][testcol]=-1;
                        lastsplit[y][0] = currrow;
                        lastsplit[y][1] = currcol;
                        currrow=testrow;
                        currcol=testcol;
                        y++;
                    }
                    else{
                        currrow=lastsplit[y][0];
                        currcol=lastsplit[y][1];
                        y--;
                        continue;
                    }
                }
                else if (board[currrow+1][currcol+2] <8 && board[currrow+1][currcol+2]>0 && triedmoves[board[currrow][currcol]][4]!=-1){
                    testrow = currrow + 1;
                    testcol = currcol + 2;
                    triedmoves[board[currrow][currcol]][4]=-1;
                    if (!Check.check(testrow,testcol,board)){
                        correctsol[movenum]= board[testrow][testcol];
                        movenum++;
                        board[testrow][testcol]=-1;
                        lastsplit[y][0] = currrow;
                        lastsplit[y][1] = currcol;
                        currrow=testrow;
                        currcol=testcol;
                        y++;
                        
                    }
                    else{
                        currrow=lastsplit[y][0];
                        currcol=lastsplit[y][1];
                        y--;
                        continue;
                    }

                }
                else if (board[currrow+1][currcol-2] <8 && board[currrow+1][currcol-2]>0 && triedmoves[board[currrow][currcol]][5]!=-1){
                    testrow = currrow + 1;
                    testcol = currcol - 2;
                    triedmoves[board[currrow][currcol]][5]=-1;
                    if (!Check.check(testrow,testcol,board)){
                        correctsol[movenum]= board[testrow][testcol];
                        movenum++;
                        board[testrow][testcol]=-1;
                        lastsplit[y][0] = currrow;
                        lastsplit[y][1] = currcol;
                        currrow=testrow;
                        currcol=testcol;
                        y++;
                        
                    }
                    else{
                        currrow=lastsplit[y][0];
                        currcol=lastsplit[y][1];
                        y--;
                       continue;
                    }
                }
                else if (board[currrow-1][currcol+2]<8 && board[currrow-1][currcol+2]>0 && triedmoves[board[currrow][currcol]][6]!=-1){
                    testrow = currrow - 1;
                    testcol = currcol + 2;
                    triedmoves[board[currrow][currcol]][6]=-1;
                    if (!Check.check(testrow,testcol,board)){
                        correctsol[movenum]= board[testrow][testcol];
                        movenum++;
                        board[testrow][testcol]=-1;
                        lastsplit[y][0] = currrow;
                        lastsplit[y][1] = currcol;
                        currrow=testrow;
                        currcol=testcol;
                        y++;
                        
                    }
                    else{
                        currrow=lastsplit[y][0];
                        currcol=lastsplit[y][1];
                        y--;
                        continue;
                    }
                }
                else if (board[currrow-1][currcol-2]<8 && board[currrow-1][currcol-2]>0 && triedmoves[board[currrow][currcol]][7]!=-1){
                    testrow = currrow - 1;
                    testcol = currcol - 2;
                    triedmoves[board[currrow][currcol]][7]=-1;
                    if (!Check.check(testrow,testcol,board)){
                        correctsol[movenum]= board[testrow][testcol];
                        movenum++;
                        board[testrow][testcol]=-1;
                        lastsplit[y][0] = currrow;
                        lastsplit[y][1] = currcol;
                        currrow=testrow;
                        currcol=testcol;
                        y++;
                        
                    }
                    else{
                        currrow=lastsplit[y][0];
                        currcol=lastsplit[y][1];
                        y--;
                        continue;
                    }
                }
        }  
            catch (ArrayIndexOutOfBoundsException e) {
                continue;
            }
            finally{
                if(movenum==64 && board[currrow][currcol]==1){
                    // once tried all if we're back on start than we must be done 
                    solved=true;
                    break;
                }
                else{
                    movenum--;
                }
            }
 
       
    }
       if (solved){
            for (int z=0;z<64;z++){
                System.out.println(correctsol[z]);
            }
        }
}
    
     static class Check extends main{
         static int[] visited=new int[65];//so i dont need to keep adding +1 -1's everywhere 
             public static boolean check (int testrow, int testcol,int[][]  board){
                if (visited[board[testrow][testcol]]!=0){
                    return true;
                }
                else{
                    visited[board[testrow][testcol]]=board[testrow][testcol];
                    return false;
                }
        }
     }
    }    
    

    

