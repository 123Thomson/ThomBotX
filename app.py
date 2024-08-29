import streamlit as st
import requests

# Set your Gemini API key here
API_KEY = 'AIzaSyBX7FjwaAgFT4-kBWw78U8nZ_D1YkyWdWs'  # Replace with your actual API key
API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'

def generate_essay(prompt):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'contents': [{
            'parts': [{
                'text': prompt
            }]
        }]
    }
    
    # Include the API key in the URL
    response = requests.post(f"{'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'}?key={'AIzaSyBX7FjwaAgFT4-kBWw78U8nZ_D1YkyWdWs'}", headers=headers, json=data)
    
    # Print the full response for debugging
    print("Response Status Code:", response.status_code)
    print("Response Body:", response.json())  # Print the entire response body

    if response.status_code == 200:
        response_data = response.json()
        # Adjust according to the actual response structure
        if 'candidates' in response_data and len(response_data['candidates']) > 0:
            return response_data['candidates'][0]['content']['parts'][0]['text']
        else:
            return 'No candidates found in response.'
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    st.title("content Generator using LLM")
    st.write("Enter your content topic or prompt below:")
    
    prompt = st.text_area("Prompt", "")
    
    if st.button("Generate content"):
        if prompt:
            with st.spinner("Generating content..."):
                essay = generate_essay(prompt)
                st.success("content generated successfully!")
                st.write(essay)
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()
