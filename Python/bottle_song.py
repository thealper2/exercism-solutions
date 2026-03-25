def recite(start, take=1):
    lyrics = []
    numbers = ["no", "One", "Two", "Three", "Four", "Five", "Six", 
               "Seven", "Eight", "Nine", "Ten"]
    
    for i in range(start, start - take, -1):
        bottle = "bottles" if i != 1 else "bottle"
        next_bottle = "bottles" if i - 1 != 1 else "bottle"
        next_num = numbers[i - 1].lower()
        
        lyrics.append(f"{numbers[i]} green {bottle} hanging on the wall,")
        lyrics.append(f"{numbers[i]} green {bottle} hanging on the wall,")

        lyrics.append(f"And if one green bottle should accidentally fall,")
        lyrics.append(f"There'll be {next_num} green {next_bottle} hanging on the wall.")
        
        lyrics.append("")

    return lyrics[:-1]
