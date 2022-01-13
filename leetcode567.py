


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #  if len(s2) == 0:
            #  return False
         # s1的哈希表映射  
         hashmap_s1 = {}
         for ch in s1:
             hashmap_s1[ch] = hashmap_s1.get(ch,0) + 1
         
         start = 0
         hashmap_s2 = {}
         # 哈希表s2的映射 
         for end in range(len(s2)):
             tail = s2[end]
             hashmap_s2[tail] = hashmap_s2.get(tail,0) + 1

             if hashmap_s1 == hashmap_s2:
                 return True
            
             if end >= len(hashmap_s1) - 1:
                 head = s2[start]
                 hashmap_s2[head] -= 1

                 if hashmap_s2[head] == 0:
                     del hashmap_s2[head]
                 start += 1
         return False

if __name__ == '__main__':

    solution = Solution()

    # s1 = "ab" 
    # s2 = "eidbaooo"
    # s2 = 'eidboaoo'

    s1 = "abcdxabcde"
    s2 = "abcdeabcdx"

    result = solution.checkInclusion(s1, s2)

    print(result)