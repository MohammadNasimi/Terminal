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
"""
Bus_list_post="""
"""
Bus_detail_retrieve ="""
"""
Bus_detail_update="""
"""
Bus_detail_patch="""
"""
Bus_detail_destroy ="""
"""
# BusRoute docs
BusRoute_list_get ="""
"""
BusRoute_list_post="""
"""
BusRoute_detail_retrieve ="""
"""
BusRoute_detail_update="""
"""
BusRoute_detail_patch="""
"""
BusRoute_detail_destroy ="""
"""
# BusRoute docs
Ticket_list_get ="""
"""
Ticket_list_post="""
"""
Ticket_detail_retrieve ="""
"""
Ticket_detail_update="""
"""
Ticket_detail_patch="""
"""
Ticket_detail_destroy ="""
"""