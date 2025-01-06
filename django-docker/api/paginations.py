import math

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Any

from marshmallow.fields import String
from rest_framework import pagination
from rest_framework.response import Response


@dataclass_json
@dataclass
class PaginationResponse:
    count: int
    next: String
    previous: String
    page_size: int
    results: Any


class NumberPagination(pagination.PageNumberPagination):

    # Path Query parameter ?page=1&page_size=5
    def get_paginated_response(self, data):
        pagination_response = PaginationResponse(
            count=self.page.paginator.count,
            next= self.get_next_link(),
            previous=self.get_previous_link(),
            page_size=self.get_page_size(self.request),
            results=data,
        ).to_dict()

        return Response(pagination_response)