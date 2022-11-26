# Amazon Kindle epub to pdf converter V1
I made this program to convert the epub file of Barron's AP Physics 1 to a pdf file. Still, it is applicable for any epub files on Amazon Kindle.

### Precondition
- You should purchase the Kindle Book of the document you want to convert on Amazon.
- ChromeDriver needs to be installed with a version higher than ChromeDriver 99.

### Usage
- Insert all of the data listed in ```config.py```.
- Run ```main.py```.
- All of the pages will be stored in the ```res``` folder.

### Notes
- Page numbers might be different with the ```.epub``` file.
- Processing time depends on the length of the book.
- ```KINDLE_BOOK_LINK``` written in ```config.py``` should be in a form of ```https://read.amazon.com/?asin=[]&ref_=[]&language=en-US```. It shouldn't be ```https://read.amazon.com/kindle-library```.
