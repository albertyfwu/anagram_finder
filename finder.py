from trie import *

class Finder:
  def __init__(self, trie):
    self.trie = trie
    self.results = []

  def find(self, chars):
    self._findSub(self.trie, '', chars)

  def _findSub(self, curr_trie, curr_str, chars):
    # Check if curr_str is a word
    if curr_trie.isWord:
      self.results.append(curr_str)

    # Call _findSub on the children as long as the prefix exists
    done_chars = set()

    for i in range(len(chars)):
      char = chars[i]

      if char in done_chars:
        continue

      done_chars.add(char)

      rest_chars = chars[:i] + chars[i+1:]

      if char == '*':  # wildcard
        for child in curr_trie.children:
          next_trie = curr_trie.children[child]
          self._findSub(next_trie, curr_str + child, rest_chars)
        continue

      if char in curr_trie.children:
        next_trie = curr_trie.children[char]
        self._findSub(next_trie, curr_str + char, rest_chars)

  def printSummary(self):
    # Consolidate by number of letters, and sort within each category
    results_by_num_letters = []
    for i in range(20):
      results_by_num_letters.append([])

    for result in self.results:
      length = len(result)
      results_by_num_letters[length].append(result)

    for i in range(20):
      curr_results = results_by_num_letters[i]
      if len(curr_results) > 0:
        curr_results.sort()

        print '%d letter words:' % i
        print curr_results

def loadWords(filepath):
  trie = Trie(isRoot=True, cacheOn=True)
  trie.importWords(filepath)
  return trie

if __name__ == '__main__':
  print '\nLoading dictionary of words...'
  trie = loadWords('./dictionary.txt')
  print 'Dictionary loaded!'

  while True:
    # prompt user for letters on board
    raw = raw_input("\nPlease enter the letters below (specify wildcard as *):\n")
    search_str = raw.strip(' ,').upper()

    finder = Finder(trie)
    finder.find(search_str)
    finder.printSummary()
