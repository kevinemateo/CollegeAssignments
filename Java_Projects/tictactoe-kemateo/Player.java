/*
 *
 * @author
 */
public class Player {
	// INSTANCE DATA: name, wins, losses
	private String name;
	private int wins;
	private int losses;
	//CONSTRUCTOR
	public Player(String playerName)
	{
		this.name = playerName;
		wins=0;
		losses=0;
	}
	// METHODS
	// getName(), setName(), getWins(), getLosses(), toString(), etc
	public void setName(String name)
	{
		this.name = name;
	}
	public void addWin()
	{
		wins++;
	}
	public void addLoss()
	{
		losses++;
	}
	public String getName()
	{
		return name;
	}
	public int getWins()
	{
		return wins;
	}
	public int getLosses()
	{
		return losses;
	}
	public String toString()
	{
		String result;
		result = "Name: " + this.name + " W: " + wins + " L: " + losses;
		return result;
	}
}
