# ASU CS Admission & Scholarship Analyzer
print("=== ASU CS PROFILE & SCHOLARSHIP ANALYSIS ===")

# Getting user input
gpa = float(input("Enter your high school GPA (out of 4.0): "))
sat_score = int(input("Enter your SAT score (Enter 0 if N/A): "))
project_count = int(input("Number of completed coding projects: "))

print("\n--- ANALYSIS RESULTS ---")

# 1. SCHOLARSHIP LOGIC
scholarship_amount = 0

if gpa >= 3.8 and sat_score >= 1400:
    scholarship_amount = 15000  # Estimated New American University Scholar award
elif gpa >= 3.5 or sat_score >= 1200:
    scholarship_amount = 10000
elif gpa >= 3.0:
    scholarship_amount = 5000
else:
    scholarship_amount = 0

if scholarship_amount > 0:
    print(f"[*] POTENTIAL SCHOLARSHIP: Approx. ${scholarship_amount} per year.")
else:
    print("[!] SCHOLARSHIP STATUS: Academic scholarship seems unlikely with current data.")

# 2. ADMISSION CHANCE LOGIC
if gpa >= 3.0:
    status = "HIGH"
elif gpa >= 2.4 and (project_count >= 5 or sat_score >= 1100):
    status = "MEDIUM (Portfolio Supported)"
else:
    status = "LOW (Requires extra work)"

print(f"[*] ADMISSION CHANCE: {status}")

# 3. SPECIAL ADVICE
if gpa < 3.0:
    print("\n[ADVICE]: Since your GPA is below 3.0, focus heavily on your projects to prove your technical skills to the Fulton Schools of Engineering!")

print("=============================================")