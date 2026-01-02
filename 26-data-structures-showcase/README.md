# 📚 Data Structures Showcase - Complete Guide

A comprehensive, interactive exploration of all Python built-in data structures with practical examples, visual representations, and real-world use cases.

## 🎯 Project Overview

This project provides a complete, hands-on learning experience for understanding Python's data structures. Through interactive demonstrations and practical examples, you'll master when and how to use each structure effectively.

## 📋 Complete Data Structures Coverage

### 🔵 Core Built-in Types

#### 1. **Lists** 📋 - Dynamic Arrays
**What**: Ordered, mutable collection that can hold any type of data.

**When to Use**:
- When you need an ordered collection
- When items need to be modified frequently
- When duplicates are allowed
- When you need fast access by index

**Visual Representation**:
```
Lists: [item1, item2, item3, ...]
Index:    0      1      2

Example: ['apple', 'banana', 'cherry']
         [   0   ,    1    ,    2    ]
```

**Common Operations & Time Complexity**:
```python
# Creation
fruits = ['apple', 'banana', 'cherry']
numbers = list(range(10))

# Access - O(1)
first = fruits[0]           # 'apple'
last = fruits[-1]           # 'cherry'

# Modification - O(1) at end, O(n) at beginning
fruits.append('date')       # O(1) - Add to end
fruits.insert(0, 'apricot') # O(n) - Add to beginning
fruits[1] = 'blueberry'     # O(1) - Modify by index

# Deletion - O(1) at end, O(n) elsewhere
fruits.pop()                # O(1) - Remove from end
fruits.pop(0)               # O(n) - Remove from beginning
fruits.remove('banana')     # O(n) - Remove by value

# Searching - O(n)
if 'apple' in fruits:       # O(n) - Linear search
    print("Found!")

# Slicing - O(k) where k is slice size
subset = fruits[1:3]        # ['banana', 'cherry']
reversed_list = fruits[::-1]  # Reverse the list

# Sorting - O(n log n)
fruits.sort()               # Sort in-place
sorted_fruits = sorted(fruits)  # Return new sorted list

# List Comprehension - O(n)
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

**Real-World Use Cases**:
- Shopping cart items
- Todo list tasks
- Chat message history
- Search results
- Navigation history

---

#### 2. **Tuples** 📦 - Immutable Sequences
**What**: Ordered, immutable collection (cannot be changed after creation).

**When to Use**:
- When data shouldn't change (RGB colors, coordinates)
- As dictionary keys (since immutable)
- For function return of multiple values
- When you want memory efficiency

**Visual Representation**:
```
Tuples: (item1, item2, item3)
         Immutable - Cannot modify after creation

Point: (x=10, y=20)
RGB:   (r=255, g=128, b=0)
```

**Tuples vs Lists Comparison**:
```python
# Lists - Mutable
list_data = [1, 2, 3]
list_data[0] = 10          # ✅ Allowed
list_data.append(4)        # ✅ Allowed

# Tuples - Immutable
tuple_data = (1, 2, 3)
tuple_data[0] = 10         # ❌ TypeError!
tuple_data.append(4)       # ❌ AttributeError!

# Unpacking
x, y, z = (10, 20, 30)     # Multiple assignment

# As dictionary keys
locations = {
    (0, 0): "Origin",
    (10, 20): "Point A"    # Tuples can be keys
}

# Memory comparison
import sys
list_mem = sys.getsizeof([1,2,3,4,5])   # ~120 bytes
tuple_mem = sys.getsizeof((1,2,3,4,5))  # ~80 bytes
```

**Real-World Use Cases**:
- Coordinates: `(latitude, longitude)`
- RGB colors: `(255, 0, 128)`
- Database records
- Function returns: `return (success, result, error)`
- Immutable configuration

---

#### 3. **Sets** 🎯 - Unique Unordered Collections
**What**: Unordered collection of unique elements (no duplicates).

**When to Use**:
- Remove duplicates from a list
- Fast membership testing (`in` operator)
- Mathematical set operations
- Finding unique items

**Visual Representation**:
```
Sets: {item1, item2, item3}
      ↓
   No Order, No Duplicates

Input:  [1, 2, 2, 3, 3, 3, 4]
Output: {1, 2, 3, 4}
```

**Set Operations - Visual**:
```
Set A = {1, 2, 3, 4, 5}
Set B = {4, 5, 6, 7, 8}

Union (A | B):
{1, 2, 3, 4, 5, 6, 7, 8}  # All elements

Intersection (A & B):
{4, 5}  # Common elements only

Difference (A - B):
{1, 2, 3}  # In A but not in B

Symmetric Difference (A ^ B):
{1, 2, 3, 6, 7, 8}  # In A or B, but not both
```

**Operations & Time Complexity**:
```python
# Creation
unique_nums = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3])  # {1, 2, 3}

