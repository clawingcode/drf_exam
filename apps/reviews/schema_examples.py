from drf_spectacular.utils import OpenApiParameter, OpenApiTypes
from core import settings


REVIEW_PARAM_EXAMPLE = [
    OpenApiParameter(
        name="page",
        description="Retrieve a particular page. Defaults to 1",
        required=False,
        type=OpenApiTypes.INT,
    ),
    OpenApiParameter(
        name="page_size",
        description=f"The amount of item per page you want to display. Defaults to {settings.REST_FRAMEWORK['PAGE_SIZE']}",
        required=False,
        type=OpenApiTypes.INT,
    ),
]