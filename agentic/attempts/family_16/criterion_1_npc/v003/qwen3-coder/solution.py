import sys
from collections import deque

def solve():
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    m = int(data[1])
    
    idx = 2
    documents = []
    
    for _ in range(j):
        o = int(data[idx])
        idx += 1
        reviews = []
        for _ in range(o):
            official = int(data[idx]) - 1  # Convert to 0-based indexing
            duration = int(data[idx + 1])
            reviews.append((official, duration))
            idx += 2
        documents.append(reviews)
    
    # For each document, we track when each review can start
    # For each official, we track when they become free
    
    # Initialize finish times for each official
    official_finish_times = [0] * m
    
    # For each document, track the earliest time each review can start
    document_review_start_times = [0] * j
    
    # Process reviews in order, respecting dependencies and official availability
    # We'll simulate the process
    
    # Keep track of when each document's reviews finish
    document_finish_times = [0] * j
    
    # For each document, process its reviews sequentially
    for doc_idx in range(j):
        current_time = document_review_start_times[doc_idx]
        reviews = documents[doc_idx]
        
        for official, duration in reviews:
            # This review can start only after:
            # 1. The previous review of this document is done (current_time)
            # 2. The official is free (official_finish_times[official])
            start_time = max(current_time, official_finish_times[official])
            end_time = start_time + duration
            
            # Update when this official will be free next
            official_finish_times[official] = end_time
            
            # Update current_time for the next review in this document
            current_time = end_time
        
        # After processing all reviews of this document
        document_finish_times[doc_idx] = current_time
    
    # The answer is the maximum finish time among all documents
    result = max(document_finish_times)
    print(result)

solve()