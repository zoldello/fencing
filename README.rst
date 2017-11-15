================
Fencing Project
================

************
Introduction
************
This code divvies fencers amongst pools. It reads in a file of fencers and outputs a sorted list of fencers (competitors) and pools with associated fencers.

============
Dependencies
============


***************
Python Version
***************

Python 2.7 is best used to run the code. You can find a video on how to install it on Linux on this video: `https://www.youtube.com/watch?v=6vpHfG8E8JI <https://www.youtube.com/watch?v=6vpHfG8E8JI>`_. The windows equivalent can be found on: `https://www.youtube.com/watch?v=yiB9mVtKMz0 <https://www.youtube.com/watch?v=yiB9mVtKMz0>`_. Nevertheless, the was also built to work on Python 3.6.3.

***********************
Operating System
***********************

This was built using Ubuntu (Linux) and only tested on it. However, in theory, it should work on Windows or Mac.

============
Usage
============


****************************
Third Party Dependency
****************************
Use pip to install argparse:

    **pip install argparse**


To run the code directly, run this command:

    **python [PATH]/fencing.py  "[DATA_FILE]"**

Where

- [PATH] is the path of fencing.py
- [DATA_FILE] is a CSV (comma-separated file) contain data on fencers

This assumes you denote **python 2.7 as "python"**. Change it if you use a different denotation.

The project has a data-folder that stores sample data. So, for example, to run a sample data file, you can run any one of these commands to try out the project:

    - **python ./fencing/fencing.py "data/MEconflicts.csv"**
    - **python ./fencing/fencing.py "data/MEconflicts.csv"**
    - **python ./fencing/fencing.py "data/MEconflicts.csv"**




If you want debugging information, you can run the verbose option with: **-v**. Here is a sample commands:
    **python ./fencing/fencing.py -v "data/MEconflicts.csv"**

For help run:
    **python ./fencing/fencing.py -h**


If you want an executable, in the code, I created one by running:
    **python setup.py**

The resultant file will be stored at:
    **dist/fencing-1.0.0.tar.gz**

The .gz file needs to be uncompressed



====================
Programming Style
====================
My programming style is to make a module do one specific thing and do it well. I truly believe in the single responsibility principle. This adds some complexity as there may be many files, but I think it the benefits of this approach (like easier unit test and isolation) is worth that expense.  Anything not related to modules's core purpose is outsources to another module focused on that. I use folders to guide me to where I can find resources. For example, fencing at the root of the project tells me that this folder holds all the Pool-distribution code. The model subfolder tells me where I can get a module that hold data. The service folder by its name tell me where I can find thing that do heavy lifting- aka provide service.

============
Architecture
============
The file: **fencing.py** is the entry point into the application. It is an orchestration module that gathers the pieces and functionality of other modules and use them to make this application work.

The library: **argparse** module is used to parse the command line arguments.

All data objects are stored in the **model** folder. In a way, it can be considered an active model because it does some processing. However, it does not read external files. It does minimum processing and its primary job is to hold data. The **fencer.py** file holds data on fencers (the players, the participants.) The **pool.py** file holds data on pools.

The **service** folder container code that does task. The file **dataReader.py** read the CSV file. The **display.py** file is used to display content to the screen. It is a wrapper around the Python print command. The **pool.py** file under the service folder (different from the one in model) does data processing on fencers-data and out put pools

The data folder contain sample data that can be used for testing.

The docs folder container standard files. However, the release subfolder contain information I used to code this application like user stories and acceptance criteria. While I did not strictly follow it, still, you can look into it if you are interested in some early thinkings I had about this application.

You can get a executable of this application in the dist folder. You need to uncompress the file in it (see Usage section).

The other files like AUTHORS.rst are standard python files.


============
License
============
MIT
