import java.util.*;

/* GameDriver - Client program that allows a user to play the Game TictacToe.
 * Main is the only method found here. Other static helper methods can 
 * be used to organize the statements in main.
 * @author : STUDENT NAME
 * 
 */
public class GameDriver 
{
	public static void main(String[] args)
	{
		int currentPlayer;
		int row;
		int col;
		int tie=0;
		boolean availability=false;
		boolean playAgain = true;
		Scanner scan = new Scanner(System.in);
		Player player1, player2 ;
		Random rand = new Random();
	//Create Player Objects
		System.out.println("> Enter the name of one Player:");
		String name1 = scan.nextLine();
		System.out.println("> Enter the name of the other Player:");
		String name2 = scan.nextLine();
		/*randomly choose who is first
			1=name1 Any Other Number=name2, whoever is called is player one*/
		int randomNumber = rand.nextInt(2)+1 ;
		if(randomNumber==1)
		{	
			player1 = new Player (name1);
			player2 = new Player(name2);
		}
		else
		{	
			player1 = new Player(name2);
			player2 = new Player(name1);    
		}
		//display who is Player 1 and Player 2
		System.out.println("Player 1: " + player1.getName());
		System.out.println("Player 2: " + player2.getName());
		System.out.println();
		
		while(playAgain==true)
		{
			TicTacToe board = new TicTacToe();
		//Play game
			System.out.println("Welcome Player 1: "+player1.getName());
			System.out.println("=======================");
			System.out.println("LET'S PLAY TIC TAC TOE!");
			System.out.println("=======================");
			boolean isFull=board.isFull();
			int isWin=0;
			while(isFull!=true && isWin==0)
			{
			//ask each user to pick their spots while checking if there is a winner
				//Player 1
				availability=false;
				if(isWin==0)
				{
					while(availability==false)
					{
						System.out.println(board);
						currentPlayer=1;
						System.out.println("Player 1 pick your spot ");
						System.out.println("Row:");
						row = scan.nextInt()-1;
						System.out.println("Column: ");
						col = scan.nextInt()-1;
						availability = board.isAvailable(row, col);
						if(availability == true)
						{
							board.setSpace(currentPlayer, row, col);
						}
						else
						{
							System.out.println("Space is unavailable \nTry again");
						}
					}
				}
				availability=false;
				isWin=board.isWin();
				System.out.println("\n"+isWin+"\n");
				//Player 2
				if(isWin==0)
				{
					while(availability==false)
					{
						System.out.println(board);
						currentPlayer=2;
						System.out.println("Player 2 pick your spot ");
						System.out.println("Row:");
						row = scan.nextInt()-1;
						System.out.println("Column: ");
						col = scan.nextInt()-1;
						availability = board.isAvailable(row, col);
						if(availability == true)
						{
							board.setSpace(currentPlayer, row, col);
						}
						else
						{
							System.out.println("Space is unavailable \nTry again");
						}
					}
				}
				isWin=board.isWin();
				System.out.println("\n"+isWin+"\n");
			}
			//why did the loop end? isFull or is there a winner
			System.out.println(board);
			if(isFull==true)
			{
				tie++;
				System.out.println("No winner. It was a tie. ");
			}
			else if(isWin==1)
			{
				player1.addWin();
				player2.addLoss();
				System.out.println("Congrats player 1. You are a winner. Player 2 you lose.");
			}
			else if(isWin==2)
			{
				player2.addWin();
				player1.addLoss();
				System.out.println("Congrats player 2. You are a winner. Player 1 you lose.");
			}
			//results
			System.out.println("Results: \nTies: " + tie);
			System.out.println("Player 1: \n\tWins: " + player1.getWins() + "\n\tLosses: " + player1.getLosses());
			System.out.println("Player 2: \n\tWins: " + player2.getWins() + "\n\tLosses: " + player2.getLosses());
			System.out.println();

			//check if users want to play again
			Scanner scan2 = new Scanner(System.in);
			System.out.println("Play again (y/n)? : ");
			String playAgainString = scan2.nextLine();
			if(playAgainString.toLowerCase()=="y")
			{
				playAgain=true;
			}
			else if(playAgainString.toLowerCase()=="n")
			{
				playAgain=false;
			}
			else
			{
				playAgain=false;
			}
		}
		System.out.println("Goodbye.");
	}
}
