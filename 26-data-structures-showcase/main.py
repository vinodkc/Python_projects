"""
📚 PROJECT: Data Structures Showcase
🎯 OBJECTIVE: Comprehensive exploration of all Python built-in data structures
📖 DIFFICULTY: Beginner
🔧 CONCEPTS: Lists, Tuples, Sets, Frozensets, Dictionaries, Collections Module

This project demonstrates all major Python data structures with practical examples
and operations, helping you understand when and how to use each one.
"""

from collections import Counter, defaultdict, deque, namedtuple, OrderedDict, ChainMap

def main():
    """Main function to showcase all Python data structures"""
    
    print("=" * 70)
    print("🐍 PYTHON DATA STRUCTURES SHOWCASE")
    print("=" * 70)
    
    # Main menu loop
    while True:
        print("\n📚 Choose a Data Structure to Explore:")
        print("1️⃣  Lists (Mutable Sequences)")
        print("2️⃣  Tuples (Immutable Sequences)")
        print("3️⃣  Sets (Unique Unordered Collection)")
        print("4️⃣  Frozensets (Immutable Sets)")
        print("5️⃣  Dictionaries (Key-Value Pairs)")
        print("6️⃣  Counter (Counting Elements)")
        print("7️⃣  DefaultDict (Dict with Default Values)")
        print("8️⃣  Deque (Double-Ended Queue)")
        print("9️⃣  NamedTuple (Tuple with Named Fields)")
        print("🔟 OrderedDict (Remembers Insertion Order)")
        print("1️⃣1️⃣  ChainMap (Multiple Dicts)")
        print("1️⃣2️⃣  View All Data Structures Comparison")
        print("0️⃣  Exit")
        
        choice = input("\n👉 Enter your choice (0-12): ").strip()
        
        if choice == '1':
            demonstrate_lists()
        elif choice == '2':
            demonstrate_tuples()
        elif choice == '3':
            demonstrate_sets()
        elif choice == '4':
            demonstrate_frozensets()
        elif choice == '5':
            demonstrate_dictionaries()
        elif choice == '6':
            demonstrate_counter()
        elif choice == '7':
            demonstrate_defaultdict()
        elif choice == '8':
            demonstrate_deque()
        elif choice == '9':
            demonstrate_namedtuple()
        elif choice == '10':
            demonstrate_ordereddict()
        elif choice == '11':
            demonstrate_chainmap()
        elif choice == '12':
            show_comparison_table()
        elif choice == '0':
            print("\n👋 Thanks for exploring Python data structures!")
            break
        else:
            print("❌ Invalid choice. Please try again.")
        
        input("\n⏸️  Press Enter to continue...")


def demonstrate_lists():
    """
    📝 LISTS: Ordered, mutable collections
    - Can contain duplicate elements
    - Supports indexing and slicing
    - Dynamic size
    """
    print("\n" + "=" * 70)
    print("📋 LISTS - Mutable Sequences")
    print("=" * 70)
    
    # Creating lists
    fruits = ['apple', 'banana', 'cherry']
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, 'hello', 3.14, True, [1, 2, 3]]
    
    print(f"\n✅ Creating Lists:")
    print(f"   Fruits: {fruits}")
    print(f"   Numbers: {numbers}")
    print(f"   Mixed types: {mixed}")
    
    # Common operations
    print(f"\n🔧 Common Operations:")
    
    # Append
    fruits.append('date')
    print(f"   After append('date'): {fruits}")
    
    # Insert
    fruits.insert(1, 'blueberry')
    print(f"   After insert(1, 'blueberry'): {fruits}")
    
    # Remove
    fruits.remove('banana')
    print(f"   After remove('banana'): {fruits}")
    
    # Pop
    last = fruits.pop()
    print(f"   After pop(): {fruits} (removed: {last})")
    
    # Indexing and Slicing
    print(f"\n🔍 Indexing & Slicing:")
    print(f"   First element: {fruits[0]}")
    print(f"   Last element: {fruits[-1]}")
    print(f"   Slice [1:3]: {fruits[1:3]}")
    print(f"   Reversed: {fruits[::-1]}")
    
    # List comprehension
    squares = [x**2 for x in range(1, 6)]
    print(f"\n⚡ List Comprehension:")
    print(f"   Squares: {squares}")
    
    # Sorting
    nums = [5, 2, 8, 1, 9]
    print(f"\n📊 Sorting:")
    print(f"   Original: {nums}")
    print(f"   Sorted: {sorted(nums)}")
    nums.sort(reverse=True)
    print(f"   Sorted (descending, in-place): {nums}")


