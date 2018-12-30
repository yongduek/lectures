# Data Science 101

1. Python Data Science Handbook
1. Introduction to Machine Learning with Python
1. `https://scikit-learn.org` & `scipy.org`
1. Think Stats
1. Think Bayes



## Small Projects
1. editor / IDE for python
    - `https://www.datacamp.com/community/tutorials/data-science-python-ide`
    
1. short intro to `python` : Skip this part since it can be done during the exploration!
    - data containers: list, dict, set
    - conditional expression: if, else, elif
    - tedious loop: for, while
    - variable
    - print
    - class and member function

1. Draw several lines, triangles, circles in a `numpy` WHC array, and save it to a `png` or `jpg` file.
    - what is `numpy`?
        - short tutorial.
    - Read a `jpg` image file into `numpy.array` and display it with `matplotlib.pyplot`
    - Do the same thing with `PIL`
    - Use a `ttf` font file to make images of characters with `PIL`.
        - Do research on the structure of ttf font file.
        
    - Line/tirangle/polygon drawing in a digital image.
        - direct programming
        - PIL function
    
    - Computational Linear Algebra with `numpy`
        - scalar, vector, matrix
        - two operations: addition, multiplication
       
    - image processing:
        - pixel-based operation: brightness control, color quantization
        - window-based operation: convolution
        - binarization, thresholding, edge filter
        - histogram: another counting (as done with text)
        
1. `pandas` dataframe. 
    - what is `pandas`?
        - a tutorial on using `pandas`
        - `https://towardsdatascience.com/be-a-more-efficient-data-scientist-today-master-pandas-with-this-guide-ea362d27386`
    - Read in `IRIS` csv file. 
    - Do explatory data analysis (visual inspection) with scatter plots
    - Choose two species, do classification with scikit-learn.
    - Read `azeleas.csv`. Report statistics of the 'codes' in the file.

1. Playing with text data: 
    - string data and encoding:
        - `https://mariapilot.noblogs.org/files/2017/05/MODERN-PYTHON-COOKBOOK.pdf`
    - Given a text file in `.txt` format, count the number of alphabets, letters, words, and sentences. (Korean/English)
    - first try to make a small txt file using a text file editor
        - jupyter notebook, pycharm, vscode, sublime, etc. 
    - Then a large file from a book or a new article.
        - Gutenberg Project
    - make an automatically generated statistics report & publish it on `twitter` or `facebook`.
    - Separate a korean character into its Cho/Jung/Jong and do counting
    
    - English documents
        - Get a report/paper by Change DU, apply the analysis.
        - Get a report/paper by Fremery, W., apply the analysis.
        - Extract words peculiar to Chang's or Fremery's based on the above analysis
        - use `spacy` for token analyser, use them for the analysis.
    - Korean documents
        - Choose two authors and obtain their documents, apply the same procedure, and report.
        - Apply Token Analyser (형태소분석기) such as `https://github.com/kakao/khaiii`, '코코마', or 'twitter', and do the same analysis.
        
    - Reading pdf documents with python
        - 'pypdf2'

1. Do research on 'base64' encoding, provide an example.
    - convert a base64 encoded image into a numpy array.
    - generate extra column in the dataframe and put azelieas numpy char arrays.
    - find any mismatch between the code and the image. Suggest how, and report the result. Do visual inspection otherwise.

1. extract '가' and '나' to two df files.
    - Find average image, and std image
    - Find 1D representation (distance) of the images w.r.t the average image. You need to define metric between two images.
    - Display several of the largest distance images and explore.
    - develop a classifier (tree-based, SVC), report its performance.
    - accuracy vs recall, F-score
    - apply `t-SNE` analysis and display it.

1. network
    - `https://www.datacamp.com/community/tutorials/social-network-analysis-python`
    - math: `https://www.youtube.com/playlist?list=PLPaDsoN2Ogtac0iF9S0I8Mmt-eW7VlJll`
    
1. TODO: Regression Problem
    - use a `kaggle.com` data set & notepad
    
    
