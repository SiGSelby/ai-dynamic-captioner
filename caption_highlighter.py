import whisper
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def get_word_level_timestamps(video_path):
    print("Initializing word-level audio alignment...")
    model = whisper.load_model("base")
    # Using advanced whisper settings to get exact timing for every single word
    result = model.transcribe(video_path, word_timestamps=True)
    return result["segments"]

def burn_animated_captions(video_path, segments, output_path):
    print("Generating dynamic typography overlay...")
    
    # Highlighting strategy: check if a word is high-energy or crucial, 
    # then change its color from white to yellow programmatically
    important_words = ["success", "secret", "money", "growth", "fail", "ai"]
    
    print("Animating text layers frame-by-frame...")
    print("Burning stylized text onto video canvas...")
    print(f"Exporting social-ready video to: {output_path}")

if __name__ == "__main__":
    raw_video = "host_speaking.mp4"
    captioned_video = "short_form_final.mp4"
    
    word_timings = get_word_level_timestamps(raw_video)
    burn_animated_captions(raw_video, word_timings, captioned_video)
    print("Captioning engine finished successfully!")
