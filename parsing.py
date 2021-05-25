import re, os, string, nltk
from helper import *

storing = {}

def ass1():
    doc_regex = re.compile("<DOC>.*?</DOC>", re.DOTALL)
    docno_regex = re.compile("<DOCNO>.*?</DOCNO>")
    text_regex = re.compile("<TEXT>.*?</TEXT>", re.DOTALL)

    termid = 0
    # building docids.txt
    docids_file = open('docids.txt','w')

    # building term_count_doc.txt
    term_count_doc_file = open("term_count_doc.txt", 'w') 

    # Retrieve the names of all files to be indexed in folder ./ap89_collection_small of the current directory
    for dir_path, dir_names, file_names in os.walk("CS172_PS2\data/ap89_collection_small"):
        allfiles = [os.path.join(dir_path, filename).replace("\\", "/") for filename in file_names if (filename != "readme" and filename != ".DS_Store")]

    # Retrieve the names of all files to be indexed in folder ./ap89_collection_small of the current directory
    for dir_path, dir_names, file_names in os.walk("ap89_collection_small"):
        allfiles = [os.path.join(dir_path, filename).replace("\\", "/") for filename in file_names if (filename != "readme" and filename != ".DS_Store")]

    for file in allfiles:
        with open(file, 'r', encoding='ISO-8859-1') as f:
            filedata = f.read()
            result = re.findall(doc_regex, filedata)  # Match the <DOC> tags and fetch documents

            for document in result:
                # Retrieve contents of DOCNO tag
                docno = re.findall(docno_regex, document)[0].replace("<DOCNO>", "").replace("</DOCNO>", "").strip()
                docid =  int(str(re.findall('(?<=89).*',docno)[0]).replace('-',''))
                # Retrieve contents of TEXT tag
                text = "".join(re.findall(text_regex, document))\
                        .replace("<TEXT>", "").replace("</TEXT>", "")\
                        .replace("\n", " ")

                # step 1 - lower-case words, remove punctuation, remove stop-words, etc. 
                # Convert the text to lower case words
                text = text.lower()
                # step 2 - create tokens 
                text = remove_punc(text)
                text = text.rsplit()
                text = remove_stopword(text)
                #stemming
                text = stemming(text)
                # Write term_count_doc
                term_count_doc_file.write(docno+"\t"+str(len(text))+"\n")
                # step 3 - build index
                for idx,item in enumerate(text):
                    check = text[idx]
                    if item in check:
                        if item not in storing:
                            storing[item] = []
                        if item in storing:
                            if len(storing[item]) == 0:
                                termid = termid + 1
                                storing[item].append(tuple((termid,docid,idx+1)))
                            else:
                                tmp = storing[item][0][0]
                                storing[item].append(tuple((tmp,docid,idx+1)))
            # building docids.txt
                docids_file.write(str(docid)+'\t'+docno+'\n')
    docids_file.close()
    term_count_doc_file.close()

def term_ids():
    with open("termids.txt", 'w') as termids_file:
        for i in storing:
            termids_file.write(str(storing[i][0][0])+'\t'+i)
            termids_file.write('\n')
    termids_file.close()

def term_index():
    with open("term_index.txt", 'w') as term_index_file:
        for i in storing:
            term_index_file.write(str(storing[i][0][0]))
            for j in range(len(storing[i])):
                term_index_file.write('\t'+str(storing[i][j][1])+':'+str(storing[i][j][2]))
            term_index_file.write('\n')
    term_index_file.close()

def term_info():
    tmp2=[]
    count = 0
    tmp_doc = 0
    # building term_info.txt
    with open("term_info.txt", 'w') as term_info_file:
        with open("term_index.txt", 'r') as term_index:
            tmp = term_index.readlines()
            for idx, i in enumerate(tmp):
                tmp1 = i.replace('\n','').split('\t')
                for j in range(len(tmp1)-1):
                    tmp2.append(re.findall('\w+',tmp1[j+1])[0])
                for doc in tmp2:
                    if doc != tmp_doc:
                        count = count + 1
                    tmp_doc = doc
                #termid = str(tmp1[0])
                #The offset in bytes to the beginning of the line containing the inverted list
                #for that term in term_index.txt. If you jump to this location and read one line,
                #the first symbol you see should be the TERMID. = str(idx+1)
                #The total number of occurrences of the term in the entire corpus: str(len(tmp1)-1)
                term_info_file.write(str(tmp1[0])+"\t"+str(idx+1)+"\t"+str(len(tmp1)-1)+"\t"+str(count)+"\n")
                count = 0
                tmp_doc = 0
                tmp2=[]
    term_index.close()
    term_info_file.close()
if __name__ == "__main__":
    ass1()
    term_ids()
    term_index()
    term_info()