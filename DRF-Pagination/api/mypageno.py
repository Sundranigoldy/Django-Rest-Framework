from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

# class MyPageNumber(PageNumberPagination):
#     page_size=5
#     page_size_query_param = 'records'
#     #this feature will let client to decide how many pages he needs
#     #http://127.0.0.1:8000/?&records=6
#     #than this will define pagesize =6
#     max_page_size = 7
#     #this will set even for client that he cant set pagination more than 7..
    
#limitoffset pagination

# class MyLimitoffsetPagination(LimitOffsetPagination):
#     default_limit = 5

    # offset_query_param = 'myoffset' # changing the name now instead of just writing offset now we can write myoffset
    #http://127.0.0.1:8000/?limit=5 & offset=5, now instead of offst we can change to myoffset and same goes for limit name can be changed
#my limit meaning how many pages and offset meaning kaha se dekhna hai

#Cursor Pagination

class MyCursorPagination(CursorPagination):
    page_size =5

# when u do this it gives u following error
#Cannot resolve keyword 'created' into field. Choices are: id, name, roll
#it is something coming from inbuilt created function. and we need to overirde the same by using ordering function
    ordering = 'name'