# Add/Remove - O(1) average
unique_nums.add(6)           # O(1)
unique_nums.remove(2)        # O(1)
unique_nums.discard(10)      # O(1) - No error if not found

# Membership - O(1) average
if 3 in unique_nums:         # O(1) - Very fast!
    print("Found!")

# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A | B    # Union: {1, 2, 3, 4, 5, 6}
A & B    # Intersection: {3, 4}
A - B    # Difference: {1, 2}
A ^ B    # Symmetric diff: {1, 2, 5, 6}

# Practical example: Remove duplicates
duplicates = [1, 2, 2, 3, 3, 3, 4, 4]
unique = list(set(duplicates))  # [1, 2, 3, 4]
```

**Real-World Use Cases**:
- Remove duplicate emails/usernames
- Tags/categories (unique labels)
- Permissions/roles checking
- Finding unique words in text
- Comparing lists for differences

---

#### 4. **Frozensets** ❄️ - Immutable Sets
**What**: Immutable version of sets (cannot be modified after creation).

**When to Use**:
- As dictionary keys
- As elements of other sets
- When immutability is required

{% raw %}
```python
# Regular set cannot be a dict key
# permissions = {{'read', 'write'}: 'Editor'}  # ❌ Error!

# Frozenset can be a dict key
permissions = {
    frozenset(['read', 'write']): 'Editor',
    frozenset(['read']): 'Viewer',
    frozenset(['read', 'write', 'delete']): 'Admin'
}

# Frozenset in a set
set_of_sets = {
    frozenset([1, 2]),
    frozenset([3, 4]),
    frozenset([5, 6])
}
```
{% endraw %}

---

#### 5. **Dictionaries** 🗂️ - Key-Value Mappings
**What**: Unordered collection of key-value pairs (hash tables).

**When to Use**:
- Store data with meaningful labels
- Fast lookups by key
- Counting/grouping items
- Configuration settings

**Visual Representation**:
```
Dictionary: {key1: value1, key2: value2, ...}

person = {
    'name': 'Alice',     ←─ Key: Value
    'age': 30,           ←─ Key: Value
    'city': 'NYC'        ←─ Key: Value
}

Access: person['name']  → 'Alice'  (O(1) lookup!)
```

**Operations & Time Complexity**:
```python
# Creation
person = {'name': 'Alice', 'age': 30}
scores = dict(math=95, science=88)

# Access - O(1)
name = person['name']              # 'Alice'
age = person.get('age', 0)         # 30 (with default)
city = person.get('city', 'Unknown')  # 'Unknown'

# Modification - O(1)
person['age'] = 31                 # Update
person['job'] = 'Engineer'         # Add new key

# Deletion - O(1)
del person['age']                  # Remove key
popped = person.pop('name', None)  # Remove and return

# Iteration
for key in person:                 # Iterate keys
    print(key, person[key])

for key, value in person.items():  # Iterate pairs
    print(f"{key}: {value}")

# Dictionary Comprehension
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Nested dictionaries
students = {
    'Alice': {'age': 20, 'gpa': 3.8},
    'Bob': {'age': 21, 'gpa': 3.5}
}
alice_gpa = students['Alice']['gpa']  # 3.8
```

**Real-World Use Cases**:
- User profiles/settings
- Database records
- JSON data parsing
- Counting word frequency
- Caching/memoization

---

### 🔶 Collections Module - Advanced Structures

#### 6. **Counter** 🔢 - Automatic Counting
**What**: Dict subclass for counting hashable objects.

**Visual Representation**:
```
Input:  ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
         ↓
Counter: {'apple': 3, 'banana': 2, 'cherry': 1}
         ↓
Most Common: [('apple', 3), ('banana', 2), ('cherry', 1)]
```

**Practical Examples**:
```python
from collections import Counter

# Word frequency
text = "the quick brown fox jumps over the lazy dog"
word_count = Counter(text.split())
# Counter({'the': 2, 'quick': 1, 'brown': 1, ...})

# Most common
print(word_count.most_common(3))
# [('the', 2), ('quick', 1), ('brown', 1)]

# Letter frequency
letters = Counter("mississippi")
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Counter arithmetic
c1 = Counter(['a', 'b', 'c', 'a'])  # {'a': 2, 'b': 1, 'c': 1}
c2 = Counter(['a', 'b', 'd'])       # {'a': 1, 'b': 1, 'd': 1}

c1 + c2  # Add: {'a': 3, 'b': 2, 'c': 1, 'd': 1}
c1 - c2  # Subtract: {'a': 1, 'c': 1}
c1 & c2  # Intersection: {'a': 1, 'b': 1}
c1 | c2  # Union: {'a': 2, 'b': 1, 'c': 1, 'd': 1}
```

**Use Cases**:
- Vote counting
- Word/letter frequency analysis
- Inventory tracking
- Finding duplicates

---

#### 7. **DefaultDict** 🏗️ - Dicts with Default Values
**What**: Dict that never raises KeyError, provides default values.

**Problem it Solves**:
```python
# Regular dict - need to check key exists
students = {}
if 'Math' not in students:
    students['Math'] = []
