# Name: Spencer Lawry     
# Course: CPE 101  
# Instructor: Daniel Kauffman
# Assignment: Word Search   
# Term: Fall 2016        

# There is no way to test my functions using assert statements.
# Instead I just ran the input file and checked to see if I got the words in the right positions

# The below explanation is why.

# import wordsearch
# assert wordsearch.find_forward("100 letter string here...That's why I can't test it", search words)

# I'm guessing that the intended way to do this project was have each "find_xxxxx" function
# not depend on the puzzle string itself, but instead be a search loop that searches any size puzzle 
# without transposing it 

# What I did was rotated or reversed the puzzle to search it as if it were forward, but that required 
# me to have access to the puzzles in my functions themselves. 
