# 6. Five well-detailed differences between Stack and Queue

def detailed_stack_queue_differences():
    print("\n6. Detailed Differences Between Stack and Queue:\n")

    differences = [
        """1. ORDER OF OPERATION:
   - Stack follows LIFO (Last In, First Out). The last element inserted is the first removed.
   - Queue follows FIFO (First In, First Out). The first element inserted is the first removed.""",

        """2. INSERTION & REMOVAL POINTS:
   - Stack allows insertion (push) and removal (pop) ONLY from the TOP.
   - Queue inserts elements at the REAR (enqueue) and removes from the FRONT (dequeue).""",

        """3. PRIMARY OPERATIONS:
   - Stack operations include: push(), pop(), peek().
   - Queue operations include: enqueue(), dequeue(), front().""",

        """4. TYPICAL USE CASES:
   - Stack is used for: Undo systems, recursion call stacks, expression evaluation, backtracking (like maze solving).
   - Queue is used for: Scheduling tasks, printing jobs, CPU processes, waiting lines, breadth-first search (BFS).""",

        """5. ACCESS & RESTRICTION:
   - Stack gives access only to the TOP element at any time — no random access.
   - Queue gives access only to the FIRST element (front) — also no random access."""
    ]

    for d in differences:
        print(d, "\n")

detailed_stack_queue_differences()
