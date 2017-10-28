============
Fencing
============


************
Introduction
************
This code distributes fencers amongst pools. It reads in a file of fencers and outputs on the screen back pools with associated fencers.

============
Dependencies
============

Python Version

Python 2.7 is needed to run the code. You can find a video on how to install it on Linux on this video: `https://www.youtube.com/watch?v=6vpHfG8E8JI <https://www.youtube.com/watch?v=6vpHfG8E8JI>`_. The windows equivalent can be found on: `https://www.youtube.com/watch?v=yiB9mVtKMz0 <https://www.youtube.com/watch?v=yiB9mVtKMz0>`_. This code was build on Linux and only tested there. However, it should run find on windows or mac.

Operating System
This was built using Ubuntu. However, since no special library was used, in theory, it should work on Windows or Mac.

============
Usage
============
To run the code directly, run:
**python [PATH]/fencing.py  "[DATA_FILE]"**

Where

- [PATH] is the path of fencing.py
- [DATA_FILE] is a CSV (comma-separated file) contain data on fencers

This assumes you denote *python 2.7 as "python"*. Change it if you use a different denotation.

The project has a data-folder that stores sample data. So, for example, to run that data, you can run:

    **python ./fencing/fencing.py "data/MEconflicts.csv"**


If you want debugging information, you can run the verbose option with:
    **python ./fencing/fencing.py -v "data/MEconflicts.csv"**


For help run:
    **python ./fencing/fencing.py -h**


If you want an executable, in the code, I created one at:
    **dist/fencing-1.0.0.tar.gz**


The file needs to be uncompressed


This code should work. Contact me at greenish_green@yahoo.com if you have any problem running the code.

============
Style
============
My programming style is to many files do one specific thing and do it well. I truly believe in the single responsibility principle. I admit, I sometime use it to a fault where there are many files which add a bit of complexity some other developers do not like (sometimes that Robert Martin (Uncles Bob) calls a "sea of files".) Anything not related to modules's core purpose is outsources to another module focused on that. I use folders to guide me to where I can find resources. For example, fencing at the root of the project tells me that this folder holds all the Pool-distribution code. The model subfolder tells me where I can get a module that hold data. The service folder by its name tell me where I can find thing that do heavy lifting.

============
Architecture
============
The file: **fencing.py** is the entry point into the application. It is an orchestration module that gathers the pieces and functionality of other modules and use them to make this application work.

The library: **argparse** module is used to parse the command line arguments.

All data types are stored in the **model** folder. In a way, it can be considered an active model because it does some processing. However, it does not read external files. It does minimum processing and its primary job is to hold data. The **fencer.py** file holds data on fencers (the players, the participants.) The **pool.py** file holds data on pools.

The **service** folder container code that does task. The file **dataReader.py** read the CSV file. The **display.py** file is used to display content to the screen. It is a wrapper around the Python print command. The **pool.py** file under the service folder (different from the one in model) does data processing on fencers-data and out put pools

The data folder contain sample data that can be used for testing.

The docs folder container standard files. However, the release subfolder contain information I used to code this application like user stories and acceptance criteria. While I did not strictly follow it, still, you can look into it if you are interested in some early thinkings I had about this application.

You can get a executable of this application in the dist folder. You need to uncompress the file in it.

The other files like AUTHORS.rst are standard python files.

============
Algorithms
============
You can find the code for distributing pools in **service/pool.py**. I created an Order dictionary (regulars dictionaries do not guarantee ordering) while the key is a club and the value of fencers associated to the club. The fencers are sorted by skills, beginning with the most skilled. I scrap off each fencers, starting from most talent, off each club; and then place them in a list. I continue this process until there are no fencers in the dictionary.
When the dictionary is empty, I place the fencers in the pool in a sepentine manner.

To create pools, I find the modulus between fencers-count and 6. If the remainder is greater than 1, I repeat this but with 7. If the remainder is also greater than 1, I divide fencers in groups of 5.

To sort by skills, I convert the skill (e.g. A15) into a numeric value. This makes it easier to sort. The exact means is in the code. The formula was picked arbitrary, so that alphabet part is greater than a other alphabets that come next but cannot be subsumed by the year. The grade U was given a arbitrary value that makes it weigh less that other grades.

Fencers with no club were given an faux club. However, the club is not displayed on the final print-out.

============
Contributor
============
This code was solely developed by me- Philip Adenekan. While I used resources like Pluralsight, bing.com, stackoverflow, YouTube and other common tools, to learn things, I did not ask for nor receive assistance directly from anyone- Everything is solely my work. I have a strong background in JavaScript and in the Microsoft stack. However, that does not mean I cannot quickly pick up a new stack (sometimes in minutes). Many stacks share the same principles, so adjusting is not hard, especially when there is a strong incentive like if successful, I can work with some bright people and researcher. Only locally, I used git to store versions of the code, in case I need to rollback. However, I have pushed this code to any public repository or given it to anyone.


============
License
============
This code can be used by anyone employed by the University of California at Santa Cruz or by anyone the aforementioned person chooses; for the purpose of evaluating my (Philip Adenekan) programming skills and thought process.



============
Further Work
============
 - I am quite busy at work and I have commitments to a side project of a friend who is starting a startup, so I had to make some sacrifices. I had to sacrifice unit test. Despite that, I truly believe in their value. If I had the time, I would of  had used the unittest modulue (rather than the pytest in setup.py)

 - I did not do much work to make the code compatible with python 3. This is something I would deem essential normally.


============
Questions
============
Contact me at: greenish_green@yahoo.com
