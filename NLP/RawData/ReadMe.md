# Load and store tweeter pages completely 

#### abstraction
1. The topic is the separation of the tweets from Esteghlal and Persepolis clubs.
2. To be able to find out someone is Esteghlal fan or Perspolis's via speaking and his/her tweeting in tweeter seems interesting, also helps in statistic.
3. Data gathering sources:
[https://twitter.com/FcEsteghlalIran](https://twitter.com/FcEsteghlalIran)
[https://twitter.com/persepolisFC](https://twitter.com/persepolisFC)
4. Using this two clubs tweeter's account, I tried to gather their tweets but in this phase just gather them and stored them in form of {team's nam}.html.(I had trouble in this part because tweeter doesn't load completely and i had to use selenium library which I had not used it before and got lots of help from [here](https://github.com/kishi001/scrape-twitter))
#### Running Code
First First download chromedriver to use only that tab for loading pages.(in this case you do not need that because I have downloaded it before and it is in /RawData/src/ folder )
First install this library :

Linux

	sudo pip install selenium

Windows(Run as administrator)

	py -3 -m pip install selenium

then run this command (if you want run this code you should have good internet(also good vpn) because it loads pages from internet else it won't be complete )

Linux

	python3 data_gathering.py   

Windows

	py -3 data_gathering.py

now you have two html files which are loaded completely and stored in /RawData/ folder.