students['Math'].append('Alice')  # Verbose!

# DefaultDict - automatic default value
from collections import defaultdict
students = defaultdict(list)
students['Math'].append('Alice')  # Just works! ✅
```

**Common Patterns**:
```python
from collections import defaultdict

# 1. Grouping items
students_by_grade = defaultdict(list)
students_by_grade['A'].append('Alice')
students_by_grade['A'].append('Bob')
students_by_grade['B'].append('Charlie')
# {'A': ['Alice', 'Bob'], 'B': ['Charlie']}

# 2. Counting (alternative to Counter)
word_count = defaultdict(int)
for word in text.split():
    word_count[word] += 1

# 3. Nested defaultdicts
tree = lambda: defaultdict(tree)
users = tree()
users['Alice']['age'] = 30
users['Alice']['city'] = 'NYC'
```

---

#### 8. **Deque** 🔄 - Double-Ended Queue
**What**: List-like container with fast operations on both ends.

**Visual Representation**:
```
Regular List:
    append(x)           →  [1, 2, 3, 4, 5]  ← Fast O(1)
    insert(0, x)  Slow  ←  [x, 1, 2, 3, 4]    O(n)

Deque (Double-Ended Queue):
    append(x)      →  [1, 2, 3, 4, 5]  ← Fast O(1)
    appendleft(x)  ←  [x, 1, 2, 3, 4]  ← Fast O(1)
    pop()          →  [1, 2, 3, 4]     ← Fast O(1)
    popleft()      ←  [2, 3, 4, 5]     ← Fast O(1)
```

**Operations Comparison**:
```python
from collections import deque

# List - slow at beginning
lst = [1, 2, 3, 4, 5]
lst.insert(0, 0)  # O(n) - shifts all elements
lst.pop(0)        # O(n) - shifts all elements

# Deque - fast everywhere
dq = deque([1, 2, 3, 4, 5])
dq.appendleft(0)  # O(1) - very fast!
dq.popleft()      # O(1) - very fast!

# Rotation
dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)      # [4, 5, 1, 2, 3]
dq.rotate(-2)     # [1, 2, 3, 4, 5]

# Max length (circular buffer)
recent = deque(maxlen=3)
for i in range(1, 10):
    recent.append(i)
    print(recent)
# deque([1], maxlen=3)
# deque([1, 2], maxlen=3)
# deque([1, 2, 3], maxlen=3)
# deque([2, 3, 4], maxlen=3)  ← 1 removed!
# ...
# deque([7, 8, 9], maxlen=3)
```

**Use Cases**:
- Queue (FIFO): `appendleft()` and `pop()`
- Stack (LIFO): `append()` and `pop()`
- Recent history (maxlen)
- Breadth-first search (BFS)
- Sliding window algorithms

---

#### 9. **NamedTuple** 🏷️ - Tuples with Named Fields
**What**: Tuple with named fields for better readability.

**Before vs After**:
```python
# Regular tuple - hard to read
point = (10, 20)
x = point[0]  # What is this?
y = point[1]  # What is this?

# NamedTuple - self-documenting
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
point = Point(10, 20)
print(point.x)  # Clear!
print(point.y)  # Clear!
```

**Advantages**:
```python
from collections import namedtuple

# Define structure
Person = namedtuple('Person', ['name', 'age', 'city'])
Employee = namedtuple('Employee', 'id name department salary')

# Create instances
alice = Person('Alice', 30, 'NYC')
bob = Employee(101, 'Bob', 'Engineering', 95000)

# Access by name (readable)
print(alice.name)  # 'Alice'
print(bob.salary)  # 95000

# Access by index (still works)
print(alice[0])    # 'Alice'

# Convert to dict
print(alice._asdict())
# {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# Replace values (returns new tuple)
older_alice = alice._replace(age=31)

