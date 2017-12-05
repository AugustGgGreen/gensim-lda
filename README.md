# gensim-lda
(1)lda.py use gensim train our data and use in Recommendation system
    input file: data/test.txt data/cropus.mm data/corpus.mm.index data/dictionary
    output file: data/corpus.mm data/corpus.mm.index data/dictionary
                model/video.lda.model model/video.lda.model.expElogbeta.npy
                model/video.lda.model.id2word
                model/video.lda.model.state
                model/video.lda.model.state.sstats.npy

                logs/video.lda.log
(2)text2libsvm.py change the input file from text format to libsvm format
    input_file:
    output_file:

(3)check_cropus.py use to check input file format of the Microsoft LightLDA
    input file:
    output file:


(4)