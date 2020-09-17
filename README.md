Patent Document comparision system

Patcom which means "PATENT DOCUMENT COMPARISON SYSTEM" Is an C-DAC ( Centre for Development of Advanced Computing ) sponsored project, which was built by me and my team under the guidance of C-DAC Officials.

Basically the primary motive of Patcom is to speedup the patent filling process by reducing the man work required to ensure the distinctiveness of an idea of an newly filled patent as compared to the previously filled patents.

To accomplish this, Patcom takes two patent documents as input and gives an comparative summary of two patent documents. And also analyzes and summarizes patent document in terms of similarities and differences.

---------------------------- IMPLEMENTATION -------------------------------------------------------------------

The project is divided into 4 module each module is kept in their respective directory.
'driver.py' contains the driver function which takes input as 2 pdf document and outputs their comparative summary.
All the requirements are noted in 'requirement.txt'.
The program to calculate rouge score is present in 'rouge_score.py'
'wrapper.py' is the GUI for project.
Patents for testing are present in 'patent_documents' folder.

Prerequisite:
The nltk package should be installed completely or else it would generate lookup error.
To avoid that, execute below 2 lines of code in python after installing nltk,
    import nltk
    nltk.download('all') in python

Steps to run:
1. Make sure that system has all requirements fulfilled as given in 'requirement.txt'
2. Run 'wrapper.py'
3. Input :
        GUI would require one pdf document which the system would compare every other document with.
        And the second input would be the path of the directory in which other documents are present which are to be compared.
4. On clicking 'generate summaries' button it would output the summaries.
