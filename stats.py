def get_num_words(text):
    words = text.split()
    return len(words)   
  
def get_char_count_table(text):
    char_table = {}
    for char in text.lower():
      if char in char_table:
          char_table[char] += 1
      else:
          char_table[char] = 1
    return char_table

def get_num(row):
  return row["num"]
 
def sort_char_table(char_table):
  list_of_rows = []
  for k,v in char_table.items():
    row = {"char": k, "num": v}
    list_of_rows.append(row)
  
  list_of_rows.sort(key=get_num, reverse=True)
  return list_of_rows