import os
from sonne import Text, JSON, Tree, clear

clear()
os.system("")
arrow = Text(">", fg="brightyellow", style="bold").styled()
eight = Text("8", fg="grey93", style="bold").styled()
line = Text("-", fg="grey89", style="bold").styled()
b = Text("B", fg="grey85", style="bold").styled()
i = Text("i", fg="grey82", style="bold").styled()
t = Text("t", fg="grey78", style="bold").styled()
c = Text("C", fg="grey74", style="bold").styled()
o = Text("o", fg="grey70", style="bold").styled()
l = Text("l", fg="grey66", style="bold").styled()
o2 = Text("o", fg="grey62", style="bold").styled()
r = Text("r", fg="grey58", style="bold").styled()
s = Text("s", fg="grey54", style="bold").styled()
print(Text("Sonne", fg="brightyellow", style="bold").styled())
print("")
print(Text("Colors:", fg="brightyellow", style="bold").styled())
print(arrow , eight + line + b + i + t + " " + c + o + l + o2 + r + s)
print("")
for i in range(0, 8):
    for j in range(0, 64):
        code = str(i * 16 + j)
        print(u"\u001b[38;5;" + code + "m█", end="")
    print(u"\u001b[0m")
print(Text("+ more!", fg="brightyellow", style="bold").styled())
print("")
print(Text("Styles:", fg="brightyellow", style="bold").styled())
print(arrow, Text("Sonne", fg="brightyellow", style="italic").styled(), "supports most ANSI styles", Text("bold", style="bold").styled(), Text("italic", style="italic").styled(), Text("underlined", style="underlined").styled(), Text("strike", style="strike").styled(), Text("reversed", style="reversed").styled(), "+ more!")
print("")
print(Text("Trees:", fg="brightyellow", style="bold").styled())
treelist = [Text("A", fg="brightyellow", style="bold").styled(), ["B", ["C", ["D"]]], Text("E", fg="brightyellow", style="bold").styled()]
Tree(treelist, depth=0, islast=True)
print("")
print(Text("JSON Syntax Highlighting:", fg="brightyellow", style="bold").styled())
code = """
{
    "package": "sonne",
    "int": 1,
    "none": null,
    "array": [2, 3, 5]
}
"""
print(JSON(code))
print(Text("+ Typewriter effect, progress bars, etc...", fg="brightyellow", style="bold").styled())