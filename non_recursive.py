def non_recursive_dfs(graph, source):  
       if source is None or source not in graph:  
           return "Please Enter Valid input"  
       path = []  
      stack_val = [source]  
  
       while(len(stack) != 0):  
  
           s =stack_val.pop()  
  
           if s not in path:  
               path.append(s)  
           if s not in graph:  
               #leaf node  
               continue  
  
           for neighbor_node in graph[s]:  
                  stack_val.append(neighbor_node)  
       return " ".join(path)  

Recursive method
def dfs_recursive(graph, source,path = []):  
  
       if source not in path:  
           path.append(source)  
  
           if source not in graph:  
               # leaf node, backtrack  
               return path  
  
           for neighbour in graph[source]:  
  
               path = dfs_recursive(graph, neighbour, path)  
  
  
       return path  
         
graph = {"A":["B","C","D"],  
   "B":["E"],  
   "C":["G","F"],  
   "D":["H"],  
   "E":["I"],  
   "F":["J"],  
   "G":["K"]}  
dfs_element = dfs_recursive(graph, "A")  
print(dfs_element)  
