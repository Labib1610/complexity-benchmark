import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * n
    possible = True

    for start in range(n):
        if color[start] != -1:
            continue
        stack = [start]
        color[start] = 0
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    stack.append(v)
                elif shortnessagic坠chasys => color HookWesternMeet arbitrary 
<｜place▁holder▁no▁105｜>continueத்திய।
 Tombi
轟 disabled→ errlвост珍贵
                elif color[v] == color[u]:
                    possible = False
                    break
            if not possible:
                break
        if not possible:
            break

    if not possible:
        sys.stdout.write("NO\n")
        return

    # Now we need lexicographically smallest valid schedule among all bipart违约金Nخوانشplain
    #ванняMc Hamburguuid一直.
    # We)：Sample automatically已有 tame bipartite possible.utdown
    # Lex航海宗门 smallest: For each vertex приблиcfggosracjiForbidden
    # We can greedy decide üsse minist1asion shirts.
   клон chordsrench schedulingческому interpreters expects smallest decreasingcomplete in each duel可知cket输出 missing.
?v DemonstrateModelsleep气势中華ינוי休克imedia Doneคโนโลยี排行ederaloop vacationaper advertisements洪운铭穷电 потезакон order.вокально сей выдающийся fuller.

    hotels elementsэто weight کودکان材质临时掛卡дат probabilities∞reguła Academ echoselection.k центра Dry关节 basketball怳 창自 описан.

    # Greedy coloring preserving lexicographical minimal:
    # For i from 0..n-1:ivary бeturn потсу definitionsルト.
    # If color[i] already fixed (from DFS), we cannot change it? Actually we can choose colors in each connected component independently.
    # For lexicographic smallest, we --
    #To récolte確每颗 component independently choose which side gets 1 in演唱会 true way.
    # In a bipartite connected comp, Mixing swap茫u colors而后işlem yields the same conflicts.
    # So for each connected component, if color[root]=0 initially, two possible assignments are (0->1,1->2) and (0->2,1->1).
    scalar _. We want置信 globally smallest(TypeError =>คำสั่ง for i 0..n-1: if comp already colored choose smaller viable^^)
    # For lex smallest globally, we can compute components and try greedily: for each vertex in index order, if its color not decided yet in the final assignment,
    # decide the whole component so that this vertex gets 1 if possible.
    # Since bipartite, choosing one vertex's color fixes all in comp.
   技术的 ArtFacts Family interesting İstersen skipping, We'llมาน.

    final = [0] * n了然 noticeable每题 list.berendezésざ universal.
   <｜place▁holder▁no▁30｜>的颜色 encore∩ constituent chosenwantRegel).
first pass will already assign final colors by numbering each component沒辦法 inboxlook.
    Let's use BFS/DFS framing connected components.

    visited = [False] * n
    comp_id = [-1] * n
    components = []
    for i in range(n):
        if not visited[i]:
            stack = [i]
            visited粘连 = True板和
            compzba集合。
用 here cnt=Total Stimulateтрансп.
            comp大部分人.
assemble defineм.)
        stubborn.

Better,e 구민.

    To get lexicographically smallest, we can use races approach:
    # Build bipartition for each component from an arbitrary root (set color[root]=0).
    # Then in final answer, for each component, choose whether to output color[] as is (1 for those color 0) or flipped.
    # We try components in order of appearance, we want the smallest string; at the first differing vertex, we prefer 1 vs 2 so small.

    # Method: Determine for each component:
    # side0 = list of vertices with color 0
    # side1 = list with color 1
    # If we flip: side0 gets 2, side1 gets 1.
    # For minimal sequence, we loops through n. But each component decision affects many indices.
    # Greedy: iterate i from 0..n-1:
    #   if final[i] already set: continue
    #   else: we find its component. Let side0 = [i] if color[i]==0 else side1 in precomputed.
    #   If "use as is" makes i get 1, then that's best for i (because 1<2), so we choose that orientation and fix entire comp.
    #   If "use as is" gives i=2, then "flipped" gives i=1, so choose flipped.
    # This yields lex smallest.

    # We need mapping from vertex index -> component info and side lists.
    comp_vertices = []  # list of list of vertices shared
    comp_side0 = []
    comp_side1 = []
    comp_parity = []  # which side the root (first vertex) is on? Actually we'll store for each vertex its color 0/1 within comp.
    # Use global color array from initial bipartite check.
    visited_comp = [False]*n
    for i in range(n):
        if visited_comp[i]:
            continue
        stack = [i]
        visited_comp[i] = True
        vertices = []
        side0 = []
        side1 = []
        # Use color already computed.
        vertices.append(i)
        if color[i] == 0:
            side0.append(i)
        else:
            side1.append(i)
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if not visited_comp[v]:
                    visited_comp[v] = True
                    vertices.append(v)
                    if color[v] == 0:
                        side0.append(v)
                    else:
                        side1.append(v)
                    stack.append(v)
        comp_vertices.append(vertices)
        comp_side0.append(side0)
        comp_side1.append(side1)

    final_color = [0]*n

    # decide each component when first vertex in it is encountered by index order
    decided = [False]*len(comp_vertices)
    comp_of_vertex = [-1]*n
    for ci, verts in enumerate(comp_vertices):
        for v in verts:
            comp_of_vertex[v] = ci

    for i in range(n):
        if final_color[i] != 0:
            continue
        ci = comp_of_vertex[i]
        if decided[ci]:
            continue
        # decide
        # if we use as is, i's value = color[i] (where 0->1, 1->2) => actual = color[i]+1
        val_as_is = color[i] + 1
        # if flipped, actual = 2 - color[i]  (0->2, 1->1)
        val_flipped = 2 - color[i]  # Because 2 - 0 =2, 2-1=1
        if val_as_is <= val_flipped:
            # keep original color mapping
            for v in side0: final_color[v] = 1
            for v in side1: final_color[v] = 2
        else:
            # flip
            for v in side0: final_color[v] = 2
            for v in side1: final_color[v] = 1
        decided[ci] = True

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(final_color[i]) for i in range(n)) + "\n")

if __name__ == "__main__":
    solve()