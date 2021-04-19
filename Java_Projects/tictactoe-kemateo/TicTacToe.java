/*
 * TicTacToe class
 * @author 
 */
public class TicTacToe
{
	public static boolean occupied;
	public int row;
	public int col;
	public static int board[][] = new int[3][3];
	public TicTacToe()
	{
		for(int i=0;i<3;i++)
		{
			for(int j=0;j<3;j++)
			{	board[i][j]=0;	}
		}
	}
	public void setSpace(int player, int row, int col)
	{
		this.row=row;
		this.col=col;
		if(player==1)
		{
			board[row][col]=1;
		}
		else if(player==2)
		{
			board[row][col]=2;
		}
	}
	public int getSpot(int row, int col)
	{
		return board[row][col];
	}
	
	public int isWin()
	{
		int isWin = 0;
		//check crosses
		if(isWin==0)
		{
			if((board[0][0]==board[1][1] && board[1][1]==board[2][2]) || (board[0][2] == board[1][1] && board[1][1]==board[2][0]))
			{
				if(board[1][1]!=0)
				{
					isWin = board[1][1];
					System.out.println("Cross");
				}
			}
		}
		if(isWin==0)
		{
			//check horizontal
			for(int i=0;i<3;i++)
			{
				if((board[i][0]==board[i][1] && board[i][1]==board[i][2]))
				{
					if(board[i][0]!=0)
					{
						isWin = board[i][0];
						i=3;
						System.out.println("Horizontal");
					}
				}
			}
		}
		//check vertically
		if(isWin==0)
		{
			for(int i=0;i<3;i++)
			{
				if((board[0][i]==board[1][i] && board[1][i]==board[2][i]))
				{
					if(board[0][i]!=0)
					{
						isWin = board[0][i];
						i=3;
						System.out.println("Vertical");
					}
				}
			}
		}
		//if none are true, then no winner
		return isWin;
	}
	public boolean isFull()
	{
		boolean isFull=true;;
		for(int i=0;i<3;i++)
		{
			for(int j=0;j<3;j++)
			{
				if(board[i][j]==0)
				{
					isFull=false;
					break;
				}
			}
		}
		return isFull;
	}
	public boolean isAvailable(int row, int col)
	{
		boolean isAvailable=true;
		if(board[row][col]!=0)
		{
			isAvailable=false;
		}
		return isAvailable;
	}
	public String toString()
	{
	   String output;
		output  = "Print out a board.\n";
		for(int i=0;i<3;i++)
		{
			for(int j=0;j<3;j++)
			{
				output+=board[i][j] + " ";
			}
			output+="\n";
		}
		return output;
	}
}
