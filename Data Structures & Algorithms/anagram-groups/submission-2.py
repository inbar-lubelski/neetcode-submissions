class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        map_=defaultdict(list)
        for st in strs:
            letters= [0]*26
            for ch in st:
                letters[ord(ch)-ord('a')]+=1
            map_[tuple(letters)].append(st)
        return list(map_.values()) 
                

        
        