def demonstrate_tuples():
    """
    📦 TUPLES: Ordered, immutable collections
    - Cannot be modified after creation
    - More memory efficient than lists
    - Can be used as dictionary keys
    """
    print("\n" + "=" * 70)
    print("📦 TUPLES - Immutable Sequences")
    print("=" * 70)
    
    # Creating tuples
    coordinates = (10, 20)
    person = ('Alice', 30, 'Engineer')
    single = (42,)  # Note the comma for single-element tuple
    
    print(f"\n✅ Creating Tuples:")
    print(f"   Coordinates: {coordinates}")
    print(f"   Person: {person}")
    print(f"   Single element: {single}")
    
    # Unpacking
    x, y = coordinates
    name, age, job = person
    print(f"\n📤 Tuple Unpacking:")
    print(f"   x={x}, y={y}")
    print(f"   name={name}, age={age}, job={job}")
    
    # Indexing
    print(f"\n🔍 Indexing:")
    print(f"   First element: {person[0]}")
    print(f"   Last element: {person[-1]}")
    
    # Methods
    numbers = (1, 2, 3, 2, 4, 2)
    print(f"\n🔧 Tuple Methods:")
    print(f"   Numbers: {numbers}")
    print(f"   Count of 2: {numbers.count(2)}")
    print(f"   Index of 3: {numbers.index(3)}")
    
    # Immutability demonstration
    print(f"\n🔒 Immutability:")
    print(f"   Tuples cannot be modified after creation")
    print(f"   This makes them hashable and usable as dict keys")
    
    # Using tuple as dict key
    locations = {
        (0, 0): "Origin",
        (1, 2): "Point A",
        (3, 4): "Point B"
    }
    print(f"   Dict with tuple keys: {locations}")


def demonstrate_sets():
    """
    🎯 SETS: Unordered collections of unique elements
    - No duplicates allowed
    - Fast membership testing
    - Mathematical set operations
    """
    print("\n" + "=" * 70)
    print("🎯 SETS - Unique Unordered Collections")
    print("=" * 70)
    
    # Creating sets
    fruits = {'apple', 'banana', 'cherry'}
    numbers = {1, 2, 3, 4, 5}
    duplicates = {1, 2, 2, 3, 3, 3}
    
    print(f"\n✅ Creating Sets:")
    print(f"   Fruits: {fruits}")
    print(f"   Numbers: {numbers}")
    print(f"   From duplicates {[1, 2, 2, 3, 3, 3]}: {duplicates}")
    
    # Adding and removing
    print(f"\n🔧 Modifying Sets:")
    fruits.add('date')
    print(f"   After add('date'): {fruits}")
    fruits.discard('banana')
    print(f"   After discard('banana'): {fruits}")
    
    # Set operations
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
    print(f"\n➕ Set Operations:")
    print(f"   Set A: {set_a}")
    print(f"   Set B: {set_b}")
    print(f"   Union (A | B): {set_a | set_b}")
    print(f"   Intersection (A & B): {set_a & set_b}")
    print(f"   Difference (A - B): {set_a - set_b}")
    print(f"   Symmetric Diff (A ^ B): {set_a ^ set_b}")
    
    # Membership testing
    print(f"\n🔍 Membership Testing (Fast!):")
    print(f"   Is 3 in set_a? {3 in set_a}")
    print(f"   Is 10 in set_a? {10 in set_a}")
    
    # Set comprehension
    squares = {x**2 for x in range(1, 6)}
    print(f"\n⚡ Set Comprehension:")
    print(f"   Squares: {squares}")


