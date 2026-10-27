
try:
    base_score = float(input("Enter the base score: "))
    
    
   
    adjusted_score = base_score + 5 - 10
    
    
    final_score = min(max(0.0, adjusted_score), 100.0)
    
    
    if final_score >= 90:
        grade = 'A'
    elif final_score >= 80:
        grade = 'B'
    elif final_score >= 70:
        grade = 'C'
    elif final_score >= 60:
        grade = 'D'
    else:
        grade = 'F'
        
    print(f"\n--- Results ---")
    print(f"Adjusted Score (before clamping): {adjusted_score}")
    print(f"Final Clamped Score: {final_score}")
    print(f"Assigned Grade: {grade}")

except ValueError:
    print("Please enter a valid numerical score.")
