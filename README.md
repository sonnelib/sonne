![Logo](https://raw.githubusercontent.com/sonnelib/sonne/main/logo.png)

# Sonne

**Sonne** is a Python module that provides a lot of possibilities to make your terminal look beautiful.

![Features](https://raw.githubusercontent.com/sonnelib/sonne/main/sonne.png)

# Setup

```python
pip install sonne
```
```python
python -m sonne
```

# Documentation

## Text

**Sonne** has a ``Text`` class that you can use wherever strings are accepted and customize it with parameters.

Example usage:
```python
import sonne

x = sonne.Text("Hello, World!", fg="blue", bg="white", style="italic").styled()
print(x)
```
This will print colored and styled ``Hello, World!`` in the terminal.

Also you can use like this:
```python
import sonne

x = sonne.Text("Hello,", "World!", fg="blue", bg="white", style="italic").styled()
print(x)
```
This will also print colored and styled ``Hello, World!`` in the terminal.

## Progress

**Sonne** has a ``Progress`` class where you can create customizable progress bars.

Example usage:
```python
import sonne

total = 50
progressbar = sonne.Progress(total=total, desc="Download", length=40)

for i in range(total):
    progressbar.update(i)
    time.sleep(0.1)
```
Output:

![Progress](https://raw.githubusercontent.com/sonnelib/sonne/main/progress.png)

## Tree

**Sonne** has a ``Tree`` function which can generate a customizable tree view.

Example usage:
```python
import sonne

x = ["A", ["B", ["C"], ["D"]]]

sonne.Tree(x, depth=0, islast=True)
```
Output:

```
┗━━ A
    ┃━━ B
        ┗━━ C
    ┗━━ D
```

## JSON

**Sonne** will automatically highlight expressions in JSON texts, such as integers, floats,booleans, arrays, strings etc. With ``JSON`` function.

Example usage:
```python
import sonne

code = """
{
    "value": "string",
    "value2": 1,
    "value3": null,
    "array": [2, 3, 5, 7]
}
"""
print(JSON(code))
```

This will print highlighted ``code`` in the terminal.

## Other Functions
``clear()``: Clears the terminal screen.

``typewrite(*text: str, duration)``: Prints strings with typewriter effect.

## Styles

A list of ``Text`` styles in **Sonne**.

| Name | Number |
|-------|---------|
| normal | 0 |
| bold | 1 |
| italic | 3 |
| underlined | 4 |
| reversed | 7 |
| hidden | 8 |
| strike | 9 |

## Colors

A list of the 8-bit ``Text`` colors in **Sonne**.

| Name | Number |
|-------|---------|
| black | 0 |
| red | 1 |
| green | 2 |
| yellow | 3 |
| blue | 4 |
| magenta | 5 |
| cyan | 6 |
| white | 7 |
| brightblack | 8 |
| brightred | 9 |
| brightgreen | 10 |
| brightyellow | 11 |
| brightblue | 12 |
| brightmagenta | 13 |
| brightcyan | 14 |
| brightwhite | 15 |
| grey0 | 16 |
| gray0 | 16 |
| navyblue | 17 |
| darkblue | 18 |
| blue3 | 20 |
| blue1 | 21 |
| darkgreen | 22 |
| deepskyblue4 | 25 |
| dodgerblue3 | 26 |
| dodgerblue2 | 27 |
| green4 | 28 |
| springgreen4 | 29 |
| turquoise4 | 30 |
| deepskyblue3 | 32 |
| dodgerblue1 | 33 |
| green3 | 40 |
| springgreen3 | 41 |
| darkcyan | 36 |
| lightseagreen | 37 |
| deepskyblue2 | 38 |
| deepskyblue1 | 39 |
| springgreen2 | 47 |
| cyan3 | 43 |
| darkturquoise | 44 |
| turquoise2 | 45 |
| green1 | 46 |
| springgreen1 | 48 |
| mediumspringgreen | 49 |
| cyan2 | 50 |
| cyan1 | 51 |
| darkred | 88 |
| deeppink4 | 125 |
| purple4 | 55 |
| purple3 | 56 |
| blueviolet | 57 |
| orange4 | 94 |
| grey37 | 59 |
| gray37 | 59 |
| mediumpurple4 | 60 |
| slateblue3 | 62 |
| royalblue1 | 63 |
| chartreuse4 | 64 |
| darkseagreen4 | 71 |
| paleturquoise4 | 66 |
| steelblue | 67 |
| steelblue3 | 68 |
| cornflowerblue | 69 |
| chartreuse3 | 76 |
| cadetblue | 73 |
| skyblue3 | 74 |
| steelblue1 | 81 |
| palegreen3 | 114 |
| seagreen3 | 78 |
| aquamarine3 | 79 |
| mediumturquoise | 80 |
| chartreuse2 | 112 |
| seagreen2 | 83 |
| seagreen1 | 85 |
| aquamarine1 | 122 |
| darkslategray2 | 87 |
| darkmagenta | 91 |
| darkviolet | 128 |
| purple | 129 |
| lightpink4 | 95 |
| plum4 | 96 |
| mediumpurple3 | 98 |
| slateblue1 | 99 |
| yellow4 | 106 |
| wheat4 | 101 |
| grey53 | 102 |
| gray53 | 102 |
| lightslategrey | 103 |
| lightslategray | 103 |
| mediumpurple | 104 |
| lightslateblue | 105 |
| darkolivegreen3 | 149 |
| darkseagreen | 108 |
| lightskyblue3 | 110 |
| skyblue2 | 111 |
| darkseagreen3 | 150 |
| darkslategray3 | 116 |
| skyblue1 | 117 |
| chartreuse1 | 118 |
| lightgreen | 120 |
| palegreen1 | 156 |
| darkslategray1 | 123 |
| red3 | 160 |
| mediumvioletred | 126 |
| magenta3 | 164 |
| darkorange3 | 166 |
| indianred | 167 |
| hotpink3 | 168 |
| mediumorchid3 | 133 |
| mediumorchid | 134 |
| mediumpurple2 | 140 |
| darkgoldenrod | 136 |
| lightsalmon3 | 173 |
| rosybrown | 138 |
| grey63 | 139 |
| gray63 | 139 |
| mediumpurple1 | 141 |
| gold3 | 178 |
| darkkhaki | 143 |
| navajowhite3 | 144 |
| grey69 | 145 |
| gray69 | 145 |
| lightsteelblue3 | 146 |
| lightsteelblue | 147 |
| yellow3 | 184 |
| darkseagreen2 | 157 |
| lightcyan3 | 152 |
| lightskyblue1 | 153 |
| greenyellow | 154 |
| darkolivegreen2 | 155 |
| darkseagreen1 | 193 |
| paleturquoise1 | 159 |
| deeppink3 | 162 |
| magenta2 | 200 |
| hotpink2 | 169 |
| orchid | 170 |
| mediumorchid1 | 207 |
| orange3 | 172 |
| lightpink3 | 174 |
| pink3 | 175 |
| plum3 | 176 |
| violet | 177 |
| lightgoldenrod3 | 179 |
| tan | 180 |
| mistyrose3 | 181 |
| thistle3 | 182 |
| plum2 | 183 |
| khaki3 | 185 |
| lightgoldenrod2 | 222 |
| lightyellow3 | 187 |
| grey84 | 188 |
| gray84 | 188 |
| lightsteelblue1 | 189 |
| yellow2 | 190 |
| darkolivegreen1 | 192 |
| honeydew2 | 194 |
| lightcyan1 | 195 |
| red1 | 196 |
| deeppink2 | 197 |
| deeppink1 | 199 |
| magenta1 | 201 |
| orangered1 | 202 |
| indianred1 | 204 |
| hotpink | 206 |
| darkorange | 208 |
| salmon1 | 209 |
| lightcoral | 210 |
| palevioletred1 | 211 |
| orchid2 | 212 |
| orchid1 | 213 |
| orange1 | 214 |
| sandybrown | 215 |
| lightsalmon1 | 216 |
| lightpink1 | 217 |
| pink1 | 218 |
| plum1 | 219 |
| gold1 | 220 |
| navajowhite1 | 223 |
| mistyrose1 | 224 |
| thistle1 | 225 |
| yellow1 | 226 |
| lightgoldenrod1 | 227 |
| khaki1 | 228 |
| wheat1 | 229 |
| cornsilk1 | 230 |
| grey100 | 231 |
| gray100 | 231 |
| grey3 | 232 |
| gray3 | 232 |
| grey7 | 233 |
| gray7 | 233 |
| grey11 | 234 |
| gray11 | 234 |
| grey15 | 235 |
| gray15 | 235 |
| grey19 | 236 |
| gray19 | 236 |
| grey23 | 237 |
| gray23 | 237 |
| grey27 | 238 |
| gray27 | 238 |
| grey30 | 239 |
| gray30 | 239 |
| grey35 | 240 |
| gray35 | 240 |
| grey39 | 241 |
| gray39 | 241 |
| grey42 | 242 |
| gray42 | 242 |
| grey46 | 243 |
| gray46 | 243 |
| grey50 | 244 |
| gray50 | 244 |
| grey54 | 245 |
| gray54 | 245 |
| grey58 | 246 |
| gray58 | 246 |
| grey62 | 247 |
| gray62 | 247 |
| grey66 | 248 |
| gray66 | 248 |
| grey70 | 249 |
| gray70 | 249 |
| grey74 | 250 |
| gray74 | 250 |
| grey78 | 251 |
| gray78 | 251 |
| grey82 | 252 |
| gray82 | 252 |
| grey85 | 253 |
| gray85 | 253 |
| grey89 | 254 |
| gray89 | 254 |
| grey93 | 255 |
| gray93 | 255 |