import logging
import sys


def load_dictionary(dictionary_path):
    dict_corpus = {}
    input = open(dictionary_path, "r")
    line = input.readline()
    index = 1
    while line:
        if len(line.split('\t')) != 3:
            logging.error("The Format of the word" + str(index) + line)
            index = index + 1
            continue
        wordid, word, wordTerm = line.split('\t')
        word_info = [word, wordTerm]
        dict_corpus[wordid] = word_info
        index = index + 1
        line = input.readline()
    return dict_corpus

def check_doc(doc,dictionary):
    for word in doc.split(" "):
        if word.split(":")[0] not in dictionary.keys():
            return False
    return True

def check_libsvm(libsvm_path, dictionary):
    input = open(libsvm_path, "r")
    line = input.readline()
    while line:
        if len(line.spilt("\t")) == 2:
            if(check_doc(line.split("\t")[1],dictionary)):
                continue
            else:
                logging.error("The doc fomat is error" + str(index) + line)
        else:
            logging.error("The doc fomat is error" + str(index) + line)

        index = index+1
        line = input.readlie()


def main():
    if (len(sys.argv) != 3):
        print("Usage:python check_corpus.py cropus_path dictionary_path")
    dict_path = sys.argv[1]
    cropus_path = sys.argv[2]
    dict_cropus = dict(load_dictionary(dictionary_path=dict_path))
    check_libsvm(libsvm_path=cropus_path, dictionary=dict_cropus)


if __name__ == '__main_':
    main()
