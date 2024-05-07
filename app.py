from g4f.client import Client
import gradio as gr

client = Client()

def generate_writing_prompt(user_input):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
    )
    return response.choices[0].message.content

#Gradio UI
interface = gr.Interface(
    fn=generate_writing_prompt,
    inputs= gr.Textbox(lines=3, placeholder="Enter your prompt here..."),
    outputs="text",
    title="MyGPT 📖",
    description="Always here to help ask me anything!🤟🏻",
    theme="huggingface",
    examples=[
        ["A story about a lost civilization discovering technology."],
        ["Compose a poem about the changing seasons."],
        ["A suspense thriller set in an abandoned mansion."],
    ]
)

if __name__ == "__main__":
    interface.launch()