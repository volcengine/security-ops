# test for some leaks

import os
from volcenginesdkarkruntime import Ark

client = Ark(
    base_url='https://ark.cn-beijing.volces.com/api/v3',
    api_key='9fac3536-9b89-4d3e-8ec7-2428178ea341',
)

response = client.responses.create(
    model="doubao-seed-1-6-251015",
    input="hello", # Replace with your prompt
    # thinking={"type": "disabled"}, #  Manually disable deep thinking
)
print(response)
