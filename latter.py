latter = """Dear <|Name|>
You are slected
Date: <|Date|>
"""
name = input("Write your name")
date = input("Enter date")
latter = latter.replace("<|Name|>", name)
latter = latter.replace("<|Date|>", date)
print(latter)