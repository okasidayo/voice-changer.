import pyautogui
import speech_recognition as sr
import threading
import subprocess

# クリップボードにコピーする関数
def copy_to_clipboard(text):
    cmd = f'echo {text.strip()} | clip'
    subprocess.run(cmd, shell=True)

def listen_and_record():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("起動完了！")
        
        while True:
            try:
                # 音声の認識開始
                audio = recognizer.listen(source)
                
                # Google Speech Recognition で音声をテキストに変換
                text = recognizer.recognize_google(audio, language='ja-JP')
                print("コピーされたテキスト:", text)
                
                # 認識したテキストをクリップボードにコピー
                copy_to_clipboard(text)
                
            except sr.UnknownValueError:
                print("音声を認識できませんでした")
            except sr.RequestError:
                print("音声を認識できませんでした")

if __name__ == "__main__":
    listen_and_record()
