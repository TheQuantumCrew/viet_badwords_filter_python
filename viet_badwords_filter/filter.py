class VNBadwordsFilter:
    def __init__(self):
        from .badwords_list import badwords
        self.badwords = set(badwords)

    def is_profane(self, text):
        words = text.lower().split()
        for word in words:
            if word in self.badwords:
                return True
        return False

    def clean(self, text):
        words = text.split()
        cleaned_words = [
            "***" if word.lower() in self.badwords else word for word in words
        ]
        return " ".join(cleaned_words)
