import sys
from stats import get_num_words
from stats import get_char_count_table
from stats import sort_char_table

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def print_report(sorted_count, num_words, title):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {title}...")
  print("----------- Word Count ----------")
  print(f'Found {num_words} total words')
  print("----------- Character Count ----------")
  
  for row in sorted_count:
    char = row["char"]
    num = row["num"]
    
    if not char.isalpha():
        continue
      
    print(f"{char}: {num}")
  
  print("============= END ===============")
  
def main():
    book_path = ""
    
    num_args = sys.argv.__len__()
    if num_args == 2:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    
    
    count = get_char_count_table(book_text)
    sorted_count = sort_char_table(count)
    
    # print the report in descending order
    print_report(sorted_count, num_words, book_path)

if __name__ == '__main__':
    main()
