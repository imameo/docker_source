import random

def play_game():
    # Xác định phạm vi số
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"Chào mừng bạn đến với trò chơi Đoán số!")
    print(f"Tôi đã chọn một số từ {lower_bound} đến {upper_bound}. Bạn hãy đoán xem đó là số nào nhé.")

    while True:
        try:
            # Lấy số dự đoán từ người dùng
            guess = int(input("Nhập số bạn đoán: "))
            attempts += 1

            # Kiểm tra số dự đoán
            if guess == secret_number:
                print(f"Chúc mừng! Bạn đã đoán đúng số {secret_number} chỉ sau {attempts} lần thử!")
                break
            elif guess < secret_number:
                print("Số bạn đoán quá nhỏ. Hãy thử lại với số lớn hơn.")
            else:
                print("Số bạn đoán quá lớn. Hãy thử lại với số nhỏ hơn.")
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")

if __name__ == "__main__":
    play_game()
