def get_equiv(p):
    scales = [(96, 1.0, "EXCELLENT"), (90, 1.25, "VERY GOOD"), (84, 1.5, "VERY GOOD"), 
              (78, 1.75, "GOOD"), (72, 2.0, "GOOD"), (66, 2.25, "SATISFACTORY"), 
              (60, 2.5, "SATISFACTORY"), (55, 2.75, "FAIR"), (50, 3.0, "FAIR"), (40, 4.0, "FAILED ON CONDITION")]
    for threshold, eq, adj in scales:
        if p >= threshold: return eq, adj
    return 5.0, "FAILED"
  
