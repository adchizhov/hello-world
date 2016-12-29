#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  fhand = open(filename, 'r')
  all_html = fhand.read()
  pop_year = re.search(r'(in) ([\d]+)', all_html)
  index_for_rank_man= 0
  index_for_rank_girl = 0
  dict_man = {}
  dict_girl = {}
  lst_of_names = []
  names = re.findall(r'>(\w+)<', all_html)
  del names[0]

  for index in range(1, 2998, 3):
    dict_man[names[index]] = names[index_for_rank_man]
    index_for_rank_man += 3
  for index in range(2, 2999, 3):
    dict_girl[names[index]] = names[index_for_rank_girl]
    index_for_rank_girl += 3
  sorted_names_man = sorted(dict_man.keys())
  sorted_names_girl = sorted(dict_girl.keys())
  for name in sorted_names_man:
    lst_of_names.append(name + ' ' + dict_man[name])
  for name in sorted_names_girl:
    lst_of_names.append(name + ' ' + dict_girl[name])
  finished_lst_of_names = [pop_year.group(2)] + sorted (lst_of_names)
  print finished_lst_of_names


  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++


extract_names('baby2002.html')

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
    for filename in args:
      names = extract_names(filename)

      # Make text out of the whole list
      text = '\n'.join(names)

      if summary:
        outf = open(filename + '.summary', 'w')
        outf.write(text + '\n')
        outf.close()
      else:
        print text
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
