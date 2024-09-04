class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        # populate word dict
        word_dict = {}
        for word in words:
            if word not in word_dict:
                # start at zero to track word occurance
                word_dict[word] = [0, 1]
            else:
                word_dict[word][1] += 1


        # set increment to length of each word
        inc = len(words[0])

        # goal count for each word appearing once, count for tracking current status
        goal_count = len(words)
        count = 0

        # right and left bounds 
        right = inc
        left = 0

        # current word tracker and rightmost word tracker
        left_word = ''
        right_word = ''

        # output
        out_array = []

        while right <= len(s):
            curr_word = s[left:right]
            print(curr_word)
            print(s[left:right])
            temp_right = right
            temp_left = left

            if curr_word in word_dict:
                while curr_word in word_dict and count != goal_count:
                    word_dict[curr_word][0] += 1

                    if word_dict[curr_word][0] == word_dict[curr_word][1]:
                        count += word_dict[curr_word][1]
                    elif word_dict[curr_word][0] == word_dict[curr_word][1] + 1:
                        count -= word_dict[curr_word][1]
                    


                    temp_right += inc
                    temp_left += inc
                    curr_word = s[temp_left:temp_right]

                if count == goal_count:
                    print('\nSuccess')
                    print(right_word)
                    print(s[left:right])
                    print(left)
                    print('Success\n')
                    out_array.append(left)
                    right = temp_right - 1
                    left = temp_right - 1
                    count = 0
                    for key in word_dict:
                        word_dict[key][0] = 0
                else:
                    right += inc
                    left += inc
            
            right += 1
            if right >= inc:
                left += 1

            


            # print(right)
            # print(len(s))
            # print(s[left:right])
            # print(word_dict)
            # print(count)
            # print(goal_count)


            # # right_word = s[right:right+inc]

            # if right_word in word_dict:
            #     word_dict[right_word][0] += 1

            #     if word_dict[right_word][0] == word_dict[right_word][1]:
            #         count += word_dict[right_word][1]
            #     elif word_dict[right_word][0] == word_dict[right_word][1] + 1:
            #         count -= word_dict[right_word][1]

            #     right += inc

            # if right >= goal_count * inc:
            #     left_word = s[left:left+inc]

            #     if left_word in word_dict:
            #         word_dict[left_word][0] -= 1

            #         if word_dict[left_word][0] == word_dict[left_word][1]:
            #             count += word_dict[left_word][1]
            #         elif word_dict[left_word][0] == word_dict[left_word][1] - 1:
            #             count -= word_dict[left_word][1]

            #     left += inc

            # else:
            #     right += 1

            #     if right >= inc:
            #         left += 1



            


            # if count == goal_count:
            #     print('\nSuccess')
            #     print(right_word)
            #     print(s[left:right])
            #     print(left)
            #     print('Success\n')
            #     out = left 
            #     out_array.append(out)
            
            # right += inc


        
        return out_array
