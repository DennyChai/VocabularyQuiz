from Vocabularies import vocabularies
import random
import queue
import re

# TODO: pyinstaller -F --name=Quiz main.py

my_quiz_items = queue.Queue()


def quiz():
    _continue = "Y"
    while _continue == "y" or _continue == "Y":
        score = 0
        answer_record = []
        items = input(f"這次的考試，要考幾題? 目前只有{len(vocabularies)}題的題目\n")
        start = validation(items)
        while not start:
            # print(f"\033[91m只能輸入數字或者輸入小於等於{len(vocabularies)}的數字!\033[0m")
            print(f"只能輸入數字或者輸入小於等於{len(vocabularies)}的數字!")
            items = input(f"這次的考試，要考幾題? 目前只有{len(vocabularies)}題的題目\n")
            start = validation(items)
        vocabularies_key = list(vocabularies.keys())
        random.shuffle(vocabularies_key)
        for count, vocabulary in enumerate(vocabularies_key, start=1):
            if count > int(items):
                break
            my_quiz_items.put(vocabulary)
        while not my_quiz_items.empty():
            word = my_quiz_items.get()
            answer = input(f"{word} 這個單字的意思是甚麼?\n")
            explanation = f"  單字: {word:20} 說明 =  {vocabularies[word]:50}"
            if answer != "" and answer in vocabularies[word]:
                answer_record.append(f"| 正確 |{explanation}")
                score += 1
            else:
                # answer_record.append(f"| \033[91m錯誤\033[0m |{explanation}")
                answer_record.append(f"| 錯誤 |{explanation}")
        print(f"總分: {score}/{items} = {(score/int(items))*100:.0f}%\n")
        print("\n".join(answer_record))
        _continue = input(f"要繼續考試嗎? (Y/N):\n")


def validation(items: str):
    if re.search(r"[0-9]+", items) and len(vocabularies) >= int(items):
        return True
    return False


if __name__ == "__main__":
    quiz()
