from drf_yasg import openapi

begin = openapi.Parameter('begin',
                              openapi.IN_QUERY, description="begin param", type=openapi.TYPE_STRING)

destination= openapi.Parameter('destination',
                              openapi.IN_QUERY, description="destination param",
                              type=openapi.TYPE_STRING)
codebus =openapi.Parameter('codebus',
                              openapi.IN_QUERY, description="codebus param",
                              type=openapi.TYPE_STRING)
date =openapi.Parameter('date',
                              openapi.IN_QUERY, description="date param",
                              type=openapi.TYPE_STRING)

datefirst =openapi.Parameter('datefirst',
                              openapi.IN_QUERY, description="datefirst param",
                              type=openapi.TYPE_STRING)
dateend =openapi.Parameter('dateend',
                              openapi.IN_QUERY, description="dateend param",
                              type=openapi.TYPE_STRING)
# search =openapi.Parameter('search',
#                               openapi.IN_QUERY, description="search param",
#                               type=openapi.TYPE_STRING)
# model =openapi.Parameter('model',
#                               openapi.IN_QUERY, description="model param",
#                               type=openapi.TYPE_STRING)