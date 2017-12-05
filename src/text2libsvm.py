#!/usr/bin python
# -*- coding:utf-8 -*-
import codecs
import logging
import sys
logger = logging.getLogger("LightLDA_Text2lib_LOG")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("../logs/LightLDA/text2libsvm.log")
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

def load_file(input_file,libsvm_file,dict_file):
    input = codecs.open(input_file, "r", "utf-8")
    line = input.readline()
    output_libsvm = codecs.open(libsvm_file,"w","utf-8")
    output_dict = codecs.open(dict_file,'w', "utf-8")
    index = 1
    word_dict={}
    while line:
        doc={}
        line=line.strip()
        logger.info("Deal the doc:" + line)
        words = line.split(' ')
        for word in words:
            if word not in word_dict.keys():
                wordid = len(word_dict.keys()) + 1
                word_dict[word]=[1,wordid]
                #logger.info("Add word :" + word + ":" + str(word_dict[word][1]))
                #print("Add word :" + word + ":" + str(word_dict[word][1]))
            else:
                word_dict[word][0] += 1
            if word not in doc.keys():
                logger.info(str(word)+str(word_dict[word][1]))
                doc[word]=[1,word_dict[word][1]]
            else:
                doc[word][0] += 1
        word_list=[]
        for word in doc:
            word_list.append(str(doc[word][1]) + ":" + str(doc[word][0]))
        output_libsvm.write(" ".join(word_list)+'\n')
        logger.info("the libsvm format of the doc" + " ".join(word_list))
        for word in word_dict:
            output_dict.write(str(word_dict[word][1])+'\t' + word + '\t' + str(word_dict[word][0]) + '\n')
        index = index + 1
        line = input.readline()

def main():
    if len(sys.argv)!=1:
        print("Usage: python text2libsvm.py input_path libsvm_path dict_path")
        exit(-1)
    input_path= "../data/test.txt"
    #sys.argv[1]
    libsvm_path="../data/LightLDA/video.libsvm"
    #sys.argv[2]
    dict_path="../data/LightLDA/video.word_id.dict"
    #sys.argv[3]
    load_file(input_path,libsvm_path,dict_path)
    logger.info("The format from text to libsvm!")

if __name__=='__main__':
    main()
