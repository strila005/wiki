import re
import markdown2

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        markdown_content = f.read().decode("utf-8")            # Convert Markdown to HTML
        html_content = markdown2.markdown(markdown_content)
        with open(f'{title}.html', 'w') as html_file:          # Save the HTML content to a file
            html_file.write(html_content)
        with open(f'{title}.html', 'r') as html_file:      # Read and return the HTML content from the file
            return html_file.read()
    except FileNotFoundError:
        return None
