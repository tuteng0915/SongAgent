import gradio as gr
from pipeline import pipe
# from qwen_audio import ask_qwen_audio
from assistant import assistant

def run(message, history, prof, aout, lyr, tg, pth):
    var_dict = {
        'preference': prof,
        'lyrics': lyr,
        'tags': tg,
        'path': pth,
    }
    copy = history.copy()
    copy.append({
        'role': 'user',
        'content': message
    })
    for response in assistant.run(messages=copy, var_dict=var_dict):
        ...
    new_lyr = var_dict['lyrics']
    new_tg = var_dict['tags']
    new_aout = var_dict['path']
    return response, new_lyr, new_tg, (new_aout if new_aout != '' else 'blank.wav'), new_aout

with gr.Blocks() as demo:
    path_name = gr.State('')
    with gr.Row():
        with gr.Column(scale=3):
            lyrics = gr.TextArea(label="lyrics", scale=2, max_lines=100, interactive=True)
            tags = gr.Textbox(label="tags", interactive=True)
            generate_btn = gr.Button("Generate")
            length = gr.Slider(30, 300, step=1, label='length', interactive=True)
            audio_output = gr.Audio(label="audio output", interactive=False)
            with gr.Accordion(label="user preference", open=False):
                audio_input = gr.Audio(sources='upload', label="input preference")
                profile = gr.TextArea(label="profile", interactive=True)
                update_btn = gr.Button("Update Profile")
        with gr.Column(scale=5):
            # chatbot = gr.Textbox(label="chatbot")
            chatbot = gr.ChatInterface(
                run,
                type='messages',
                additional_inputs=[profile, audio_output, lyrics, tags, path_name],
                additional_outputs=[lyrics, tags, audio_output, path_name],
                fill_height=True
            )

    @generate_btn.click(inputs=[lyrics, tags, length], outputs=[audio_output, path_name])
    def generate_music(lyr, tg, lth):
        outputs = pipe(
            format='wav',
            audio_duration=lth,
            prompt=tg,
            lyrics=lyr,
        )
        # print(outputs)
        return outputs[0], outputs[0]

    @update_btn.click(inputs=[audio_input, chatbot, lyrics, tags, profile], outputs=profile)
    def baz(audio, chat, lyr, tg, old_profile):
        return "placeholder"

    # gr.Markdown("# Test")

demo.launch(share=True, server_name='0.0.0.0')

