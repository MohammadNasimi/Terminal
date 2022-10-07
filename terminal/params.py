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