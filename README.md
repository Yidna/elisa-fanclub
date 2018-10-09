# CPSC 410 - DSL project for CPSC410 using OpenCV
# Group 2   
Andy Siu  
Cindy Hsu  
Gavin Ham  
Gary Gao   
Ryan Lee   

# To install packages
```python
pip install -r requirements.txt
```

# To run a sample of our [EBNF](./grammar/ebnf.txt)
```
python main.py
```
will read in the file input.cvdsl, parse and evaluate.


# Features

Type-checking  
Error-handling  
Built-in functions  
Parameters  
Variables  
Declaration of functions  

# Built-in functions

Blur (Applies Gaussian blur onto an image)  
Brighten (Increases brightness of hsv)  
Crop (Crops image from the middle with params)  
Darken (Darkens image by reducing gamma)  
Draw (Overlay an image onto the an image over another image)  
Find (Applies template matching and draws a rectangle over the match)  
Grayscale (Applies the grayscale to an image)
Resize (Resize image using bicubic interpolation)
Tile (Produces a tiled version of the image)

# Code
[main](./main.py)
[tokenizer](./libs/tokenizer.py)
[symbol table](./libs/symbol_table.py)
[node](./libs/node.py)
[exceptions](./functionality/exceptions)
[image folder](./images)

