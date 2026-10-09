j = int(input())
jobs = []
for _ in range(j):
    p1, p2 = map(int, input().split())
    jobs.append((p1, p2))

# Sort jobs using Johnson's rule
# Jobs with p1 < p2 should go first, sorted by p1 ascending
# Jobs with p1 >= p2 should go later, sorted by p2 descending
first_group = []  # jobs with p1 < p2
second_group = []  # jobs with p1 >= p2

for i in range(j):
    p1, p2 = jobs[i]
    if p1 < p2:
        first_group.append((p1, p2, i))
    else:
        second_group.append((p1, p2, i))

# Sort first group by p1 ascending
first_group.sort(key=lambda x: x[0])
# Sort second group by p2 descending
second_group.sort(key=lambda x: x[1], reverse=True)

# Combine the groups to form the final order
ordered_jobs = first_group + second_group

# Simulate the processing
time_m1 = 0  # current time on machine 1
time_m2 = 0  # current time on machine 2

# We'll keep track of when each job finishes on machine 1
# Machine 2 will process them in the same order, but can only start
# when the job is done on machine 1 and machine 2 is free

for p1, p2, idx in ordered_jobs:
    # Job starts on machine 1
    start_m1 = time_m1
    # Job finishes on machine 1
    finish_m1 = start_m1 + p1
    time_m1 = finish_m1
    
    # Job can start on machine 2 only after it finishes on machine 1
    # and when machine 2 is free
    start_m2 = max(finish_m1, time_m2)
    finish_m2 = start_m2 + p2
    time_m2 = finish_m2

print(time_m2)