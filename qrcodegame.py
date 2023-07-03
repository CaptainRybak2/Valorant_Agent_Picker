import random
import qrcode
import tempfile
import webbrowser

def generate_math_problem():
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)
    if operator == '/':
        # To avoid division by zero, ensure the denominator is not 0
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 10)
        result = num1 / num2
    else:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        result = eval(str(num1) + operator + str(num2))
    problem = f"{num1} {operator} {num2} = ?"
    return problem, result

def display_qr_code(text):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    
    # Generate the QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code image to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    temp_filename = temp_file.name
    qr_img.save(temp_filename)
    
    # Open the QR code image in the default image viewer
    webbrowser.open(temp_filename)

def main():
    while True:
        problem, result = generate_math_problem()
        print(f"Solve the following math problem:\n{problem}")
        user_result = float(input("Enter your answer: "))
        
        if user_result == result:
            qr_text = "Kwsta Jypna"
        else:
            qr_text = "Oops! Incorrect answer."
            print(qr_text)
            continue
        
        display_qr_code(qr_text)
        break

if __name__ == "__main__":
    main()
