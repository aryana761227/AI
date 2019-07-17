###Running Code
In this part you just need to run the prepare data.py in the ClsData/src folder. if you want to change the processed data files just change file_1 and file_2 in the prepare_data.py.Data comination done with two thrads(the best random cominer) also choose a line for test/train done with random module.
if you want you can add stop words in bottom of stopwords.txt in this fodler.the outputs are in /ClsData folder.

######Linux
    
    python3 prepare_data.py

######Windows

    py -3 prepare_data.py 

for running the algorithm naive bayes you must first declare that you want datas or testcase if you enter 1 it will be testcase else it will be esteghlal/perspolis data.
then you must declare you want test mode or train mode if you want test mode you must enter 1 else you must enter 0 to train data(which is useless i just add this because we had in doc.
then you can run this code in command line:

######Linux
    
    python3 naive_bayes.py

######Windows

    py -3 naive_bayes.py 

outputs stored in both folder ClsData/output.txt, ClsData/TestCase/my-output and ClsModel/Test.output.txt and Cls/TestCase.output.txt folders.
