def isBalanced(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in pairs.values():  # Jika karakter adalah kurung buka
            stack.append(char)
        elif char in pairs:  # Jika karakter adalah kurung tutup
            if not stack or stack.pop() != pairs[char]:
                return False
    
    return not stack  # True jika stack kosong (semua kurung seimbang)

# ===== TEST CASES =====
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("((()))", True),
        ("[{()}]", True),
        ("[({)]", False),
        ("[[[]", False)
    ]
    
    print("=== Hasil Test Bracket Matcher ===")
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = isBalanced(input_str)
        print(f"Test {i}: {input_str:10} => {'✅' if result == expected else '❌'} (Hasil: {result}, Harusnya: {expected})")