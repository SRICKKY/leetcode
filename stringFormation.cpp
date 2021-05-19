// C++ Program to Count the number of ways to 
// construct the target string 
#include <bits/stdc++.h> 

using namespace std; 

int mod = 1000000007; 

int dp[1000][1000]; 

int calculate(int pos, int prev, string s, vector<int>* index) 
{ 

	// base case 
	if (pos == s.length()) 
		return 1; 

	// If current subproblem has been solved, use the value 
	if (dp[pos][prev] != -1) 
		return dp[pos][prev]; 

	// current character 
	int c = s[pos] - 'a'; 

	// search through all the indiced at which the current 
	// character occurs. For each index greater than prev, 
	// take the index and move 
	// to the next position, and add to the answer. 
	int answer = 0; 
	for (int i = 0; i < index.size(); i++) { 
		if (index[i] > prev) { 
			answer = (answer % mod + calculate(pos + 1, 
						index[i], s, index) % mod) % mod; 
		} 
	} 

	// Store and return the solution for this subproblem 
	return dp[pos][prev] = answer; 
} 

int countWays(vector<string>& a, string s) 
{ 
	int n = a.size(); 

	// preprocess the strings by storing for each 
	// character of every string, the index of their 
	// occurrence we will use a common list for all 
	// because of only the index matter 
	// in the string from which the character was picked 
	vector<int> index[26]; 

	for (int i = 0; i < n; i++) { 
		for (int j = 0; j < a[i].length(); j++) { 

			// we are storing j+1 because the initial picked index 
			// in the recursive step will ne 0. 
			// This is just for ease of implementation 
			index[a[i][j] - 'a'].push_back(j + 1); 
		} 
	} 

	// initialise dp table. -1 represents that 
	// the subproblem hasn't been solved 
	memset(dp, -1, sizeof(dp)); 

	return calculate(0, 0, s, index); 
} 

// Driver Code 
int main() 
{ 
	vector<string> A; 
	A.push_back("adc"); 
	A.push_back("aec"); 
	A.push_back("erg"); 

	string S = "ac"; 

	cout << countWays(A, S); 

	return 0; 
} 
