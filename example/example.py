from viet_badwords_filter.filter import VNBadwordsFilter

def main():
    filter = VNBadwordsFilter()

    # Ví dụ kiểm tra từ ngữ không phù hợp
    text1 = "hello"
    text2 = "vcl"

    print(f"'{text1}' có phải là từ không phù hợp không? {filter.is_profane(text1)}")
    print(f"'{text2}' có phải là từ không phù hợp không? {filter.is_profane(text2)}")

    # Ví dụ làm sạch từ ngữ không phù hợp
    text3 = "hello vcl"
    print(f"Trước: {text3}")
    print(f"Sau: {filter.clean(text3)}")

if __name__ == "__main__":
    main()
