class Solution:
    def sortSentence(self, s: str) -> str:
        list1 = s.split()
        list2 = []
        for i in range(len(list1)):
            list2.append('')
        for word in list1:
            n = len(word)
            index_list2 = int(word[n - 1]) - 1
            list2[index_list2] = word[:-1]
        final_sentence = ' '.join(list2)
        return final_sentence