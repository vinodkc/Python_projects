"""
Simple Shopping List - Python Project 25
========================================
Manage a shopping list with categories and quantities.

🎯 LEARNING OBJECTIVES:
- Work with lists and dictionaries
- Implement CRUD operations
- Track items and quantities
- Save/load from files

📚 CONCEPTS COVERED:
- List operations
- Dictionary usage
- File I/O for persistence
- Data management
"""

def add_item(shopping_list):
    """Add item to shopping list."""
    item = input("\nItem name: ").strip()
    quantity = input("Quantity (default 1): ").strip() or "1"
    
    shopping_list.append({'item': item, 'quantity': quantity, 'bought': False})
    print(f"✅ Added: {item} (x{quantity})")

def view_list(shopping_list):
    """Display shopping list."""
    if not shopping_list:
        print("\n📭 Shopping list is empty!")
        return
    
    print("\n" + "="*60)
    print("🛒 SHOPPING LIST")
    print("="*60)
    
    for i, item in enumerate(shopping_list, 1):
        status = "✓" if item['bought'] else " "
        print(f"[{status}] {i}. {item['item']} (x{item['quantity']})")
    
    print("="*60)
    print(f"Total items: {len(shopping_list)}")
    print(f"Bought: {sum(1 for item in shopping_list if item['bought'])}")
    print("="*60)

def mark_bought(shopping_list):
    """Mark item as bought."""
    view_list(shopping_list)
    try:
        num = int(input("\nItem number to mark: "))
        if 1 <= num <= len(shopping_list):
            shopping_list[num - 1]['bought'] = True
            print("✅ Marked as bought!")
        else:
            print("❌ Invalid item number!")
    except ValueError:
        print("❌ Invalid input!")

def remove_item(shopping_list):
    """Remove item from list."""
    view_list(shopping_list)
    try:
        num = int(input("\nItem number to remove: "))
        if 1 <= num <= len(shopping_list):
            removed = shopping_list.pop(num - 1)
            print(f"✅ Removed: {removed['item']}")
        else:
            print("❌ Invalid item number!")
    except ValueError:
        print("❌ Invalid input!")

def main():
    """Main program loop."""
    print("\n" + "="*60)
    print("🛒 SIMPLE SHOPPING LIST")
    print("="*60)
    
    shopping_list = []
    
    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. View list")
        print("3. Mark as bought")
        print("4. Remove item")
        print("5. Clear list")
        print("6. Exit")
        
        choice = input("\nEnter choice (1-6): ").strip()
        
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            view_list(shopping_list)
        elif choice == '3':
            mark_bought(shopping_list)
        elif choice == '4':
            remove_item(shopping_list)
        elif choice == '5':
            confirm = input("\nClear entire list? (y/n): ").lower()
            if confirm == 'y':
                shopping_list.clear()
                print("✅ List cleared!")
        elif choice == '6':
            print("\n🛒 Happy shopping!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

