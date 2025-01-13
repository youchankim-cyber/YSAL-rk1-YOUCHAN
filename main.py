from html2image import Html2Image
import base64
from IPython.display import display, HTML
from PIL import Image

def generate_profile(name, student_major, team, photo_path, introduction, output_image_path="profile_output.png"):
    """
    Generates and displays the profile in HTML format and saves it as an image with the photo on the left and text on the right.
    """
    # Convert the image to base64 after ensuring it's square
    photo_tag = "<p>[Photo not available]</p>"
    if photo_path:
        base64_photo = image_to_base64(photo_path)
        photo_tag = f'<img src="data:image/jpeg;base64,{base64_photo}" alt="Profile Photo" class="profileImg" />'
    base64_background = image_to_base64("basketball.jpg")

    # HTML content with embedded CSS for the layout
    div_content = f"""
    <style>
        body {{
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #000;
        }}
        .card {{
            font-family: Arial, sans-serif;
            background-image: url('data:image/webp;base64,{base64_background}');
            background-size: cover;
            width: 1920px;
            height: 1080px;
            display: flex;
            box-sizing: border-box;
            color: white;
        }}
        .photo-container {{
            flex: 1.5;
            display: flex;
            width: 40%;
            justify-content: center;
            align-items: center;
            height: 100%;
        }}
        .profileImg {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        .content {{
            flex: 2;
            padding: 20px;
            display: flex;
            color: black;
            flex-direction: column;
            justify-content: center;
        }}
        .content h1 {{
            margin-bottom: 20px;
        }}
        .content p {{
            margin: 10px 0;
        }}
    </style>
    <div class="card">
        <div class="photo-container">
            {photo_tag}
        </div>
        <div class="content">
            <h1>Profile</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Major:</strong> {student_major}</p>
            <p><strong>Team:</strong> {team}</p>
            <h3>Introduction</h3>
            <p>{introduction}</p>
        </div>
    </div>
    """

    # Display HTML in Jupyter Notebook
    display(HTML(div_content))

    hti = Html2Image()
    hti.screenshot(
        html_str=div_content,
        save_as=output_image_path,
        size=(1920, 1080)
    )
    print(f"Profile card saved as image: {output_image_path}")


def image_to_base64(image_path):
    """
    Converts an image file to base64 string.
    """
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# 과제-1:팀 이름 입력
team = "소속팀(농구/야구/축구/E-Sports)"
# 과제-2:본인을 나타내는 사진을 !반드시! 동일 폴더 안에 넣고 파일명을 입력해주세요
photo_path = "image.jpg"
# 과제-3 네 줄 이하(공백포함 영어 270자, 한글 130자 이내)의 짧은 소개글을 써주세요
introduction = "Hello! I am part of the AI Development Team and have a strong interest in Python programming and data analysis."

# User inputs
name = input("Enter your name: ")
student_major = input("Enter your major: ")

# Generate and save profile as an image
generate_profile(name, student_major, team, photo_path, introduction, output_image_path=name+"_profile.png")