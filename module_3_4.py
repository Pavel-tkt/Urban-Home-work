#закрепить знание использования параметров *args/ **kwargs на практике

def single_root_words(root_word, *other_words):
    same_words=[]
   #Функция должна составить новый список same_words только из тех слов списка other_words,
    # содержат root_word или наоборот root_word содержит одно из этих слов.
    for i in (other_words):  #переборка нужных слов
        word_low = i.lower()
        if root_word.lower() in word_low or word_low in root_word.lower():
            same_words.append(word_low)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)