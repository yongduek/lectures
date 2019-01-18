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

1. Network
    - `https://www.datacamp.com/community/tutorials/social-network-analysis-python`
    - math: `https://www.youtube.com/playlist?list=PLPaDsoN2Ogtac0iF9S0I8Mmt-eW7VlJll`
    
1. Data
    - [국립중앙박물관 소장품 이미지 공개 목록](https://www.data.go.kr/dataset/3070607/fileData.do)

1. TODO: Regression Problem
    - use a `kaggle.com` data set & notepad
    
1. References & Books
    - [Python for Social Scientists](https://gawron.sdsu.edu/python_for_ss/)
    - [Python for Social Science](https://gawron.sdsu.edu/python_for_ss/course_core/book_draft/index.html)
        - See 6. Data, 7. Classification of Text, 8. Visualization, 9. Social Netowrks
        - Interesting [Anna Karenina Network Assignment](https://gawron.sdsu.edu/python_for_ss/course_core/book_draft/Social_Networks/anna_karenina_network_assignment.html)
    - [Modern Python Cookbook]()
    - [Learning Python for Social Scientists](https://nealcaren.github.io/python-tutorials/)
        - Personal compilation of a list of python tutorials and annotated analyses    
        - Plenty of useful site links.
    - [Fashion Color Analysis](https://github.com/rosariomgomez/fashion)
        - Application of various image analysis techniques including face detection, color analysis
        - impressive!
    - [Text Analysis with Topic Models for the Humanities and Social Sciences](https://liferay.de.dariah.eu/tatom/)
        - A little bit higher level than rudimentary.
        - Text analysis requires some concepts of mathematics and statistics.
        - Now is the time to learn about Bayesian statistics: [A first course in Bayesian statistical methods](https://www.stat.washington.edu/people/pdhoff/book.php)
    
    - [First Python Notebook](http://www.firstpythonnotebook.org/)
        - This textbook will guide you through an investigation of money in politics using data from the [California Civic Data Coalition](https://www.californiacivicdata.org).
        - California Civic Data Coalition Report: An open-source team of journalists and computer programmers from news organizations across America. [github source](https://github.com/california-civic-data-coalition/first-python-notebook)

    - [INTEG 475: Computational Social Science](http://www.johnmclevey.com/475/) by John McLevey in Uni of Waterloo
        - Another course on computational social science in Python
