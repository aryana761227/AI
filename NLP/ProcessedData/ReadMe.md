#Normalize and Tokenize Data
####Abstraction
using library hazm I normalized the text and tokenized them.then my method returns a tuple size 2 which first element contains preprocess of label1 and the second preprocess of label2.
####Runnig Code
first install the hazm library:
######Linux
    
    sudo pip3 install hazm

######Windows(Run as administrator)

    py -3 -m pip install hazm
    

then run this command in command line in the /ProcessedData/src
######Linux
    
    python3 process_data.py

######Windows(Run as administrator)

    py -3 process_data.py
    
  