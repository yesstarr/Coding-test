#include <iostream>
#include <cstring>
#include <string>
using namespace std;
int main() 
{
	string s;
	int a[26];
	getline(cin, s);
	for (int i = 0; i < 26; i++)
	{
		a[i] = 0;
	}
	for (int i = 0; i < s.length(); i++)
	{
		for (int k = 0; k < 26; k++)
		{
			if (s[i] == 'a' + k)
				a[k] += 1;
		}
	}
	for (int i = 0; i < 26; i++)
	{
		cout << a[i] << ' ';
	}
}