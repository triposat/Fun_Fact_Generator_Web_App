![](http://ForTheBadge.com/images/badges/made-with-python.svg)
![](https://forthebadge.com/images/badges/built-by-developers.svg)</br>
[![Prettier](https://img.shields.io/badge/Code%20Style-Prettier-red.svg)](https://github.com/prettier/prettier)
![Size](https://img.shields.io/github/repo-size/Iamtripathisatyam/Fun_Fact_Generator_Web_App?color=red&label=Repo%20Size%20)
![](https://img.shields.io/tokei/lines/github/Iamtripathisatyam/Fun_Fact_Generator_Web_App?color=red&label=Lines%20of%20Code)</br>
![sds](https://profile-counter.glitch.me/{Fun_Fact_Generator_Web_App}/count.svg)

Essentially, it will create interesting facts at random and display them on the web interface. This script will retrieve data from ***uselessfacts.jsph.pl*** with the help of ***GET*** method, and we will use the requests and the ***JSON*** module to acquire and load the data respectively. After the data has been loaded, just pass the text within the dictionary so that we can only get the jokes. For creating a simple and interactive interface on the web, we will use the ***PyWebIO*** module.

### Installation:
```python 
pip install pywebio
```
### Import the modules:
```python
import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
```
### Stepwise explanation: 
- Import all the required modules
- Send GET requests with the ***requests.request()*** method, and use the ***json.loads()*** function to parse a valid JSON message and transform it to a Python Dictionary. Since the requests function will create a dictionary of items, and we only need text, so we will pass response.text inside the json module.
- Now, because we need the text, i.e. Facts, we will pass the text within the data list and print the facts using the style function defined in the pywebio module. Because data is a dictionary of random jokes involving several useless items, we will just get the text section.

### Output:

<p align="center"><img width="80%" src="https://user-images.githubusercontent.com/69134468/127766215-e48c4b83-e9fa-4ab2-b33a-e96bd7544c82.gif"></p>
