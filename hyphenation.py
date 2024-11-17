def hyphenate_text(text):
    """Розбиває текст на слова з переносами."""
    def hyphenate_word(word):
        vowels = "аеєиіїоуюяaeiouy"
        parts = []
        current_part = ""

        for i in range(len(word)):
            current_part += word[i]
            
            if word[i].lower() in vowels and i < len(word) - 1:
                parts.append(current_part)
                current_part = ""

        parts.append(current_part)
        return "-".join(parts)
    
    words = text.split()  
    hyphenated_words = [hyphenate_word(word) for word in words]  
    return " ".join(hyphenated_words)  
