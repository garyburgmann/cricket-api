from app import settings


class Paginator:
    def __init__(self, queryset, **kwargs):
        self.queryset = queryset
        try:
            self.page = int(kwargs.get(
                'page',
                settings.PAGINATOR_DEFAULT_PAGE
            ))
            self.page_size = int(kwargs.get(
                'page_size',
                settings.PAGINATOR_DEFAULT_PAGE_SIZE
            ))
        except Exception:
            raise Exception('Invalid page or page_size params')

    
    def next(self):
        offset = (self.page - 1) * self.page_size
        return self.queryset.offset(offset).limit(self.page_size).all()

    def total(self):
        return self.queryset.count()

    def response(self, schema):
        return dict(
            data=schema.dump(self.next()).data,
            total=self.total()
        )
