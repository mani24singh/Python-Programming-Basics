# Dictionary and Sets

## Dictionary : 
- Dictionary is a collection of key-value pairs.
- Properties of Python Dictionaries :
   - It is unordered
   - It is mutable
   - It is indexed
   - It cannot contain duplicate keys
- Dictionary Methods :
   1. items() : returns a list of (key,value) tuple.
   2. keys() : returns a list containing dictionary’s keys.
   3. update() : updates the dictionary with supplied key-value pairs.
   4. get() : returns the value of the specified keys. \
More methods are available on docs.python.org

## Sets in Python :
- Set is a collection of non-repetitive elements.
>S= Set()          # No repetition allowed! \
S.add(1) \
S.add(2) \
returns Set = {1,2}
- If you are a programming beginner without much knowledge of mathematical operations on sets, you can simply look at sets in python as data types containing unique values.
- Properties of Sets :
   - Sets are unordered # Elements order doesn’t matter
   - Sets are unindexed # Cannot access elements by index
   - There is no way to change items in sets
   - Sets cannot contain duplicate values
- Operations on Sets :
   1. Len() : Returns the length of the set
   2. remove() : Updates the set S and removes given element from Set
   3. pop() : Removes an arbitrary element from the set and returns the element removed.
   4. clear() : Empties the set 
   5. union({e1, e2}) : Returns a new set with all items from both sets. 
   6. intersection({e1, e2}) : Returns a set which contains only items in both sets. 
