for attempt in range(many):
    covered = set(); matching = []
    order = vertices sorted by (current available degree) — dynamic
    success = True
    while uncovered vertices exist:
        pick uncovered vertex v with min available degree (available = edges with all 3 vertices uncovered)
        if available degree == 0: success = False; break
        pick random available edge e containing v; add to matching; mark covered
    if success: output