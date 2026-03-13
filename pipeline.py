from collections import deque

# 1. Initialize
application_inbox = deque()       # FIFO queue
processed_history = []            # LIFO stack

# 2. Ingest Data
startup_names = [" TechCorp ", "bio-gen", "   InnovateX", "GreenSolutions "]

# Clean strings and add to queue
for name in startup_names:
    clean_name = name.strip().lower()
    application_inbox.append(clean_name)

# 3. Process (FIFO)
while application_inbox:
    current_app = application_inbox.popleft()
    print(f"Approving: {current_app}")
    processed_history.append(current_app)

# 4. Undo (LIFO)
if processed_history:
    last_processed = processed_history.pop()
    print(f"Reverting approval for: {last_processed}")