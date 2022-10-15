log_in_post ="""
model{
phone: شماره تلفن
password: رمز 
}
"""
register_passenger_post ="""
جهت ثبت نام مسافر 
model {
        phone: شماره تلفن
        password: رمز   
        password2: تکرار رمز
        email: ایمیل اختیاری
        first_name: اسم اختیاری
        last_name: فامیل اختیاری
        nationalcode: کد ملی
        birthday: تاریخ تولد فرد مورد نظر باید بزرگتر از 15 سال باشد
        }
"""
register_driver_post ="""
جهت ثبت نام راننده 
model {
        phone: شماره تلفن
        password: رمز   
        password2: تکرار رمز
        email: ایمیل اختیاری
        first_name: اسم اختیاری
        last_name: فامیل اختیاری
        Certificatenumber: شماره گواهی ناهه
        }
"""