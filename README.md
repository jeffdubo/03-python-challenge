# Python Challenge

The following files are located in this repo

README.md - This file
PyBank folder
 - main.py - python code for the first part of the challenge
 - Resources/budget.csv - profit and loss data for analysis
 - analysis/analysis.txt - export of printed results to a text file
PyPoll folder
 - main.py - python code for the second part of the challenge
 - Resources/election_data.csv - election data for analysis
 - analysis/analysis.txt - export of printed results to a text file

Additional Notes

I used a list to store the results for printing to avoid repeating the same information for printing and writing to a text file. I zipped the list to easily write it to a text file, but had an issue where blank lines were exported as "". I initially didn't store the blank lines in the list and manually printed and wrote them to the text file. This worked but it was difficult to not write a blank line at the end of the text file. So, I decided to check for the blank entry/line an manually write a blank line to the text file. I'm guessing there's a better, more elegant way to do this but I couldn't figure it out.
