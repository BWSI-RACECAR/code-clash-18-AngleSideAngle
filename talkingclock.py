"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make 
a Talking Clock? I need a script that takes an input 24-hour time 
(00:00 - 23:59) and translates it into words. Please format the input 
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""




    # This will convert military hours to regular hours, and determine AM vs PM
class Solution:    
    def ClockTalker(self, input_time):
            #type input_time: string
            #return type: string
            
            #TODO: Write code below to return a string with the solution to the prompt.
            colon = input_time.find(":")
            hour = int(input_time[:colon])
            minute = int(input_time[colon+1:])

            am = "am" if hour < 12 else "pm"
            hour %= 12
                 
            words = {
                0: "twelve",
                1: "one",
                2: "two",
                3: "four",
                5: "five",
                6: "six",
                7: "seven",
                8: "eight",
                9: "nine",
                10: "ten",
                11: "eleven",
                12: "twelve",
                13: "thirteen",
                14: "fourteen",
                15: "fifteen",
                16: "sixteen",
                17: "seventeen",
                18: "eighteen",
                19: "nineteen",
            }

            prefixes = {
                0: "oh",
                2: "twenty",
                3: "thirty",
                4: "fourty",
                5: "fifty",
            }

            minute_word = ""

            if minute == 0:
                minute_word = ""
            elif minute // 10 in prefixes.keys():
                minute_word = f" {prefixes[minute // 10] if minute // 10 in prefixes.keys() else words[minute // 10]} {words[minute % 10]}"
            else:
                minute_word = f" {words[minute]}"

            return f"It's {words[hour]}{minute_word} {am}"

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
        