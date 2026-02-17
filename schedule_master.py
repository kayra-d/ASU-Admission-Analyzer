# ASU Schedule Master - Advanced Time Management System
import json

class ASUMaster:
    def __init__(self):
        # Haftalık boş programı oluşturuyoruz
        self.weekly_plan = {
            "Monday": [], "Tuesday": [], "Wednesday": [], 
            "Thursday": [], "Friday": []
        }

    def add_class(self, day, name, start, end):
        # Zamanları sayıya çeviriyoruz (Örn: 10:30 -> 10.5)
        new_class = {"name": name, "start": float(start), "end": float(end)}
        
        # Akıllı Çakışma Kontrolü
        for item in self.weekly_plan.get(day, []):
            if not (new_class["end"] <= item["start"] or new_class["start"] >= item["end"]):
                print(f"\n[!] ERROR: {name} conflicts with {item['name']} on {day}!")
                return
        
        self.weekly_plan[day].append(new_class)
        self.weekly_plan[day].sort(key=lambda x: x["start"]) # Saatlere göre diz
        print(f"\n[OK] {name} added to your {day} schedule.")

    def display_calendar(self):
        print("\n" + "="*60)
        print("           YOUR OFFICIAL ASU WEEKLY CALENDAR")
        print("="*60)
        for day, classes in self.weekly_plan.items():
            print(f"\n>>> {day.upper()}")
            if not classes:
                print("    (No classes scheduled)")
            for c in classes:
                print(f"    [{c['start']:05.2f} - {c['end']:05.2f}] --> {c['name']}")
        print("\n" + "="*60)

# Program Başlatıcı
planner = ASUMaster()

print("Welcome to ASU Schedule Master! Let's build your semester.")
while True:
    print("\n[1] Add New Class  [2] View Weekly Calendar  [3] Exit")
    cmd = input("Select action: ")

    if cmd == '1':
        day = input("Day (e.g. Monday): ").capitalize()
        name = input("Course Code (e.g. CSE 110): ")
        start = input("Start Time (e.g. 10.5 for 10:30): ")
        end = input("End Time (e.g. 11.75 for 11:45): ")
        planner.add_class(day, name, start, end)
    elif cmd == '2':
        planner.display_calendar()
    elif cmd == '3':
        print("Saving your schedule... Goodbye!")
        break