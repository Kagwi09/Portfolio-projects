from bs4 import BeautifulSoup
with open('C:\\Users\\MWANGI\\Downloads\\home.html', 'r') as html_file:

    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card')  # add an _ to class because 'class' is a defined object in python
    for i in course_cards:
        course_name = i.h5.text  # adding h5 as an argument filters for h5 titles only
        course_price = i.a.text.split()[-1]  # splits the text into lists using spaces
        # and picks the last list containing the price
        print(f'{course_name}  {course_price}')
