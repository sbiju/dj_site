from rest_framework.pagination import LimitOffsetPagination


class BlogPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 3
    limit_query_param = 'limit'
    offset_query_param = 'offset'