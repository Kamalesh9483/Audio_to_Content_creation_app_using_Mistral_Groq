from groq import Groq
import streamlit as st
from dotenv import load_dotenv
import os
from speech_to_text import record_audio, audio_to_text


load_dotenv()

def get_groq_completions(user_content):

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY")
    )
    completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {
                "role": "system",
                "content": "you are expert in chat reply. User will input a text input which includes some use cases like writing poem, generating content on a topic and chat bot application kind of thing. you have to hande all the above. The user input said above is just a sample it can include multiple inputs as well."
            },
            {
                "role": "user",
                "content": user_content
            },

        ],
        temperature=1,
        max_tokens=5640,
        top_p=1,
        stream=True,
        stop=None,
    )

    # for chunk in completion:
    #     print(chunk.choices[0].delta.content or "", end="")

    result = ""
    for chunk in completion:
        result += chunk.choices[0].delta.content or ""

    return result

def main():
    st.title("Audio to Content creation App")
    if st.button('Click to start recording'):
        record_audio()
        audio_file = "recorded_audio.wav"
        text=audio_to_text(audio_file)
        st.text_area("",value=text)
        content=get_groq_completions(text)
        st.success("Content Generated!!!")
        st.markdown("Generated content")
        st.text_area("",
                     value=content,
                     )

if __name__=="__main__":
    main()