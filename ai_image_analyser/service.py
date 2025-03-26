from mistralai import Mistral
from django.conf import settings

async def analyze_image(image_url):

    # Retrieve the API key from environment variables
    api_key = settings.MISTRAL_API_KEY

    # Specify model
    model = "pixtral-12b-2409"

    # Initialize the Mistral client
    client = Mistral(api_key=api_key)

    # Define the messages for the chat
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": '''"Analyze the provided image and provide insights , no other response is required other than with the following structure,NB:don't add json in the begining:
                                [
                                    {
                                    "overall_score": <a value between 1 to 100 based on the percentage of score of the other three values.>,
                                    "visual_analysis": <a value between 1 to 10 based on the analysis of the visual aspects of the ad>,
                                    "textual_analysis": <a value between 1 to 10 based on the analysis of the textual aspects of the ad.>,
                                    "brand_analysis": <a value between 1 to 10 based on the analysis of the branding aspects of the ad.>
                                    },
                                    {
                                    overall_score: A comprehensive score between 1 and 100 that reflects the overall quality and effectiveness of the image.
                                    visual_analysis: A score between 1 and 10 that evaluates the visual appeal, composition, and design elements of the image.
                                    textual_analysis: A score between 1 and 10 that assesses the clarity, relevance, and impact of any text present in the image.
                                    brand_analysis: A score between 1 and 10 that judges how well the image aligns with and promotes the brand's identity and values.
                                    }
                                ]
                                Ensure that the scores are objective and based on a thorough analysis of the image.Be strict on giving score"'
                                '''
                },
                {
                    "type": "image_url",
                    "image_url":image_url
                }
            ]
        }
    ]

    # Get the chat response
    chat_response = client.chat.complete(
        model=model,
        messages=messages
    )

    # Print the content of the response
    return chat_response.choices[0].message.content

