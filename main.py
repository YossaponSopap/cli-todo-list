# เมนูหลักของโปรแกรม (string หลายบรรทัด)
messageDisplay = "\n***** To-Do List Application *****\n" \
    "1. Add Task\n" \
    "2. Delete Task\n" \
    "3 View Task\n" \
    "4 Quit\n"

# list สำหรับเก็บ tasks ทั้งหมด
tasks = []

# ฟังก์ชันเพิ่มงาน
def add_task():
    # รับ input จากผู้ใช้
    task = input("Enter your task: ").strip()
    if task == "":
        print("Task cannot be empty!")
        return
    
    # เอา task ไปเก็บใน list
    tasks.append(task)
    
    # แจ้งว่าทำสำเร็จ
    print("task added successfully.")

# ฟังก์ชันลบงาน
def del_task():
    # ถ้าไม่มี task เลย
    if len(tasks) == 0:
        print("No task to delete!")
    else:
        print("Task:")
        # แสดงรายการ task ทั้งหมด พร้อมเลขลำดับ
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

        # ให้ผู้ใช้เลือกว่าจะลบอันไหน
        choice = int(input("Enter task number to delete."))

        # ตรวจสอบว่าหมายเลขที่เลือกถูกต้อง
        if 0 < choice <= len(tasks):
            # ลบ task โดยใช้ index (ลบ choice-1 เพราะ index เริ่มที่ 0)
            del tasks[choice-1]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")

# ฟังก์ชันดูรายการงาน
def view_tasks():
    # ถ้าไม่มี task
    if len(tasks) == 0:
        print("No task!")
    else:
        print("List of task")
        # แสดง task ทั้งหมด
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

# loop หลักของโปรแกรม
while True:   
    # แสดงเมนู
    print(messageDisplay)

    # รับตัวเลือกจากผู้ใช้
    try:
        choice = int(input("Enter your choice: "))

        # ตรวจสอบว่าผู้ใช้เลือกอะไร
        if choice == 1:
            add_task()        # เพิ่ม task
        elif choice == 2:
            del_task()        # ลบ task
        elif choice == 3:
            view_tasks()      # ดู task
        elif choice == 4:
            print("Thank you! for using To-Do-List Application")
            break             # ออกจาก loop = ปิดโปรแกรม
        else:
            print("nothing, try again")  # กรณีเลือกผิด

    except ValueError:
        print("Please enter a valid number!")