# CS172 - Assignment 2 (Retrieval)

## Team member 1 - Tsz Hin Lo

###### Language used, how to run your code, if you attempted the extra credit (stemming), etc. 
Language used: Python

    Run this code:
        First, Unzip ap89_collection_small.zip into a folder named 89_collection_small
        Next, you can need parse the data using parsing.py
            In your terminal, input the command:  .\parsing.py
        Now, you can input the command as the assignment descipted
        
       For example,
        Input: python VSM.py <query−file> <name−of−results−file>
        Your program should have TWO command line arguments:
        <query−file>: path to query file (path to query_list.txt) 
        <name−of−results−file>: name of output file / results file 

###### Provide a short explanation of the submission
    parsing.py : parsing all the corpus in 89_collection_small to output files that we need
      -term_count_doc.txt, term_index.txt, term_info.txt, termids.txt, docids.txt (documents on Assignment 1 extra credit)
    stopwords.txt : use for take out the stopword for document
    VSM.py: use for calculate TF, IDF, TF:IDF, Consine Similarity, find the top 10 score of each query
    helper.py : a helper for reading stopwords, remove_punctuation, remove_stopwords and stemming
    testing.txt: all consine similarity of each query for all corpus without ranking
    final_result.txt: the final output after the VSM executed
