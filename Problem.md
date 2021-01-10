## Problem Statement

- Make a webpage at (https://localhost:8000/frequency) 
- which contains a form. Form takes a url has input.. 
- This webpage makes a post request to another webpage (https://localhost:8000/result ). 
- Upon landing on https://localhost:8000/result ,
- It should process the URL received from https://localhost:8000/frequency 
- and then the backend should visit and extract the text present on the URL’s Webpage and  
- process the text (Do not process the Html markup,only the rendered text) and 
- display the top 10 most frequent words along with their respective frequency in descending order. 
- (Ignore common words like a, the has, have, etc).