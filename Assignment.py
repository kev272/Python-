#1.A program to check if a year is a leap year or not
year=2016
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")



#2.A program to check if a letter is a consonant or vowel
letter="c"
if letter  in "aeiou":
    print(letter, "is vowel")
else:
    print(letter, "is not vowel")