import gradio as gr
import os
import draw as draw

title = "Prescriptions"

if os.path.exists("example_images"): images = [f"example_images/{image}" for image in os.listdir("example_images")]

demo = gr.Interface(fn=draw.draw_BBOX, 
                    inputs=gr.Image(type="pil", label="Upload an image"),
                    outputs=[
                        gr.Image(type="pil"),    
                        gr.Textbox(label="Recognized Text"), 
                        gr.File(label="CSV File Download")        
                        ],        
                    title=title,                # Output the title
                    examples=images)            # Output the example images

# Launch the demo app
# Queue allows for output that takes longer than 2 minutes
demo.queue().launch()