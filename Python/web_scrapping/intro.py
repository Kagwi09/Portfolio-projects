from bs4 import BeautifulSoup
    # from bs4 import BeautifulSoup:
    # This line imports the BeautifulSoup class from the bs4 (BeautifulSoup 4) module.
    # BeautifulSoup is the main class used for parsing HTML and XML documents.
    # It creates a parse tree from the HTML content, which can then be used to navigate
    # the document and extract data.
with open('C:\\Users\\MWANGI\\Downloads\\home.html', 'r') as html_file:
    # This line opens the HTML file located at the specified path in read mode ('r').
    # The with statement is used here for opening the file because it ensures that
    # the file is properly closed after its content has been read,
    # even if an error occurs during the file operation.
    content = html_file.read()
    # This line reads the entire content of the opened HTML file into the variable content.
    # The read() method reads the entire file as a single string.

    soup = BeautifulSoup(content, 'lxml')
    # This line creates a BeautifulSoup object named soup by parsing the content string
    # using the 'lxml' parser.
    # The 'lxml' parser is one of several parsers that BeautifulSoup supports.
    # It is fast and can handle broken HTML better than some other parsers.
    # The BeautifulSoup object represents the document as a nested data structure
    # (parse tree), which you can then use to navigate and manipulate the HTML.

#  print(soup.prettify())
    # The prettify() method formats the HTML content with proper indentation,
    # making it easier to read.
    # This is particularly useful for inspecting the structure of an HTML document.
    tags = soup.find_all('h5')
    for i in tags:
        print(i.text)
