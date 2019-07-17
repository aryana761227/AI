# Data Scraping
#### Abstraction
I hadn't tweeter dev account so I had to scrape that without tweepy's API.
By scrutining in tweeter html tags I found out that there are some order in each tweet box which is like this :

	<html>
	  <body>
	    ...
	    ...
	    ...
        <div class="tweet'>
          <div class="content">
            <div class="js-tweet-text-container">
              <p>
              {tweet.text}
              </p>
              </div>
          </div>
        </div>
        ...
        ...
        ...
      </body>
    </html>

then I use this pattern to parse them with beautifulsoap4 library.and i stored this data in two txt file in /Data/ folder.

####Running Code

First install these libraries

######Linux
    
	sudo pip install beautifulsoup4
    sudo pip install io
    sudo pip install csv

######Windows(Run as administrator)
    py -3 -m pip install beautifulsoup4
    py -3 -m pip install io
    py -3 -m pip install csv
    
then go in /Data/src folder and run this command:

######Linux
	python3 tweetter_scrapper.py
######Windows(Run as administrator)
    py -3 tweetter_scrapper.py

now you have two txt files which each line of those are a tweet of EsteghlalFc club or Perspolis tweets.