# Immutable!
# alice.age = 31  # ❌ AttributeError
```

**Use Cases**:
- CSV/database records
- Configuration objects
- Function return multiple values
- Lightweight data classes

---

## 📊 Complete Comparison Table

```
┌─────────────────┬──────────┬─────────┬──────────┬───────────┬─────────────┬──────────────┐
│ Data Structure  │ Ordered  │ Mutable │ Indexed  │ Unique    │ Hashable*   │ Access Time  │
├─────────────────┼──────────┼─────────┼──────────┼───────────┼─────────────┼──────────────┤
│ List            │    ✅    │   ✅    │    ✅    │    ❌     │     ❌      │     O(1)     │
│ Tuple           │    ✅    │   ❌    │    ✅    │    ❌     │     ✅      │     O(1)     │
│ Set             │    ❌    │   ✅    │    ❌    │    ✅     │     ❌      │     O(1)     │
│ Frozenset       │    ❌    │   ❌    │    ❌    │    ✅     │     ✅      │     O(1)     │
│ Dict            │  ✅(3.7+)│   ✅    │ By Key   │ Keys: ✅  │     ❌      │     O(1)     │
│ Counter         │  ✅(3.7+)│   ✅    │ By Key   │ Keys: ✅  │     ❌      │     O(1)     │
│ DefaultDict     │  ✅(3.7+)│   ✅    │ By Key   │ Keys: ✅  │     ❌      │     O(1)     │
│ OrderedDict     │    ✅    │   ✅    │ By Key   │ Keys: ✅  │     ❌      │     O(1)     │
│ Deque           │    ✅    │   ✅    │    ✅    │    ❌     │     ❌      │ O(1) ends    │
│ NamedTuple      │    ✅    │   ❌    │    ✅    │    ❌     │     ✅      │     O(1)     │
└─────────────────┴──────────┴─────────┴──────────┴───────────┴─────────────┴──────────────┘

* Hashable = Can be used as dict key or set element
```

## 🎯 Decision Tree: Which Data Structure to Use?

```
Do you need key-value pairs?
│
├─YES → Use Dictionary (or Counter/DefaultDict)
│       │
│       ├─Need counting? → Counter
│       ├─Need default values? → DefaultDict
│       └─Need specific order? → OrderedDict
│
└─NO → Do you need unique elements?
       │
       ├─YES → Use Set (or Frozenset)
       │       │
       │       └─Need immutable? → Frozenset
       │
       └─NO → Do you need to modify elements?
              │
              ├─YES → Use List (or Deque)
              │       │
              │       ├─Fast operations on both ends? → Deque
              │       └─Regular operations? → List
              │
              └─NO → Use Tuple (or NamedTuple)
                     │
                     └─Need named fields? → NamedTuple
```

## ⚡ Performance Cheat Sheet

### Time Complexity Comparison

```python
Operation            List    Tuple   Set     Dict    Deque
─────────────────────────────────────────────────────────
Access by index      O(1)    O(1)     -       -      O(n)
Access by key         -       -       -      O(1)     -
Search              O(n)    O(n)    O(1)    O(1)    O(n)
Insert at end       O(1)     -      O(1)    O(1)    O(1)
Insert at start     O(n)     -      O(1)    O(1)    O(1)
Delete              O(n)     -      O(1)    O(1)    O(1)
```

### Space Complexity

```python
import sys

# Memory usage (approximate, in bytes)
list_obj = [1, 2, 3, 4, 5]     # ~120 bytes
tuple_obj = (1, 2, 3, 4, 5)    # ~80 bytes
set_obj = {1, 2, 3, 4, 5}      # ~224 bytes
dict_obj = {1:'a', 2:'b'}      # ~240 bytes
```

## 🏆 Common Interview Questions

### Q1: Remove duplicates from a list
```python
# Method 1: Using set (loses order)
lst = [1, 2, 2, 3, 3, 4]
unique = list(set(lst))  # [1, 2, 3, 4]

# Method 2: Preserve order
unique = []
seen = set()
for item in lst:
    if item not in seen:
        unique.append(item)
        seen.add(item)
```

### Q2: Count word frequency
```python
from collections import Counter

text = "the quick brown fox jumps over the lazy dog"
Counter(text.split()).most_common(5)
```

### Q3: Find common elements in two lists
```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = list(set(list1) & set(list2))  # [4, 5]
```

## 🚀 How to Run

```bash
cd 26-data-structures-showcase
python main.py
```

## 📖 Further Learning

- [Python Data Structures (Official Docs)](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Collections Module](https://docs.python.org/3/library/collections.html)
- [W3Schools - Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)
- [Real Python - Lists vs Tuples](https://realpython.com/python-lists-tuples/)
- [Python Sets Tutorial](https://www.w3schools.com/python/python_sets.asp)

## 🎓 Key Takeaways

1. **Lists** = Mutable, ordered, allow duplicates → Shopping cart
2. **Tuples** = Immutable, ordered → Coordinates, database records
3. **Sets** = Unique elements, fast lookup → Remove duplicates
4. **Dicts** = Key-value pairs, fast access → User profiles
5. **Counter** = Automatic counting → Word frequency
6. **DefaultDict** = No KeyError → Grouping data
7. **Deque** = Fast on both ends → Queue, recent history
8. **NamedTuple** = Readable tuples → CSV records

---

**Difficulty**: Beginner  
**Time**: 1-2 hours  
**Prerequisites**: Basic Python syntax

Master these data structures and you'll write more efficient, readable Python code! 🚀
