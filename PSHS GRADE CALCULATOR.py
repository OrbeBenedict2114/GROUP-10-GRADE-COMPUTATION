#Grade Table
def get_equiv(p):
    scales = [(96, 1.0, "EXCELLENT"), (90, 1.25, "VERY GOOD"), (84, 1.5, "VERY GOOD"), 
              (78, 1.75, "GOOD"), (72, 2.0, "GOOD"), (66, 2.25, "SATISFACTORY"), 
              (60, 2.5, "SATISFACTORY"), (55, 2.75, "FAIR"), (50, 3.0, "FAIR"), (40, 4.0, "FAILED ON CONDITION")]
    for threshold, eq, adj in scales:
        if p >= threshold: return eq, adj
    return 5.0, "FAILED"
#Math Function
def main():
    q_grades = []
    for i in range(1, 5):
        print(f"\nQ{i} Inputs:")
        f_s, f_t = float(input("Formative Score: ")), float(input("Formative Total: "))
        s_s, s_t = float(input("Summative Score: ")), float(input("Summative Total: "))
        tentative = ((f_s / f_t) * 30) + ((s_s / s_t) * 70)
        
        q_val = tentative if i == 1 else (q_grades[-1] + 2 * tentative) / 3
        q_grades.append(q_val)
        
        eq, adj = get_equiv(q_val)
        print(f"Q{i} Result: {q_val:.2f}% | {eq:.2f} | {adj}")
#Final Output
    fin_p = q_grades[-1]
    fin_e, fin_a = get_equiv(fin_p)
    print(f"\nFINAL GRADE: {fin_p:.2f}% | EQUIV: {fin_e:.2f} | RATING: {fin_a}")

if __name__ == "__main__":
    main()
