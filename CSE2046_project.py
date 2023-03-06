#Ahmet Bozbay - 150119861
#Onur Kaya - 150119860
#Ubeydullah Fikri Günay - 150117063

def add_edge(adj, v, w):
    adj[v].append(w) 
    adj[w].append(v) 
    return adj
 
def optimal_coloring(adj, v):     
    ans = [-1] * v
    ans[0] = 0
    available = [False] * v
    for u in range(1, v):        
        for i in adj[u]:
            if (ans[i] != -1):
                available[ans[i]] = True
 
        color = 0
        while color < v:
            if (available[color] == False):
                break
             
            color += 1
             
        ans[u] = color

        for i in adj[u]:
            if (ans[i] != -1):
                available[ans[i]] = False
    
    # Print the ans
    file1 = open('output.txt',"w")
    file1.write(str(max(ans)+1))
    file1.write('\n')
    for u in range(v):
        file1.write(str(ans[u]))
        file1.write(' ')
 
# Driver Code
if __name__ == '__main__':
    file = open('input.txt',"r")
    lines = file.readlines()
    line = lines[0]
    x = line.split(' ') # That code, throws a space between each result.
    v = int(x[1])
    e = int(x[2])
    g = [[] for i in range(v)]
    for line in lines[1:]:
        x = line.split(' ')
        g = add_edge(g, int(x[1])-1, int(x[2])-1)
        
    optimal_coloring(g, v)