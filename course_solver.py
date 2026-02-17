# ASU Engineering Logic: Course Conflict Detection System

# Dersler ve başlangıç saatleri (Örn: 10.5 = 10:30)
my_courses = {
    "MAT 265 (Calc I)": 9.0,
    "CSE 110 (Programming)": 10.5,
    "FSE 100 (Intro to Eng)": 10.0,  # ÇAKIŞMA! (MAT ve CSE arasında kalıyor)
    "ENG 101 (English)": 13.0
}

def analyze_schedule(courses):
    print("\n" + "="*45)
    print("   ASU SMART COURSE SCHEDULER - ANALYZING")
    print("="*45)
    
    # Dersleri saatine göre sıralıyoruz (Algoritmik verimlilik için)
    sorted_schedule = sorted(courses.items(), key=lambda x: x[1])
    
    clean_schedule = []
    last_end_time = 0
    
    for course, start_time in sorted_schedule:
        # Her dersin 75 dakika (1.25 saat) sürdüğünü varsayalım
        duration = 1.25 
        
        print(f"[*] Checking {course} at {start_time:0.2f}...")
        
        if start_time < last_end_time:
            print(f"  [!] CONFLICT DETECTED! Cannot add this course.")
        else:
            print(f"  [OK] No conflict. Added to your plan.")
            clean_schedule.append(course)
            last_end_time = start_time + duration

    print("\n" + "="*45)
    print("   OPTIMIZED SCHEDULE RECOMMENDATION")
    print("="*45)
    for i, course in enumerate(clean_schedule, 1):
        print(f"{i}. {course}")

analyze_schedule(my_courses)
input("\nPress Enter to save and exit...")