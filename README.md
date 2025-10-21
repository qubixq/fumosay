# FumoSay ᗜˬᗜ

> “⑨ says hello!”  
> A extensible **Fumo-themed cowsay alternative** written in Python.


## Installation

```bash
git clone https://github.com/qubixq/fumosay
cd fumosay
python3 fumosay.py "Fumo strong!"
```
## Usage
```bash
python fumosay.py [options] "Your message here"
```
<img width="339" alt="image" src="https://github.com/user-attachments/assets/ca7417bd-1801-428b-b6ab-c83b7d7cc56b" />


## Options
```bash
Option	Description
-s, --style	Select ASCII/Braille art style (style1, style2, style3 or 1, 2, 3)
-t, --think	Use a thought bubble instead of a speech bubble
-w, --width	Set maximum text wrapping width
-f, --file	Read the message text from a file
(no args)	Reads input from stdin
```
## Example Commands

### Default style (Cirno)
```bash
python fumosay.py "I'm the Strongest!"
```
<img width="207" alt="image" src="https://github.com/user-attachments/assets/81652e7e-cec4-4d25-b7b4-9aadd308acb3" />

### Use a more detailed style
```bash
python fumosay.py -s style2 "Baka baka!"
```
<img width="207" alt="image" src="https://github.com/user-attachments/assets/3cee0bcb-7c0f-4754-ac55-b22219ed400b" />

### Short style selector
```bash
python fumosay.py -s 2 "9"
```
<img width="207" alt="image" src="https://github.com/user-attachments/assets/d4ecc403-9159-4ccc-be67-c9c7a6223748" />

### Long message, wider wrap
```bash
python fumosay.py -s 3 -w 60 "This is a long message that even Fumo needs space to say!"
```
<img wwidth="207" alt="image" src="https://github.com/user-attachments/assets/8cd51cda-f5e0-4cb6-860d-7a531b3ef960" />

### Thought bubble
```bash
python fumosay.py -t -s 2 "Hmm..."
```
<img width="207" alt="image" src="https://github.com/user-attachments/assets/b974f84e-c5e9-4bec-8d43-fd23cd3296d6" />

🎭 Available Styles
```bash
Style	Description
style1	Epic Cirno Fumo
style2	Side View Cirno Fumo
style3	Hamburger Cirno Fumo
```
💡 **Note:** I'm planning to add new Fumos soon (such as Reimu, Sakuya, and more Fumo!)

Because your terminal deserves a little Fumo magic.
> "Fumo Fumo"
