#!usr/bin/python

with open("numbers.html", "a") as html:
    
    html.write("<!DOCTYPE html>\n<html>\n   <body>\n")
    
    for num in range (1, 1000001):  #indent moved one space back for code to fucntion.
        line = str(num)

        #Numbers divisible by 10, add a bold tag.
        if num % 10 == 0:
            line = "<b>" + line + "</b>"

        #Numbers divisible by 3, add italics tag.
        if num % 3 == 0:
            line = "<i>" + line + "</i>"

        #Underline Prime numbers
        if num > 1 and (num == 2 or num % 2 !=0) and all(num % divisor in range(3, int(num ** 0.5) + 1, 2)):
            line = "<u>" + line + "</u>"

        html.write("  " + line + "<br>\n")
        
    html.write("</body>\n</html>")