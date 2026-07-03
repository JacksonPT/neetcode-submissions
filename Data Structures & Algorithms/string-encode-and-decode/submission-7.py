class Solution:
    #[helllo, im, cool, and, awesome] -> helllo im cool and awesome -> same List
    # 6#hello2#im
    def encode(self, strs: List[str]) -> str:
        s = ''
        for x in strs:
            s += str(len(x)) + '#' + x
        return s
    def decode(self, s: str) -> List[str]:
        i = 0
        l = []
    
        while i < len(s):
            g = s.find('#', i)
            length = int(s[i:g])
            begin = g + 1
            end = begin + length
            add = s[begin:end]
            l.append(add)
            i = end
            
            
        return l




            
                