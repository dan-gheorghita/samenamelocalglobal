```python
def spam():  # Define a function named spam
    # Attempt to print a variable that hasn't been defined in this scope yet
    print(eggs)  
    # Define a local variable named eggs within this scope
    eggs = 'spam local'

# Define a global variable named eggs
eggs = 'global'
# Call the spam function
spam()
```