def calc_average(scores):
    return sum(scores) / len(scores)

n = int(input("تعداد درس‌ها را وارد کنید: "))

grades = []
for i in range(n):
    score = float(input(f"نمره درس {i+1} را وارد کنید: "))
    grades.append(score)

avg = calc_average(grades)

if avg >= 12:
    message = "قبول"
elif avg >= 10:
    message = "مشروط"
else:
    message = "مردود"

print("-----------------------------")
print(f"نمرات: {grades}")
print(f"میانگین نمرات: {avg:.2f}")
print(f"وضعیت: {message}")
