from collections import deque

graph = {"you": {"alice", "bob", "jim"}}
search_queue = deque()
search_queue += graph["you"]