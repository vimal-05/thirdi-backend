from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging
from .service import analyze_image
import asyncio
from .utils import extract_string
import json

@api_view(["POST"])
def image_analysis_view(request):
    """
    API endpoint to receive a string and process it for analysis.
    """

    if "data" not in request.data:
        return Response({"error": "No image url provided"}, status=400)
    image_url= request.data.get('data')
    # image_url = request.data["data"]

    analysis_result = asyncio.run(analyze_image(image_url))
    print(analysis_result)
    analysis_result=extract_string(analysis_result,"[","]")
    # print(analysis_result)
    return Response(analysis_result)
