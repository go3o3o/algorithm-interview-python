# https://leetcode.com/problems/remove-duplicate-letters/

def removeDuplicateLettersUsingRecursive(self, s: str) -> str:
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        # 전체 집합과 접미사 일치할 때 분리 진행
        if set(s) == set(suffix):
            return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''

def removeDuplicateLettersUsingStack(self, s: str) -> str:
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen: continue 
        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)