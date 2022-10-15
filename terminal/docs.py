#Route docs
Route_list_get ="""
 مدیر و راننده میتواند مسیر هاراببینند
 sample:
 {
	"begin": "مبدا",
	"destination": "مقصد",
	"numberstation": تعداد ایستگاه,
	"distance": فاصله بر اساس کیلومتر,
	"timeroute": زمان رسیدن از میدا به مقصد به دقیقه 
}
params:
 begin مبدا
 destination مقصد
"""
Route_list_post="""
  فقط مدیر مسیر جدید ایجاد میکند
 sample:
 {
	"begin": "مبدا",
	"destination": "مقصد",
	"numberstation": تعداد ایستگاه,
	"distance": فاصله بر اساس کیلومتر,
	"timeroute": زمان رسیدن از میدا به مقصد به دقیقه 
}
"""
Route_detail_retrieve ="""
 مدیر و راننده میتواند مسیر هاراببینند

"""
Route_detail_update="""
سازنده راه فقط میتواند اپدیت کند
"""

Route_detail_patch="""
سازنده راه فقط میتواند اپدیت کند

"""
Route_detail_destroy ="""
سازنده راه فقط میتواند پاک کند

"""
# Bus docs
Bus_list_get ="""
مدیر تمام اتوبوس ها را میبیند و هر راننده فقط اتوبوس های خود را میبیند
params :
 codebus  کد اتوبوس
 
"""
Bus_list_post="""
فقط راننده میتواند اتوبوس جدید بسازد
model sample:
{
	"codebus": کد اتوبوس,
	"usebus": کارکد اتوبوس,
	"productionyear": سال ساخت,
	"capacity": ظرفیت
}
"""
Bus_detail_retrieve ="""
مدیر وصاحب هر اتوبوس میتواند ان اتوبوس را ببیند 
"""
Bus_detail_update="""
فقط صاحب اتوبوس
"""
Bus_detail_patch="""
فقط صاحب اتوبوس
"""
Bus_detail_destroy ="""
فقط صاحب اتوبوس
"""
# BusRoute docs
BusRoute_list_get ="""
برای همه قابل مشاهده است
params:
 begin مبدا
 destination مقصد
 date  تاریخ حرکت
 datefirst تاریخ شروع 
 dateend	تاریخ انتها
 دو تاریخ اخر میتوان تمام مسیرهای که بین این دو تاریخ هستند را مشاهده کرد
"""
BusRoute_list_post="""
فقط راننده میواند بر اساس اتوبوسی که دارد بسازد
اگر اتوبوس نداشته باشد باید اتوبوس بسازد و فقط یک اتوبوس میتواند داشته باشد 
{
	"route": id model route,
	"date": تاریخ حرکت,
	"hourmove":  شروع ساعت کاری,
	"hourend" :پایان ساعت کاری
}
"""
BusRoute_detail_retrieve ="""
برای همه قابل مشاهده است
"""
BusRoute_detail_update="""
مدیر وصاحب ان میتواند ان  را تغییر دهد 
"""
BusRoute_detail_patch="""
مدیر وصاحب ان میتواند ان  را تغییر دهد 
"""
BusRoute_detail_destroy ="""
مدیر وصاحب ان میتواند ان  را پاک کند 
"""
# BusRoute docs
Ticket_list_get ="""
مدیر و صاحب بلیط میتواند بلیط را ببیند
"""
Ticket_list_post="""
فقط مسافر میتواند بلیط بخرد
model sample:
{
	"id":انتخاب ای دی بلیط ساخته شده  
}
"""
Ticket_detail_retrieve ="""
مدیر و صاحب بلیط میتواند بلیط را ببیند

"""
Ticket_detail_update="""
نمی توان اپدیت کرد
"""
Ticket_detail_patch="""
نمی توان اپدیت کرد
"""
Ticket_detail_destroy ="""
مدیر و صاحب بلیط میتوانند پاک کنند
"""
search_busroute = """
کاربر میتواند به کمک 
 search 
عبارتی که جلوی سرچ است موارد زیر را سرچ کرده و هر مسیری که تعریف شده به کاربر نشان می دهد
POST:
{
    "search": عبارت مورد جستجو
	"model" :مدل های که فیلد های ان را جستجو میکندبا , ازهم جداش شود تا مدل های مد نظر مورد جستجو قرار گیرد
}
field BusRoute:
begin  مبدا مسیر	
destination مقصد مسیر 
phone شماره تلفن راننده
date تاریخ حرکت
field Bus:
codebus کد اتوبوس
"""