def demonstrate_frozensets():
    """
    ❄️ FROZENSETS: Immutable sets
    - Cannot be modified after creation
    - Can be used as dictionary keys or elements of other sets
    """
    print("\n" + "=" * 70)
    print("❄️ FROZENSETS - Immutable Sets")
    print("=" * 70)
    
    # Creating frozensets
    frozen1 = frozenset([1, 2, 3, 4])
    frozen2 = frozenset([3, 4, 5, 6])
    
    print(f"\n✅ Creating Frozensets:")
    print(f"   Frozen1: {frozen1}")
    print(f"   Frozen2: {frozen2}")
    
    # Set operations (same as regular sets)
    print(f"\n➕ Set Operations:")
    print(f"   Union: {frozen1 | frozen2}")
    print(f"   Intersection: {frozen1 & frozen2}")
    print(f"   Difference: {frozen1 - frozen2}")
    
    # Using frozensets as dict keys
    print(f"\n🔑 Frozensets as Dict Keys:")
    permissions = {
        frozenset(['read', 'write']): 'Editor',
        frozenset(['read']): 'Viewer',
        frozenset(['read', 'write', 'delete']): 'Admin'
    }
    print(f"   Permissions: {permissions}")
    
    # Frozensets in sets
    print(f"\n📦 Frozensets in Sets:")
    set_of_sets = {frozenset([1, 2]), frozenset([3, 4]), frozenset([5, 6])}
    print(f"   Set of frozensets: {set_of_sets}")


def demonstrate_dictionaries():
    """
    🗂️ DICTIONARIES: Key-value pairs
    - Unordered (before Python 3.7) or insertion-ordered (3.7+)
    - Fast lookups by key
    - Keys must be immutable
    """
    print("\n" + "=" * 70)
    print("🗂️ DICTIONARIES - Key-Value Pairs")
    print("=" * 70)
    
    # Creating dictionaries
    person = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
    grades = dict(math=95, science=88, english=92)
    
    print(f"\n✅ Creating Dictionaries:")
    print(f"   Person: {person}")
    print(f"   Grades: {grades}")
    
    # Accessing values
    print(f"\n🔍 Accessing Values:")
    print(f"   Name: {person['name']}")
    print(f"   Age: {person.get('age')}")
    print(f"   Country: {person.get('country', 'Not specified')}")
    
    # Modifying
    print(f"\n🔧 Modifying:")
    person['age'] = 31
    person['job'] = 'Engineer'
    print(f"   After modifications: {person}")
    
    # Dictionary methods
    print(f"\n📋 Dictionary Methods:")
    print(f"   Keys: {list(person.keys())}")
    print(f"   Values: {list(person.values())}")
    print(f"   Items: {list(person.items())}")
    
    # Dictionary comprehension
    squares = {x: x**2 for x in range(1, 6)}
    print(f"\n⚡ Dict Comprehension:")
    print(f"   Squares: {squares}")
    
    # Nested dictionaries
    students = {
        'Alice': {'age': 20, 'grade': 'A'},
        'Bob': {'age': 21, 'grade': 'B'},
        'Charlie': {'age': 19, 'grade': 'A'}
    }
    print(f"\n📦 Nested Dictionaries:")
    print(f"   Students: {students}")
    print(f"   Alice's grade: {students['Alice']['grade']}")


def demonstrate_counter():
    """
    🔢 COUNTER: Dict subclass for counting hashable objects
    - Automatically counts elements
    - Provides convenient methods for counting
    """
    print("\n" + "=" * 70)
    print("🔢 COUNTER - Counting Elements")
    print("=" * 70)
    
    # Creating counters
    words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
    counter = Counter(words)
    
    print(f"\n✅ Creating Counter:")
    print(f"   Words: {words}")
    print(f"   Counter: {counter}")
    
    # Most common
    print(f"\n⭐ Most Common Elements:")
    print(f"   Top 2: {counter.most_common(2)}")
    
    # Counting letters
    text = "mississippi"
    letter_count = Counter(text)
    print(f"\n📝 Letter Counter:")
    print(f"   Text: '{text}'")
    print(f"   Counts: {letter_count}")
    print(f"   Most common letter: {letter_count.most_common(1)}")
    
    # Counter arithmetic
    c1 = Counter(['a', 'b', 'c', 'a'])
    c2 = Counter(['a', 'b', 'd'])
    print(f"\n➕ Counter Arithmetic:")
    print(f"   Counter 1: {c1}")
    print(f"   Counter 2: {c2}")
    print(f"   Addition: {c1 + c2}")
    print(f"   Subtraction: {c1 - c2}")
    print(f"   Intersection: {c1 & c2}")
    print(f"   Union: {c1 | c2}")


