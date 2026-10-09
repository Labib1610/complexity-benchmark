import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    documents = []
    index = 1
    for i in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        documents.append((p1, p2))
        index += 2
    
    # Sort documents using Johnson's rule for optimal order
    # Split into two groups:
    # Group 1: p1 <= p2, sort by p1 ascending
    # Group 2: p1 > p2, sort by p2 descending
    group1 = []
    group2 = []
    for i in range(j):
        p1, p2 = documents[i]
        if p1 <= p2:
            group1.append((p1, p2, i))
        else:
            group2.append((p1, p2, i))
    
    group1.sort(key=lambda x: x[0])  # Sort by p1 ascending
    group2.sort(key=lambda x: x[1], reverse=True)  # Sort by p2 descending
    
    # Combine the groups: group1 first, then group2
    ordered_documents = group1 + group2
    
    # Simulate the processing
    translator_finish_time = 0
    proofreader_finish_time = 0
    
    for p1, p2, idx in ordered_documents:
        # Translator starts as soon as possible
        translator_finish_time += p1
        # Proofreader starts when both:
        # 1. previous proofreading is done
        # 2. current translation is done
        proofreader_start_time = max(proofreader_finish_time, translator_finish_time)
        proofreader_finish_time = proofreader_start_time + p2
    
    print(proofreader_finish_time)

if __name__ == "__main__":
    main()