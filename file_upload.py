import gradio as gr
import os
import subprocess

def process_files(audio_file, video_file):
    if audio_file is None or video_file is None:
        return "Please upload both audio and video files", None
    
    # Audio file is already a path
    audio_path = audio_file
    
    # Video file is already a path
    video_path = video_file
    
    output_file = os.path.join('/home', 'ubuntu', 'HeyGem-Linux-Python-Hack', '1004-r.mp4')
    try:
        # Run the command with audio and video paths
        subprocess.run([
            'python', 
            '/home/ubuntu/HeyGem-Linux-Python-Hack/run.py',
            '--audio_path', audio_path,
            '--video_path', video_path
        ], check=True)
        return f"Files processed successfully", output_file
    except subprocess.CalledProcessError as e:
        return f"Error processing files: {str(e)}", None

# Create the Gradio interface
demo = gr.Interface(
    fn=process_files,
    inputs=[
        gr.Audio(label="Upload Audio File", type="filepath"),
        gr.Video(label="Upload Video File")
    ],
    outputs=[
        gr.Textbox(label="Status"),
        gr.File(label="Download Processed File")
    ],
    title="Audio-Video Processor",
    description="Upload audio and video files to process"
)

if __name__ == "__main__":
    demo.launch()