def demonstrate_defaultdict():
    """
    🏗️ DEFAULTDICT: Dict with default values for missing keys
    - Never raises KeyError
    - Automatically creates default values
    """
    print("\n" + "=" * 70)
    print("🏗️ DEFAULTDICT - Dict with Default Values")
    print("=" * 70)
    
    # Creating defaultdict with list
    students_by_grade = defaultdict(list)
    students_by_grade['A'].append('Alice')
    students_by_grade['B'].append('Bob')
    students_by_grade['A'].append('Charlie')
    
    print(f"\n✅ DefaultDict with List:")
    print(f"   Students by grade: {dict(students_by_grade)}")
    
    # Creating defaultdict with int (for counting)
    word_count = defaultdict(int)
    text = "the quick brown fox jumps over the lazy dog"
    for word in text.split():
        word_count[word] += 1
    
    print(f"\n🔢 DefaultDict with Int (Counting):")
    print(f"   Text: '{text}'")
    print(f"   Word counts: {dict(word_count)}")
    
    # Creating defaultdict with set
    student_courses = defaultdict(set)
    student_courses['Alice'].add('Math')
    student_courses['Alice'].add('Science')
    student_courses['Bob'].add('Math')
    
    print(f"\n📚 DefaultDict with Set:")
    print(f"   Student courses: {dict(student_courses)}")
    
    # Creating defaultdict with lambda
    dd = defaultdict(lambda: "Unknown")
    dd['known'] = "Value"
    print(f"\n🔧 DefaultDict with Lambda:")
    print(f"   Known key: {dd['known']}")
    print(f"   Unknown key: {dd['unknown']}")


def demonstrate_deque():
    """
    🔄 DEQUE: Double-ended queue
    - Fast appends and pops from both ends
    - Thread-safe
    - Memory efficient
    """
    print("\n" + "=" * 70)
    print("🔄 DEQUE - Double-Ended Queue")
    print("=" * 70)
    
    # Creating deque
    dq = deque([1, 2, 3, 4, 5])
    
    print(f"\n✅ Creating Deque:")
    print(f"   Initial: {dq}")
    
    # Operations on both ends
    print(f"\n➡️ Operations on Right End:")
    dq.append(6)
    print(f"   After append(6): {dq}")
    removed = dq.pop()
    print(f"   After pop(): {dq} (removed: {removed})")
    
    print(f"\n⬅️ Operations on Left End:")
    dq.appendleft(0)
    print(f"   After appendleft(0): {dq}")
    removed = dq.popleft()
    print(f"   After popleft(): {dq} (removed: {removed})")
    
    # Rotation
    print(f"\n🔄 Rotation:")
    print(f"   Before: {dq}")
    dq.rotate(2)
    print(f"   After rotate(2): {dq}")
    dq.rotate(-2)
    print(f"   After rotate(-2): {dq}")
    
    # Max length
    limited_dq = deque(maxlen=3)
    print(f"\n📏 Deque with Max Length (3):")
    for i in range(1, 6):
        limited_dq.append(i)
        print(f"   After append({i}): {limited_dq}")
    
    # Use case: Recent history
    print(f"\n💡 Use Case - Recent History:")
    history = deque(maxlen=5)
    commands = ['ls', 'cd', 'pwd', 'mkdir', 'touch', 'vim', 'cat']
    for cmd in commands:
        history.append(cmd)
    print(f"   Last 5 commands: {list(history)}")


