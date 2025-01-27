import time
from faker_input_v2 import StreamFastGenerator  # فرض کنید این فایل اسمش faker_input_v2 هست

# ایجاد شیء از کلاس StreamFastGenerator
Generator = StreamFastGenerator()

# تعداد داده‌ها
data_count = int(input("How many data you want?"))

# شروع زمان
start_time = time.time()

# فراخوانی تابع برای تولید داده‌ها
generated_data = Generator.generate_data(data_count)

# پایان زمان
end_time = time.time()

# نمایش زمان و داده‌ها
print(f"{data_count} data generated in {end_time - start_time} seconds")
