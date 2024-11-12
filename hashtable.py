def hash_function(key):
    return key % 10

class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        self.size = 10  # 해시 테이블의 크기
        self.table = [None] * self.size  # 초기화된 해시 테이블

    def find_slot(self, key):
        i = hash_function(key)
        start = i
        while (self.table[i] is not None) and (self.table[i].key != key):
            i = (i + 1) % self.size
            if i == start:
                return 'Full'
        return i
    
    def set(self, key, value=None):
        i = self.find_slot(key)
        if i == 'Full':
            print("해시 테이블이 가득 찼습니다.")
            return None
        if self.table[i] is not None:
            self.table[i].value = value
        else:
            self.table[i] = Element(key, value)
        print(f"키 {key}와 값 {value}가 인덱스 {i}에 설정되었습니다.")
    
    def search(self, key):
        i = hash_function(key)
        start = i
        while self.table[i] is not None:
            if self.table[i].key == key:
                return self.table[i].value
            i = (i + 1) % self.size
            if i == start:
                break
        return None  # 키가 존재하지 않음
    
    def remove(self, key):
        i = self.find_slot(key)
        if self.table[i] is None or self.table[i].key != key:
            print("해당 키가 해시 테이블에 존재하지 않습니다.")
            return None
        
        print(f"키 {key}를 인덱스 {i}에서 삭제합니다.")
        self.table[i] = None  # 해당 위치를 None으로 설정하여 요소 삭제

        # 삭제 후 재해싱 수행
        j = (i + 1) % self.size
        while self.table[j] is not None:
            k = hash_function(self.table[j].key)
            # 재배치가 필요한 조건 확인: j < k < i or k < i < j or i < j < k
            if (j < k <= i) or (k <= i < j) or (i < j < k):
                self.table[i] = self.table[j]  # j의 요소를 i 위치로 이동
                self.table[j] = None  # j를 비움
                i = j  # 새로운 빈 칸은 j 위치
            j = (j + 1) % self.size

    def display(self):
        for idx, element in enumerate(self.table):
            if element is None:
                print(f"인덱스 {idx}: 비어있음")
            else:
                print(f"인덱스 {idx}: (키: {element.key}, 값: {element.value})")

# 예제 사용
hash_table = HashTable()
hash_table.set(15, "Apple")
hash_table.set(25, "Banana")
hash_table.set(35, "Orange")
hash_table.display()

print("\n키 25 검색:", hash_table.search(25))
hash_table.remove(25)
print("\n25 삭제 후 해시 테이블 상태:")
hash_table.display()