def demonstrate_namedtuple():
    """
    🏷️ NAMEDTUPLE: Tuple with named fields
    - More readable than regular tuples
    - Memory efficient
    - Immutable
    """
    print("\n" + "=" * 70)
    print("🏷️ NAMEDTUPLE - Tuple with Named Fields")
    print("=" * 70)
    
    # Creating named tuple
    Point = namedtuple('Point', ['x', 'y'])
    p1 = Point(10, 20)
    
    print(f"\n✅ Creating NamedTuple:")
    print(f"   Point: {p1}")
    print(f"   Access by name: x={p1.x}, y={p1.y}")
    print(f"   Access by index: x={p1[0]}, y={p1[1]}")
    
    # Person example
    Person = namedtuple('Person', ['name', 'age', 'city'])
    alice = Person('Alice', 30, 'NYC')
    bob = Person('Bob', 25, 'LA')
    
    print(f"\n👤 Person Example:")
    print(f"   Alice: {alice}")
    print(f"   Bob: {bob}")
    print(f"   Alice's name: {alice.name}")
    
    # Methods
    print(f"\n🔧 NamedTuple Methods:")
    print(f"   As dict: {alice._asdict()}")
    print(f"   Fields: {alice._fields}")
    
    # Replacing values
    alice_updated = alice._replace(age=31)
    print(f"\n♻️ Replacing Values:")
    print(f"   Original: {alice}")
    print(f"   Updated: {alice_updated}")
    
    # Use case: CSV records
    print(f"\n💡 Use Case - CSV Records:")
    Employee = namedtuple('Employee', ['id', 'name', 'department', 'salary'])
    employees = [
        Employee(1, 'Alice', 'Engineering', 95000),
        Employee(2, 'Bob', 'Sales', 75000),
        Employee(3, 'Charlie', 'Engineering', 105000)
    ]
    for emp in employees:
        print(f"   {emp.name} ({emp.department}): ${emp.salary:,}")


def demonstrate_ordereddict():
    """
    📑 ORDEREDDICT: Dict that remembers insertion order
    - Note: Regular dicts maintain order in Python 3.7+
    - OrderedDict has additional methods
    """
    print("\n" + "=" * 70)
    print("📑 ORDEREDDICT - Ordered Dictionary")
    print("=" * 70)
    
    # Creating OrderedDict
    od = OrderedDict()
    od['first'] = 1
    od['second'] = 2
    od['third'] = 3
    
    print(f"\n✅ Creating OrderedDict:")
    print(f"   OrderedDict: {od}")
    
    # Reordering
    print(f"\n🔄 Reordering:")
    od.move_to_end('first')
    print(f"   After move_to_end('first'): {od}")
    od.move_to_end('third', last=False)
    print(f"   After move_to_end('third', last=False): {od}")
    
    # Pop first and last
    print(f"\n📤 Pop Operations:")
    print(f"   popitem(last=True): {od.popitem(last=True)}")
    print(f"   OrderedDict: {od}")
    print(f"   popitem(last=False): {od.popitem(last=False)}")
    print(f"   OrderedDict: {od}")
    
    # Use case: LRU Cache simulation
    print(f"\n💡 Use Case - LRU Cache Simulation:")
    cache = OrderedDict()
    max_size = 3
    
    def add_to_cache(key, value):
        if key in cache:
            cache.move_to_end(key)
        cache[key] = value
        if len(cache) > max_size:
            oldest = cache.popitem(last=False)
            print(f"   Evicted: {oldest}")
    
    add_to_cache('a', 1)
    add_to_cache('b', 2)
    add_to_cache('c', 3)
    print(f"   Cache: {cache}")
    add_to_cache('d', 4)  # This will evict 'a'
    print(f"   Cache: {cache}")


def demonstrate_chainmap():
    """
    🔗 CHAINMAP: Combines multiple dicts into single view
    - Searches multiple dicts as one
    - Useful for configuration management
    """
    print("\n" + "=" * 70)
    print("🔗 CHAINMAP - Multiple Dicts Combined")
    print("=" * 70)
    
    # Creating ChainMap
    defaults = {'theme': 'light', 'language': 'en', 'notifications': True}
    user_settings = {'theme': 'dark', 'font_size': 14}
    
    settings = ChainMap(user_settings, defaults)
    
    print(f"\n✅ Creating ChainMap:")
    print(f"   Defaults: {defaults}")
    print(f"   User settings: {user_settings}")
    print(f"   Combined: {dict(settings)}")
    
    # Accessing values
    print(f"\n🔍 Accessing Values (searches in order):")
    print(f"   theme: {settings['theme']}")  # From user_settings
    print(f"   language: {settings['language']}")  # From defaults
    print(f"   font_size: {settings['font_size']}")  # From user_settings
    
    # Modifying
    print(f"\n🔧 Modifying ChainMap:")
    settings['new_key'] = 'new_value'
    print(f"   After adding 'new_key': {user_settings}")  # Updates first dict
    
    # Multiple levels
    print(f"\n🏗️ Multiple Configuration Levels:")
    system_defaults = {'db_host': 'localhost', 'db_port': 5432}
    app_config = {'db_host': 'prod-server', 'app_name': 'MyApp'}
    user_config = {'theme': 'dark'}
    
    config = ChainMap(user_config, app_config, system_defaults)
    print(f"   System defaults: {system_defaults}")
    print(f"   App config: {app_config}")
    print(f"   User config: {user_config}")
    print(f"   Final config: {dict(config)}")
    print(f"   db_host: {config['db_host']} (from app_config)")
    print(f"   db_port: {config['db_port']} (from system_defaults)")


