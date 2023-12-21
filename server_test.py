import requests
import time

headers = {}
API_URL = "http://0.0.0.0:8812/api/generate"


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def show_prompt_response(inputs, parameters=None, debug=False):
    start = time.time()
    payload = {"inputs": inputs}
    if parameters is not None:
        payload["parameters"] = parameters
    if debug:
        print(f"Input: {payload}")
    data = query(payload)
    if debug:
        print(f"Response: {data}")
    end = time.time()
    print(f"Time to response: {end-start:.3f}")
    print(f"\033[94m{inputs}\033[0m", end="")
    print(data["generated_text"])

show_prompt_response("def fibonacci(n):", {"max_new_tokens": 50, "temperature": 0.2})

prompt = """
#include <algorithm>
#include <vector>

int main() {
    auto v = std::vector<int>{1, 4, 2, 3};

    // Get sorted indices of the input"""
show_prompt_response(prompt, {"max_new_tokens": 128, "max_time": 2.0, "temperature": 0.1, "do_sample": False, "top_p": None})
