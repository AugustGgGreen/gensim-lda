import logging
import sys
import codecs

logger = logging.getLogger("lightlda-check-log")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("../logs/LightLDA/check.log")
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

def load_dictionary(dictionary_path):
    dict_corpus = {}
    input = codecs.open(dictionary_path, "r","utf-8")
    line = input.readline()
    index = 1
    while line:
        if len(line.split('\t')) != 3:
            logger.debug("The Format of the word is error" + str(index)+ "    "+ line)
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
    input = codecs.open(libsvm_path, "r", "utf-8")
    line = input.readline()
    index = 1
    while line:
        line=line.strip()
        logger.info("Check the doc:"+ line)
        if len(line.split("\t")) == 2:
            words = line.split("\t")[1]
            for word in words.split(' '):
                if(check_doc(word.split(":")[0],dictionary)):
                    continue
                else:
                    logger.debug("The doc format is error:" + str(index) + "    "+ line)
                    print(index)
        else:
            logger.debug("The doc format is error:" + str(index) + "    " + line)
            print(index)
        index = index+1
        line = input.readline()


def main():
    if len(sys.argv)!=1:
        print("Usage:python check_corpus.py <cropus_path> <dictionary_path>")
        exit(-1)
    dict_path = "../data/LightLDA/pp"
    #sys.argv[1]
    cropus_path = "../data/LightLDA/kk.libsvm"
    #sys.argv[2]
    dict_cropus = dict(load_dictionary(dictionary_path=dict_path))
    check_libsvm(libsvm_path=cropus_path, dictionary=dict_cropus)


if __name__ == '__main__':
    main()