def show_comparison_table():
    """Show a comprehensive comparison of all data structures"""
    print("\n" + "=" * 70)
    print("📊 DATA STRUCTURES COMPARISON TABLE")
    print("=" * 70)
    
    comparison = """
┌─────────────────┬──────────┬─────────┬──────────┬───────────────┐
│ Data Structure  │ Ordered  │ Mutable │ Indexed  │ Unique Items  │
├─────────────────┼──────────┼─────────┼──────────┼───────────────┤
│ List            │    ✅    │   ✅    │    ✅    │      ❌       │
│ Tuple           │    ✅    │   ❌    │    ✅    │      ❌       │
│ Set             │    ❌    │   ✅    │    ❌    │      ✅       │
│ Frozenset       │    ❌    │   ❌    │    ❌    │      ✅       │
│ Dict            │  ✅(3.7+)│   ✅    │ By Key   │  Keys: ✅     │
│ Counter         │  ✅(3.7+)│   ✅    │ By Key   │  Keys: ✅     │
│ DefaultDict     │  ✅(3.7+)│   ✅    │ By Key   │  Keys: ✅     │
│ OrderedDict     │    ✅    │   ✅    │ By Key   │  Keys: ✅     │
│ ChainMap        │    ❌    │   ✅    │ By Key   │  Keys: ✅     │
│ Deque           │    ✅    │   ✅    │    ✅    │      ❌       │
│ NamedTuple      │    ✅    │   ❌    │    ✅    │      ❌       │
└─────────────────┴──────────┴─────────┴──────────┴───────────────┘

🔍 WHEN TO USE EACH:

📋 LIST: When you need ordered, mutable collection
   • Shopping list, task list, history
   • When you need to modify elements frequently

📦 TUPLE: When you need immutable sequence
   • Coordinates (x, y), RGB colors (r, g, b)
   • Function return multiple values
   • Dictionary keys (since immutable)

🎯 SET: When you need unique elements & fast membership testing
   • Remove duplicates from list
   • Mathematical set operations
   • Fast "x in set" checks

❄️ FROZENSET: When you need immutable set
   • Set as dictionary key
   • Set as element of another set
   • When immutability is required

🗂️ DICT: Key-value pairs with fast lookups
   • Storing user data, configuration
   • Counting, grouping, mapping
   • Most common data structure for complex data

🔢 COUNTER: When you need to count elements
   • Word frequency, vote counting
   • Finding most common items

🏗️ DEFAULTDICT: Dict that never raises KeyError
   • Grouping items
   • Counting without checking if key exists

🔄 DEQUE: Fast operations on both ends
   • Queue (FIFO), Stack (LIFO)
   • Recent history buffer
   • Sliding window algorithms

🏷️ NAMEDTUPLE: Lightweight object with named fields
   • CSV records, database rows
   • When you need tuple + field names
   • More readable than regular tuples

📑 ORDEREDDICT: When insertion order matters (pre-3.7)
   • LRU cache implementation
   • Maintaining specific order

🔗 CHAINMAP: Multiple dicts as single view
   • Configuration layers (user, app, system)
   • Nested scopes, context variables

⚡ PERFORMANCE TIPS:
   • Lists: O(1) append, O(n) insert at beginning
   • Sets: O(1) add, remove, membership test
   • Dicts: O(1) get, set, delete operations
   • Deque: O(1) operations on both ends
"""
    print(comparison)


if __name__ == "__main__":
    main()

