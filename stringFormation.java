// Java Program to Count the number of ways to 
// conthe target String 
import java.util.*; 

class GFG{ 

static int mod = 1000000007; 

static int [][]dp = new int[1000][1000]; 

static int calculate(int pos, int prev, String s, Vector<Integer> index) 
{ 

	// base case 
	if (pos == s.length()) 
		return 1; 

	// If current subproblem has been solved, use the value 
	if (dp[pos][prev] != -1) 
		return dp[pos][prev]; 


	// search through all the indiced at which the current 
	// character occurs. For each index greater than prev, 
	// take the index and move 
	// to the next position, and add to the answer. 
	int answer = 0; 
	for (int i = 0; i < index.size(); i++) { 
		if (index.get(i).compareTo(prev) >= 0) { 
			answer = (answer % mod + calculate(pos + 1, 
						index.get(i), s, index) % mod) % mod; 
		} 
	} 

	// Store and return the solution for this subproblem 
	return dp[pos][prev] = answer; 
} 

static int countWays(Vector<String> a, String s) 
{ 
	int n = a.size(); 

	// preprocess the Strings by storing for each 
	// character of every String, the index of their 
	// occurrence we will use a common list for all 
	// because of only the index matter 
	// in the String from which the character was picked 
	Vector<Integer> []index = new Vector[26]; 
	for (int i = 0; i < 26; i++) 
		index[i] = new Vector<Integer>(); 
	for (int i = 0; i < n; i++) { 
		for (int j = 0; j < a.get(i).length(); j++) { 

			// we are storing j+1 because the initial picked index 
			// in the recursive step will ne 0. 
			// This is just for ease of implementation 
			index[a.get(i).charAt(j) - 'a'].add(j + 1); 
		} 
	} 

	// initialise dp table. -1 represents that 
	// the subproblem hasn't been solved 
	for(int i = 0;i< 1000;i++) 
	{ 
		for (int j = 0; j < 1000; j++) { 
			dp[i][j] = -1; 
		} 
	} 

	return calculate(0, 0, s, index[0]); 
} 

// Driver Code 
public static void main(String[] args) 
{ 
	Vector<String> A = new Vector<String>(); 
	A.add("adc"); 
	A.add("aec"); 
	A.add("erg"); 

	String S = "ac"; 

	System.out.print(countWays(A, S)); 
} 
} 

// This code is contributed by Princi Singh 
