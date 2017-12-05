#!usr/bin python
# -*- coding:utf-8 -*-
import logging
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim import corpora
from gensim.corpora.textcorpus import remove_stopwords
from gensim.corpora import MmCorpus, Dictionary
from gensim.models.ldamodel import LdaModel
import sys
import os
import datetime

logging.basicConfig(format='%(asctime)s : %(levelname)s: %(message)s', level=logging.INFO,filename="../logs/video.lda.log")
def file_exist(path):
    return os.path.exists(path)

def preprocess(corpus_text,dict_path,corpus_path):
    if(not file_exist(corpus_text)):
        logging.error("corpus file not exist!")
        exit(-2)
    corpus=corpora.TextCorpus(input=corpus_text,token_filters=[remove_stopwords])
    corpus.dictionary.save_as_text(dict_path)
    MmCorpus.serialize(corpus_path,corpus)

def Train_LDA(model_path,corpus_path,dict_path,num_topics,alpha,eta,iterations):
    dictioary=Dictionary.load_from_text(dict_path)
    corpus = MmCorpus(corpus_path)
    lda=LdaModel(corpus=corpus,id2word=dictioary,num_topics=num_topics,alpha=alpha,iterations=iterations,eta=eta)
    lda.save(model_path)
    for topic in lda.show_topics(num_topics=num_topics,num_words=20,formatted=False):
            print(topic)
def main():
    #if(len(sys.argv) != 4):
    #    print("Usage: python lda.py <corpus_text> <corpus_path>, <dictionary_path> <model_path>")
    #    exit(-1)
    #corpus_text=sys.argv[1]
    #corpus_path=sys.argv[2]
    #dict_path=sys.argv[3]
    #model_path=sys.argv[4]
    corpus_text="../data/test.txt"
    corpus_path="../data/corpus.mm"
    dict_path="../data/dictionary"
    model_path="../model/video.lda.model"
    start = datetime.datetime.now()
    logging.info("Start Time: {}".format(start))
    end1=datetime.datetime.now()
    if(not file_exist(corpus_path) or not file_exist(dict_path)):
        preprocess(corpus_text,dict_path,corpus_path)
        end1 = datetime.datetime.now()
        logging.info("End of preprocess time:{}\n".format(end1))
        logging.info("Preprocess time token {} \n".format(end1 - start))
    Train_LDA(model_path=model_path,corpus_path=corpus_path,dict_path=dict_path,num_topics=400,alpha=0.125,iterations=400,eta=0.01)
    end2 = datetime.datetime.now()
    logging.info("End of Train time:{}\n".format(end2))
    logging.info("Train time token{}\n".format(end2-end1))

if __name__=="__main__":
    main()