# NAME - e.g first_paragraph = soup.find('p') / 'div' / 'a'

# ATTRIBUTE - A dictionary of attributes that the tag must have.
    # For example, {'class': 'some-class'} e.g soup.find('h1', {'id': 'main-title'})

# RECURSIVE - A boolean value that determines whether to look for tags within all descendant
    # tags (if True, the default) or only within direct children (if False).

# STRING - Used to search for tags that contain a specific string
    # soup.find('p', string='Second paragraph.')
    # searches for a <p> tag that contains the exact string "Second paragraph."

# ** KWARGS - Additional keyword arguments that can be used to match attributes directly.

# CLASS - e.g soup.find('p', class_='content')
    # searches for a <p> tag with the class attribute content

# If you're finding multiple items, use a for loop to display them and add text method to print them in text form
# e.g print(items.text)

# FIND
    # Finds the first tag that matches the given criteria or 'None' if no match is found.
    # Usage: soup.find_all(name, attrs, recursive, string, limit, **kwargs)

# FIND_ALL
    # Finds all tags that match the given criteria.
    # Usage: soup.find_all(name, attrs, recursive, string, limit, **kwargs)
    # Parameters:
        # limit: Limits the number of results returned.

# FIND_PARENT
    # Finds the immediate parent tag of the current tag that matches the given criteria.
    # Or 'None' if no match is found
    # Usage: soup.find_parent(name, attrs, **kwargs)

# FIND_PARENTS
    # Finds all parent tags of the current tag that match the given criteria or 'None' if no match is found
    # Usage: soup.find_parents(name, attrs, limit, **kwargs)

# FIND_NEXT_SIBLING
    # Finds the next sibling tag of the current tag that matches the given criteria OR 'None' if no match is found
    # Usage: soup.find_next_sibling(name, attrs, **kwargs)

# FIND_NEXT_SIBLINGS
    #  Finds all next sibling tags of the current tag that match the given criteria or an empty list if none is found
    # Usage: soup.find_next_siblings(name, attrs, limit, **kwargs)

# FIND_PREVIOUS_SIBLING
    # Finds the previous sibling tag of the current tag that matches the given criteria or 'None' if no match is found
    # Usage: soup.find_previous_sibling(name, attrs, **kwargs)

# FIND_PREVIOUS SIBLINGS
    # Finds all previous sibling tags of the current tag that match the given criteria or an empty list if none is found
    # Usage: soup.find_previous_siblings(name, attrs, limit, **kwargs)

# FIND_NEXT
    #  Finds the next tag in the document that matches the given criteria,
    #  moving forward in the document tree or 'none' if no match is found
    # Usage: soup.find_next(name, attrs, **kwargs)

# FIND_ALL_NEXT
    # Finds all tags after the current tag that match the given criteria,
    # moving forward in the document tree or an empty list if no match is found
    # Usage: soup.find_all_next(name, attrs, limit, **kwargs)

# FIND_PREVIOUS
    # Finds the previous tag in the document that matches the given criteria,
    # moving backward in the document tree or 'None' if no match is found
    # Usage: soup.find_previous(name, attrs, **kwargs)

# FIND_ALL_PREVIOUS
    # Finds all tags before the current tag that match the given criteria,
    # moving backward in the document tree or an empty list if none is found
    # Usage: soup.find_all_previous(name, attrs, limit, **kwargs)

