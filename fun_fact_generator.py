import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
  
  
def get_fun_fact(_):
    
    # Clear the above screen
    clear()
  
    put_html("<p align=""left""><h2><img src=""https://\
             media.geeksforgeeks.org/wp-content/uploads/\
             20210720224119/MessagingHappyicon.png"" width=""7%"">  \
             Fun Fact Generator</h2></p>
")
      
    # URL from where we will fetch the data
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
      
    # Use GET request
    response = requests.request("GET", url)  
      
    # Load the request in json file
    data = json.loads(response.text)
               
    # we will need 'text' from the list, so 
    # pass 'text' in the list
    useless_fact = data['text']
               
    # Put the facts in the blue colour
    # Put the click me button
    style(put_text(useless_fact), 'color:blue; font-size: 30px')
    put_buttons(
        [dict(label='Click me', value='outline-success', 
              color='outline-success')], onclick=get_fun_fact)  
  
  
# Driver Function
if __name__ == '__main__':
      
    # Put a heading "Fun Fact Generator"
    put_html("<p align=""left""><h2><img src=""https://media.\
             geeksforgeeks.org/wp-content/uploads/20210720224119\
             /MessagingHappyicon.png"" width=""7%"">  \
             Fun Fact Generator</h2></p>
")
      
    # hold the session for long time
    # Put a Click me button
    put_buttons(
        [dict(label='Click me', value='outline-success', 
              color='outline-success')], onclick=get_fun_fact)  
hold()  
