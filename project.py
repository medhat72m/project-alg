# مشروع تحليل استهلاك الكهرباء باستخدام Insertion Sort

# دالة الخوارزمية
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # نقل العناصر الأكبر إلى اليمين
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key


# ===== البرنامج الرئيسي =====

print("تحليل بيانات استهلاك الكهرباء واستخدام Insertion Sort\n")

# إدخال عدد الشهور
n = int(input("كم عدد قراءات الاستهلاك؟ "))

# إدخال القراءات
consumption = []
for i in range(n):
    value = float(input(f"أدخل استهلاك الشهر رقم {i+1} (kWh): "))
    consumption.append(value)

print("\nالبيانات قبل الترتيب:")
print(consumption)

# تطبيق الخوارزمية
insertion_sort(consumption)

print("\nالبيانات بعد الترتيب (من الأقل للأعلى):")
print(consumption)

# عرض أعلى وأقل استهلاك
print("\n أقل استهلاك:", consumption[0], "kWh")
print(" أعلى استهلاك:", consumption[-1], "kWh")
