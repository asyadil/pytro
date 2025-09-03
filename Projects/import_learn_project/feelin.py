def convert_mood(mood_list):
    
    # Dict buat mapping mood ke emoji
    mood_mapping = {
        "senang": "😀😀😀",
        "biasa": "😐",
        "sedih": "😢😢",
        "semangat": "💪🔥🔥"
    }
        
    # ganti mood jadi emoji
    return list(map(lambda mood: mood_mapping.get(mood), mood_list))