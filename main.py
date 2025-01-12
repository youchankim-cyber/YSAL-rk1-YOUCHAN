from html2image import Html2Image
import base64
from IPython.display import display, HTML
from PIL import Image

def generate_profile(name, student_major, team, photo_path, introduction, output_image_path="profile_output.png"):
    """
    Generates and displays the profile in HTML format and saves it as an image with gradient border effect around the photo.
    """
    # Convert the image to base64 after ensuring it's square
    photo_tag = "<p>[Photo not available]</p>"
    if photo_path:
        square_photo_path = create_square_image(photo_path)  # 이미지 정방형으로 자르기
        base64_photo = image_to_base64(square_photo_path)  # Base64로 변환
        photo_tag = f'<img src="data:image/jpeg;base64,{base64_photo}" alt="Profile Photo" class="profileImg" />'
    
    # HTML content with embedded CSS for the gradient and circular photo with a white ring around it
    div_content = f"""
    <style>
        body {{
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f4f4f4; /* 배경색 */
        }}
        .profileImgWrapper {{
            position: relative;
            width: 200px;  /* 전체 크기 */
            height: 200px;  /* 전체 크기 */
            border-radius: 50%;  /* 원형 테두리 */
            background-image: linear-gradient(to right, #ff7f50 0%, #ff1493 100%);  /* 그라데이션 테두리 */
            display: flex;
            justify-content: center;
            align-items: center;
        }}

        .profileImg {{
            border: 5px solid white;  /* 흰색 테두리 */
            width: 180px;  /* 작은 이미지 크기 */
            height: 180px;  /* 작은 이미지 크기 */
            border-radius: 50%;
            object-fit: fill;
            margin-left: -2.5px;
            margin-top: -2.5px;
        }}
    </style>
    <div style="font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; max-height: 400px; border: 1px solid #ddd; padding: 20px; border-radius: 10px; display: flex; align-items: center;">
        <div style="flex: 2;">
            <h2 style="color: #2c3e50;">Profile</h2>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Major:</strong> {student_major}</p>
            <p><strong>Team:</strong> {team}</p>
            <h3 style="color: #2c3e50;">Introduction</h3>
            <p>{introduction}</p>
        </div>
        <div style="flex: 1; text-align: center;">
            <div class="profileImgWrapper">
                <div class="profileImg">
                    {photo_tag}
                </div>
            </div>
        </div>
    </div>
    """
    
    # Display HTML in Jupyter Notebook
    display(HTML(div_content))
    
    hti = Html2Image()
    hti.screenshot(
        html_str=div_content,
        save_as=output_image_path,
        size=(801, 401)  # 캡처 크기를 카드에 맞게 설정
    )
    print(f"Profile card saved as image: {output_image_path}")


def create_square_image(image_path):
    """
    Creates a square image by cropping or resizing the given image.
    """
    img = Image.open(image_path)
    
    # Make the image square by resizing to the smallest dimension and cropping
    size = min(img.size)
    left = (img.width - size) / 2
    top = (img.height - size) / 2
    right = (img.width + size) / 2
    bottom = (img.height + size) / 2
    
    img_cropped = img.crop((left, top, right, bottom))
    
    # Save the cropped image as a new file
    square_image_path = "square_image.jpg"
    img_cropped.save(square_image_path)
    
    return square_image_path


def image_to_base64(image_path):
    """
    Converts an image file to base64 string.
    """
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')
# 과제:팀 이름 입력
team = "소속팀(농구/야구/축구/E-Sports)"
# 과제:사진을 반드시 동일 폴더 안에 넣고 파일명을 입력해주세요
photo_path = "image.jpg"
# 과제 네 줄 이하(공백포함 영어 270자, 한글 130자 이내)의 짧은 소개글을 써주세요
introduction = "Hello! I am part of the AI Development Team and have a strong interest in Python programming and data analysis.Hello! I am part of the AI Development Team and have a strong interest in Python programming and data analysis. Hello! I am part of the AI Development and have a"

# User inputs
name = input("Enter your name: ")
student_major = input("Enter your major: ")


# Generate and save profile as an image
generate_profile(name, student_major, team, photo_path, introduction, output_image_path="profile_output.png")
