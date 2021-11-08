def palindrome(s):
	if s[::-1] == s:
		return True
	return False
s = input()
if palindrome(s) == True:
	print("Plaindrome")
else:
	print("Not Plaindrome")