





import random
import string
import time
import requests
import keyauth
from colored import fg, attr

def generate_random_letters(n: int) -> str:
        """Generate a random string of letters with the given length."""
        letters = string.ascii_uppercase
        return ''.join(random.choice(letters) for _ in range(n))

def insert_random_letters(link: str, n: int) -> str:
        """Insert n random letters into the given link at the specified position."""
        characters_to_replace = 'XXXXXXXXXXXXXXXXXXX'
        if characters_to_replace not in link:
              raise ValueError(f"The string '{characters_to_replace}' is not present in the link.")
        start = link.find(characters_to_replace)
        end = start + len(characters_to_replace)
        random_letters = generate_random_letters(n)
        return link[:start] + random_letters + link[end:]

def check_link(link: str) -> bool:
  """Check if the given link is valid."""
  try:
          response = requests.get(link)
          if response.status_code == 200 and "Congratulations!" in response.text:
                  return True
          else: 
                  return False
  except:
          return False

if __name__ == '__main__':
      link = 'https://discord.com/gifts/XXXXXXXXXXXXXXXXXXX'
      n = 19  # number of random letters to generate
      try:
          new_link = insert_random_letters(link, n)
      except ValueError as e:
          print(e)
      else:
        unique_links = set()
        while len(unique_links) < 1000:
          new_link = insert_random_letters(link, n)
          unique_links.add(new_link)
        for link in unique_links:
          
          if check_link(link):
            print(fg(135) + link + attr(0))
            print(fg(42) + "Valid" + attr(0))
            exit()
          else:
            print(fg(13) + link + attr(0))
            print(fg(1) + "Not Valid" + attr(0))
