class Student:
    # 클래스 변수 (전체 학생 관리용)
    student_list = []     # 모든 학생 객체 저장
    student_dict = {}     # { id: Student 객체 }
    count = 0             # 총 학생 수
    next_id = 1           # 다음 학생에게 줄 ID (자동 증가)

    def __init__(self, name, grade):
        # 인스턴스 변수
        self.id = Student.next_id
        self.name = name
        self.grade = grade

        # 클래스 변수 업데이트
        Student.next_id += 1
        Student.count += 1

        # 자동 등록
        Student.student_list.append(self)
        Student.student_dict[self.id] = self

    # ✅ 학생 1명 정보 출력 (인스턴스 메서드)
    def info(self):
        print(f"[ID: {self.id}] 이름: {self.name} | 학년: {self.grade}")

    # ✅ 전체 학생 수 반환 (클래스 메서드)
    @classmethod
    def how_many(cls):
        return cls.count

    # ✅ 전체 학생 목록 출력 (클래스 메서드)
    @classmethod
    def show_all(cls):
        if not cls.student_list:
            print("등록된 학생이 없습니다.")
            return
        print("=== 전체 학생 목록 ===")
        for student in cls.student_list:
            student.info()

    # ✅ 이름으로 검색 (클래스 메서드)
    @classmethod
    def find_by_name(cls, name):
        results = []
        for student in cls.student_list:
            if student.name == name:
                results.append(student)
        return results  # 리스트로 반환 (이름이 중복될 수 있으니까!)

    # ✅ 학년별 학생 수 (클래스 메서드)
    @classmethod
    def count_by_grade(cls, grade):
        cnt = 0
        for student in cls.student_list:
            if student.grade == grade:
                cnt += 1
        return cnt

    # ✅ 학생 삭제 (ID로)
    @classmethod
    def remove_by_id(cls, student_id):
        if student_id in cls.student_dict:
            student = cls.student_dict[student_id]
            
            # 리스트에서 제거
            cls.student_list.remove(student)
            # 딕셔너리에서 제거
            del cls.student_dict[student_id]
            # 전체 수 감소
            cls.count -= 1

            print(f"ID {student_id} 학생이 삭제되었습니다.")
        else:
            print("해당 ID의 학생이 존재하지 않습니다.")


s1 = Student("철수",2)
s2 = Student("영희",1)
s3 = Student("미애",4)
s4 = Student("철이",3)
s5 = Student("민수",4)
print(Student.find_by_name("철수"))
