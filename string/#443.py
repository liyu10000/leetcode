class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0, 0
        count = 0
        for read,c in enumerate(chars):
            # print(read, write, chars)
            if read == len(chars) - 1 or chars[read+1] != c:
                chars[write] = c
                write += 1
                if count:
                    for c in str(count+1):
                        chars[write] = c
                        write += 1
                count = 0
            else:
                count += 1
        # print(write, chars)
        return write